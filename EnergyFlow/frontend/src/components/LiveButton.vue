<template>
  <button class="button-container" @click="handleClick">
    <h>LIVE</h>
    <span class="pulse" />
  </button>
</template>

<script>
export default {
  methods: {
    handleClick() {
      console.log('Button clicked');
    },
    handleHover() {
    }
  }
}
</script>

<style scoped>
.pulse {
  display: inline-block;
  margin-left: 8px;
  width: 12px;
  height: 12px;
  background-color: red;
  border-radius: 50%;
  animation: pulseAnimation 1s infinite;
}

@keyframes pulseAnimation {
  0% {
    transform: scale(0.8);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(0.8);
  }
}
</style>