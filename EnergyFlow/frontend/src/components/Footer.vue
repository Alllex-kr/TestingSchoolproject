<template>
  
  <footer class="bg-gray-600 text-white p-8">
    <div class="flex justify-center">

      <!-- Spalte 1 -->
      <div class="flex flex-col text-left">
        <strong>OX2 Corporate</strong>
        <router-link to="/about">About OX2</router-link>
        <router-link to="/projects">Projects</router-link>
        <router-link to="/market">Our market</router-link>
        <router-link to="/strategy">Our strategy</router-link>
        <router-link to="/contact">Contact</router-link>
      </div>
    
      <!-- Spalte 2 -->
      <div class="flex flex-col ml-16 text-left">
        <div style="margin-bottom: 5px;">
          <strong>Head Office Sweden</strong>
          <p >Lilla Nygatan 1, Box 2299</p>
          <p >103 17 Stockholm</p>
        </div>
        <div >
          <small >Phone:</small>
          <p >+46 8 559 310 00</p>
        </div>
        <div >
          <small >Email:</small>
          <p >info@ox2.com</p>
        </div>
        <div>
          <a href="https://www.linkedin.com/company/ox2/" target="_blank" rel="noopener noreferrer" >LinkedIn</a>
        </div>
      </div>
    </div>

    <!-- Trenner -->
    <hr class="my-4 mx-4 border-gray-400">

    <!-- Copyright und Policies -->
    <div class="text-sm"> <!-- Hinzugefügt: text-left -->
      <p>© 2022-2023 OX2 - <router-link to="/cookie-policy">Cookie policy</router-link> - <router-link to="/integrity-policy">Integrity policy</router-link></p>
    </div>
  </footer>
</template>

<style>
footer {
  margin-top: 100px;
  position: bottom;
  left: 0;
  bottom: 0;
  width: 100%;
  text-align: center;
}

@media (hover: hover) {
  a:hover {
    transition: 0.5s ease all;
    color: #00afea;
    border-color: #00afea;
  }
}
</style>
