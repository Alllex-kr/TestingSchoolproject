<script setup>
import {ref, watchEffect} from 'vue'
import DiceButton from "@/components/DiceButton.vue";
import LiveButton from "@/components/LiveButton.vue";
// define component props for the slider component
const {min, max, step, modelValue, unit} = defineProps({
  min: {
    type: Number,
    default: 0,
  },
  max: {
    type: Number,
    default: 100,
  },
  step: {
    type: Number,
    default: 1,
  },
  modelValue: {
    type: Number,
    default: 500,
  },
  unit: {
    type: String,
    default: "",
  },
  info: {
    type: String,
    default: "",
  },
});
// define emits for the slider component
const emit = defineEmits(["update:modelValue"]);
// define refs for the slider component
const sliderValue = ref(modelValue);
const slider = ref(null);
// function to get the progress of the slider
const getProgress = (value, min, max) => {
  return ((value - min) / (max - min)) * 100;
};
// function to set the css variable for the progress
const setCSSProgress = (progress) => {
  slider.value.style.setProperty("--ProgressPercent", `${progress}%`);
};
// watchEffect to update the css variable when the slider value changes
watchEffect(() => {
  if (slider.value) {
    // emit the updated value to the parent component
    emit("update:modelValue", sliderValue.value);
    // update the slider progress
    const progress = getProgress(
        sliderValue.value,
        slider.value.min,
        slider.value.max
    );
    // define extra-width to ensure that the end of progress is always under the slider thumb.
    let extraWidth = (100 - progress) / 10;
    // set the css variable
    setCSSProgress(progress + extraWidth);
  }
});
//define values for the slider
const amountPanels = ref(500)
const powerFeed = ref(50)
const sunPower = ref(50)
const season = ref(1)
//Additional Info for the sliders
const panelInfo = "One panel has 10 m²."
const powerInfo = "Energy used for direct power feed."
const sunInfo = "Sunpower"
const seasonInfo = "Spring(1), Summer(2), Fall(3), Winter(4)"
//Units for the sliders
const panelUnit = "pc"
const powerUnit = "%"
const sunUnit = "%"
const seasonUnit = "Choose a season"
//fix values
const energyPerHour = 1250
const household = ref(0)

function calculate() {
  const seasonValue = getSeasonValue()
  const sunValue = getSunPowerValue()
  const energyProduction = (sunValue * (amountPanels.value * 10) * 0.15 * 0.85) * seasonValue
  const energyUsageForHouseholds = energyProduction * (powerFeed.value / 100)
  household.value = Math.round(energyUsageForHouseholds / energyPerHour);
}

//energy production changes per season - returns values for calculation
function getSeasonValue() {
  if (season.value === 1) {
    return 0.8
  } else if (season.value === 2) {
    return 1
  } else if (season.value === 3) {
    return 0.6
  } else {
    return 0.5
  }
}

function getSunPowerValue() {
  if (sunPower.value === 0) {
    return 200
  } else if (sunPower.value === 25) {
    return 400
  } else if (sunPower.value === 50) {
    return 600
  } else if (sunPower.value === 75) {
    return 900
  } else {
    return 1200
  }
}

//variables for popups
const tutorialStart = ref(false)
const tutorialNext = ref(false)
const lastTutorial = ref(false)

function updateDataFromNamedChannel(data, name) {
  const channelNameToFind = name;
  let foundValue = null;
  data.forEach(item => {
    // Check if the 'channels' property exists and it's an array
    if (Array.isArray(item.channels)) {
      const foundChannel = item.channels.find(channel => channel.channelName === channelNameToFind);
      if (foundChannel) {
        foundValue = foundChannel.value;
      }
    }
  });
  if (foundValue != null) {
    // Extract the value associated with the found channel and update it
    switch (name) {
      case 'PanelCount':
        amountPanels.value = foundValue;
        console.log(`Updated amountPanels to: ${amountPanels.value}`);
        break;
      case 'CurrentSolarPower':
        if (foundValue <= 25) {
          sunPower.value = 0;
        }
        if (foundValue <= 50) {
          sunPower.value = 25;
        }
        if (foundValue <= 75) {
          sunPower.value = 75;
        }
        if (foundValue > 75) {
          sunPower.value = 100;
        }
        console.log(`Updated amountPanels to: ${sunPower.value}`);
        break;
    }
  } else {
    console.error(`Channel '${channelNameToFind}' not found in the data.`);
  }
}

async function fetchDataFromServer() {
  fetch('http://localhost:3000/data')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Data from JSON server:', data);
        updateDataFromNamedChannel(data, 'PanelCount')
        updateDataFromNamedChannel(data, 'CurrentSolarPower')
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
}

function onClickLive() {
  fetchDataFromServer(), calculate()
}

const updateSimulation = (newValues) => {
  // Update your simulation state with the new random values
  season.value = newValues.season;
  sunPower.value = newValues.sunPower;
  amountPanels.value = newValues.panelCount;
  powerFeed.value = newValues.powerFeed;

  // Recalculate after updating
  calculate();
};

</script>
<template>
  <div class="topBar">
    <div class="singleButtonElement leftPart">
      <LiveButton @click="onClickLive"></LiveButton>
      <div v-if="tutorialNext" class="popup" id="popupLive">
        <div class="popup-inner">
          <p class="popupText">You can check the live data from the last 24 hours.</p>
          <button @click="tutorialNext = false" class="popupButtons">Close</button>
          <button @click="tutorialNext = false, lastTutorial = true" class="popupButtons">Got it!</button>
        </div>
      </div>
    </div>
    <div class="singleButtonElement rightPart">
      <DiceButton @dice-rolled="updateSimulation"></DiceButton>
      <div v-if="lastTutorial" class="popup" id="popupRandom">
        <div class="popup-inner">
          <p class="popupText">And you can use the random button to find our easteregg.</p>
          <button @click="lastTutorial = false" class="popupButtons">Close</button>
          <button @click="lastTutorial = false" class="popupButtons">Got it!</button>
        </div>
      </div>
    </div>
    <button class="button-container rightPart" id="questionbutton" @click="tutorialStart = true">?</button>
  </div>
  <div id="picture">
    <img v-if="season === 1 && sunPower === 0" class="mainPicture" src="/Simulation_01_Spring_100.png"/>
    <img v-else-if="season === 1 && sunPower === 25" class="mainPicture" src="/Simulation_01_Spring_75.png"/>
    <img v-else-if="season === 1 && sunPower === 50" class="mainPicture" src="/Simulation_01_Spring_50.png"/>
    <img v-else-if="season === 1 && sunPower === 75" class="mainPicture" src="/Simulation_01_Spring_25.png"/>
    <img v-else-if="season === 1 && sunPower === 100" class="mainPicture" src="/Simulation_01_Spring_00.png"/>
    <img v-if="season === 2 && sunPower === 0" class="mainPicture" src="/Simulation_02_Summer_100.png"/>
    <img v-else-if="season === 2 && sunPower === 25" class="mainPicture" src="/Simulation_02_Summer_75.png"/>
    <img v-else-if="season === 2 && sunPower === 50" class="mainPicture" src="/Simulation_02_Summer_50.png"/>
    <img v-else-if="season === 2 && sunPower === 75" class="mainPicture" src="/Simulation_02_Summer_25.png"/>
    <img v-else-if="season === 2 && sunPower === 100" class="mainPicture" src="/Simulation_02_Summer_00.png"/>
    <img v-if="season === 3 && sunPower === 0" class="mainPicture" src="/Simulation_03_Autumn_100.png"/>
    <img v-else-if="season === 3 && sunPower === 25" class="mainPicture" src="/Simulation_03_Autumn_75.png"/>
    <img v-else-if="season === 3 && sunPower === 50" class="mainPicture" src="/Simulation_03_Autumn_50.png"/>
    <img v-else-if="season === 3 && sunPower === 75" class="mainPicture" src="/Simulation_03_Autumn_25.png"/>
    <img v-else-if="season === 3 && sunPower === 100" class="mainPicture" src="/Simulation_03_Autumn_00.png"/>
    <img v-if="season === 4 && sunPower === 0" class="mainPicture" src="/Simulation_04_Winter_100.png"/>
    <img v-else-if="season === 4 && sunPower === 25" class="mainPicture" src="/Simulation_04_Winter_75.png"/>
    <img v-else-if="season === 4 && sunPower === 50" class="mainPicture" src="/Simulation_04_Winter_50.png"/>
    <img v-else-if="season === 4 && sunPower === 75" class="mainPicture" src="/Simulation_04_Winter_25.png"/>
    <img v-else-if="season === 4 && sunPower === 100" class="mainPicture" src="/Simulation_04_Winter_00.png"/>
  </div>
  <div id="controlPanel" class="inline-flex">
    <div v-if="tutorialStart" class="popup" id="popupControl">
      <div class="popup-inner">
        <p class="popupText">You can use the control panels to change the environmental conditions and to calculate how
          much households
          could be supplied with energy.</p>
        <button @click="tutorialStart = false" class="popupButtons">Close</button>
        <button @click="tutorialStart = false, tutorialNext = true" class="popupButtons">Got it!</button>
      </div>
    </div>
    <div id="solarpanel" class="p-2">
      <img src="../images/icons/solarpanel.png"/>
      <div class="custom-slider">
        <input
            ref="slider"
            :value="amountPanels"
            @input="({ target }) => (amountPanels = parseFloat(target.value))"
            type="range"
            :min="1"
            :max="1000"
            :step="1"
            class="slider"
            @change="calculate"
        />
        <br>
        <input
            :value="amountPanels"
            @input="({ target }) => (amountPanels = parseFloat(target.value))"
            :min="1"
            :max="1000"
            :step="1"
            type="number"
            class="input"
            @change="calculate"
        />
        <h4>{{ panelUnit }}</h4>
        <p>{{ panelInfo }}</p>
      </div>
    </div>
    <div id="powerFeed" class="p-2">
      <img src="../images/icons/energy.png"/>
      <div class="custom-slider">
        <input
            ref="slider"
            :value="powerFeed"
            @input="({ target }) => (powerFeed = parseFloat(target.value))"
            type="range"
            :min="1"
            :max="100"
            :step="1"
            class="slider"
            @change="calculate"
        />
        <br>
        <input
            :value="powerFeed"
            @input="({ target }) => (powerFeed = parseFloat(target.value))"
            :min="1"
            :max="100"
            :step="1"
            type="number"
            class="input"
            @change="calculate"
        />
        <h4>{{ powerUnit }}</h4>
        <p>{{ powerInfo }}</p>
      </div>
    </div>
    <div id="sunPower" class=" p-2">
      <img src="../images/icons/sun.png"/>
      <div class="custom-slider">
        <input
            ref="slider"
            :value="sunPower"
            @input="({ target }) => (sunPower = parseFloat(target.value))"
            type="range"
            :min="0"
            :max="100"
            :step="25"
            class="slider"
            @change="calculate"
        />
        <br>
        <input
            :value="sunPower"
            @input="({ target }) => (sunPower = parseFloat(target.value))"
            :min="0"
            :max="100"
            :step="25"
            type="number"
            class="input"
            @change="calculate"
        />
        <h4>{{ sunUnit }}</h4>
        <p>{{ sunInfo }}</p>
      </div>
    </div>
    <div id="seasons" class="p-2">
      <img src="../images/icons/seasons.png"/>
      <div class="custom-slider">
        <input
            ref="slider"
            :value="season"
            @input="({ target }) => (season = parseFloat(target.value))"
            type="range"
            :min="1"
            :max="4"
            :step="1"
            class="slider"
            @change="calculate"
        />
        <br>
        <input
            :value="season"
            @input="({ target }) => (season = parseFloat(target.value))"
            :min="1"
            :max="4"
            :step="1"
            type="number"
            class="input"
            @change="calculate"
        />
        <h4>{{ seasonUnit }}</h4>
        <p>{{ seasonInfo }}</p>
      </div>
    </div>
    <div id="household" class="p-2">
      <img src="../images/icons/household.png"/>
      <p id="textHousehold">How much households could be supplied by one hour operational time?</p>
      <p id="amount">{{ household }}</p>
    </div>
  </div>
</template>

<style scoped>
.mainPicture {
  height: 30rem;
  width: auto;
  margin: auto;
}

img {
  height: 3rem;
  width: auto;
  margin: auto;
}

#controlPanel {
  display: flex;
  justify-content: center;
  margin: 0.5rem auto 4rem auto;
  position: relative;
}

#textHousehold {
  font-size: x-small;
  width: 100px;
  text-align: center;
}

#amount {
  font-size: medium;
  text-align: center;
}

/*css for the popup elements*/
.singleButtonElement {
  position: relative;
}

.popup {
  width: 200px;
  display: flex;
  justify-content: center;
  position: absolute;
}

.popup-inner {
  background-color: lavender;
  border-radius: 12px;
  padding: 6px 6px 2px 6px;
  text-align: center;
}

#questionbutton {
  color: white;
  width: 49px;
  padding: 4px 8px;
}

.questionbutton:hover {
  scale: 1.05;
  background-color: #2b4642;
  color: #EEEAE0;
}

.popupButtons {
  background-color: darkslategray;
  color: white;
  border-radius: 12px;
  padding: 4px 8px;
  margin: 1rem;
}

#popupControl {
  top: -240px;
}

#popupLive {
  top: 60px;
}

#popupRandom {
  top: 60px;
}

.popupText {
  font-size: medium;
}

.button-container {
  background-color: #416662;
  border-radius: 8px;
  height: 49px;
  color: #ffffff;
  padding: 6px 12px;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, transform 0.01s ease-in-out;
  margin-top: 5px;
  margin-bottom: 5px;
}

.button-container:hover {
  scale: 1.05;
  background-color: #2b4642;
  color: #ffffff;
}


/*css for sliders*/
.custom-slider {
  --trackHeight: 0.5rem;
  --thumbRadius: 1rem;
}

/* style the input element with type "range" */
.custom-slider input[type="range"] {
  position: relative;
  appearance: none;
  /* pointer-events: none; */
  border-radius: 999px;
  z-index: 0;
}

/* ::before element to replace the slider track */
.custom-slider input[type="range"]::before {
  content: "";
  position: absolute;
  width: auto;
  height: 100%;
  background: #00865a;
  /* z-index: -1; */
  pointer-events: none;
  border-radius: 999px;
}

/* `::-webkit-slider-runnable-track` targets the track (background) of a range slider in chrome and safari browsers. */
.custom-slider input[type="range"]::-webkit-slider-runnable-track {
  appearance: none;
  background: #005a3c;
  height: var(--trackHeight);
  border-radius: 999px;
}

/* `::-moz-range-track` targets the track (background) of a range slider in Mozilla Firefox. */
.custom-slider input[type="range"]::-moz-range-track {
  appearance: none;
  background: #005a3c;
  height: var(--trackHeight);
  border-radius: 999px;
}

.custom-slider input[type="range"]::-webkit-slider-thumb {
  position: relative;
  top: 50%;
  transform: translate(0, -50%);
  width: var(--thumbRadius);
  height: var(--thumbRadius);
  /* margin-top: calc((var(--trackHeight) - var(--thumbRadius)) / 2); */
  background: #00bd7e;
  border-radius: 999px;
  pointer-events: all;
  appearance: none;
  z-index: 1;
}

p {
  font-size: xx-small;
}

.leftPart {
  justify-content: flex-start;
  /* margin-left: 5px; */
  margin-right: auto;
}

.rightPart {
  justify-content: flex-end;
  margin-left: 10px;
}

.topBar {
  display: flex;
}
</style>
