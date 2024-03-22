<template>
  <div class="sliderAx h-auto">
    <div :class="{ 'hidden': activeSlide !== 1, 'block': activeSlide === 1 }" id="slider-1" class="container mx-auto">
      <div class="bg-cover bg-center h-auto text-[#353839] py-24 px-10 object-fill"
           :style="{ 'background-image': 'url('+ imageUrlBattery +')'}">
        <div class="md:w-1/2">
          <p class="font-bold text-sm uppercase">See how the battery storage works...</p>
          <p class="text-3xl font-bold">lorem ipsum </p>
          <p class="text-2xl mb-10 leading-none">dolor sit amet, consetetur sadipscing elitr, sed diam</p>
          <a href="#"
             class="bg-[#416662] py-4 px-8 text-white font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Learn
            about the battery storage...</a>
        </div>
      </div>
      <br>
    </div>

    <div :class="{ 'hidden': activeSlide !== 2, 'block': activeSlide === 2 }" id="slider-2" class="container mx-auto">
      <div class="bg-cover bg-top h-auto text-[#EEEAE0] py-24 px-10 object-fill"
           :style="{ 'background-image': 'url(' + imageUrlCarCharging +')' }">
        <p class="font-bold text-sm uppercase">Charging</p>
        <p class="text-3xl font-bold">Lorem ipsum</p>
        <p class="text-2xl mb-10 leading-none">dolor sit amet, consetetur sadipscing elitr, sed diam</p>
        <a href="#"
           class="bg-[#41664b] py-4 px-8 text-[#EEEAE0] font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Learn
          about the charging methods...</a>
      </div>
      <br>
    </div>

    <div :class="{ 'hidden': activeSlide !== 3, 'block': activeSlide === 3 }" id="slider-3" class="container mx-auto">
      <div class="bg-cover bg-top h-auto text-white py-24 px-10 object-fill"
           :style="{ 'background-image': 'url(' + imageUrlH2 +')' }">
        <p class="font-bold text-sm uppercase">H2</p>
        <p class="text-3xl font-bold">Lorem ipsum</p>
        <p class="text-2xl mb-10 leading-none">dolor sit amet, consetetur sadipscing elitr, sed diam</p>
        <a href="#"
           class="bg-[#416662] py-4 px-8 text-white font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Find
          out more about H2...</a>
      </div>
      <br>
    </div>

    <div :class="{ 'hidden': activeSlide !== 4, 'block': activeSlide === 4 }" id="slider-4" class="container mx-auto">
      <div class="bg-cover bg-top h-auto text-white py-24 px-10 object-fill"
           :style="{ 'background-image': 'url(' + imageUrlSolarPanel +')' }">
        <p class="font-bold text-sm uppercase">Solar panel</p>
        <p class="text-3xl font-bold">Lorem ipsum</p>
        <p class="text-2xl mb-10 leading-none">dolor sit amet, consetetur sadipscing elitr, sed diam</p>
        <a href="#"
           class="bg-[#416662] py-4 px-8 text-white font-bold uppercase text-xs rounded hover:bg-gray-200 hover:text-gray-800">Learn
          more about solar panels...</a>
      </div>
      <br>
    </div>

    <div class="flex justify-between w-24 mx-auto pb-2">
      <button @click="sliderButton(1)"
              :class="{ 'bg-[#416662]': activeSlide === 1, 'bg-gray-900': activeSlide !== 1 }"
              class="rounded-full w-4 pb-2"></button>
      <button @click="sliderButton(2)"
              :class="{ 'bg-[#416662]': activeSlide === 2, 'bg-gray-900': activeSlide !== 2 }"
              class="rounded-full w-4 p-2"></button>
      <button @click="sliderButton(3)"
              :class="{ 'bg-[#416662]': activeSlide === 3, 'bg-gray-900': activeSlide !== 3 }"
              class="rounded-full w-4 pb-2"></button>
      <button @click="sliderButton(4)"
              :class="{ 'bg-[#416662]': activeSlide === 4, 'bg-gray-900': activeSlide !== 4 }"
              class="rounded-full w-4 p-2"></button>
    </div>
  </div>
</template>

<script>
import Battery from '../images/Battery.jpg';
import CarCharging from '../images/CarCharging.jpg';
import H2 from '../images/H2.jpg';
import SolarPanel from '../images/SolarPanel.jpg';

export default {
  data() {
    return {
      slideSpan: 8000,
      activeSlide: 1,
      slideInterval: null,
      imageUrlBattery: Battery,
      imageUrlCarCharging: CarCharging,
      imageUrlH2: H2,
      imageUrlSolarPanel: SolarPanel
    };
  },
  mounted() {
    this.loopSlider();
  },
  methods: {
    path() {
      return path
    },
    loopSlider() {
      this.slideInterval = setInterval(() => {
        if (this.activeSlide < 4) {
          this.activeSlide++;
        } else {
          this.activeSlide = 1;
        }
      }, 8000);
    },
    reinitLoop() {
      clearInterval(this.slideInterval);
      setTimeout(() => {
        this.loopSlider();
      });
    },
    sliderButton(slideNumber) {
      if (this.activeSlide !== slideNumber) {
        this.activeSlide = slideNumber;
        this.reinitLoop();

      }
    },
  },
};
</script>

<style>
/* Add any additional styles here */
</style>
