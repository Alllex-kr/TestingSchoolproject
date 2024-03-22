<script>
import Footer from './components/Footer.vue';
import AdditionalInfo from "@/components/AdditionalInfo.vue";
import Navigation from './components/Navigation.vue';
import SimulationView from "@/views/SimulationView.vue";

export default {
  name: "App",
  components: {
    SimulationView,
    AdditionalInfo,
    Footer,
    Navigation
  }
}
</script>

<template>
  <div class="app">
    <Navigation/>
  </div>
  <div class="main-content">
    <SimulationView></SimulationView>

    <div>
      <h3><strong>What is energy flow and why is it important?</strong></h3>
      <br>
      <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et
        dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet
        clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet,
        consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea
        takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed
        diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et
        accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum
        dolor sit amet.</p>
      <br>
      <br>
    </div>
    <AdditionalInfo></AdditionalInfo>
  </div>
    <div style="margin-top: 3rem">
      <v-footer>
        <Footer/>
      </v-footer>
    </div>
</template>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Raleway", sans-serif;
  font-weight: 400;
}

h1 {
  text-align: center;
  font-size: x-large;
}

.main-content{
  padding-top: 100px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}



</style>