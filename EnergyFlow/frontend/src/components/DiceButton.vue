<template>
  <button class="button-container square" @click="rollDice">
    <img :src="imagePath" :alt="altText" class="button-image"/>
  </button>
</template>

<script>
import dices from '../images/Dice.png';

export default {
  data() {
    return {
      imagePath: dices,
      altText: "Dice Button",
    };
  },
  methods: {
    handleClick() {
      console.log('Button clicked');
    },
    handleHover() {
    },

    rollDice() {
      // Generate random values for your simulation
      const newSeason = Math.floor(Math.random() * 4) + 1; // Random seasons 1-4
      const newSunPower = [0, 25, 50, 75, 100][Math.floor(Math.random() * 5)]; // 0, 25, 50, 75, 100
      const newPanelCount = Math.floor(Math.random() * 1000) + 1; // 1 to 1000 panels
      const newPowerFeed = Math.floor(Math.random() * 100) + 1;  //1 to 100%

      // Emit the new values to the parent component
      this.$emit('dice-rolled', {
        season: newSeason,
        sunPower: newSunPower,
        panelCount: newPanelCount,
        powerFeed: newPowerFeed
      });
    },
  }
};
</script>

<style scoped>
.button-image {
  width: auto;
  height: 100%;
  object-fit: contain;
  transform-origin: center;
  transition: transform 0.05s ease-in-out;
}

.button-container:hover .button-image {
  transform: scale(1.05) rotate(7deg);
}

.square {
  width: 49px;
}
</style>
