<template>
  <!--  sprawdzic na tło do fraktali-->
  <!--https://www.lesscake.com/fractals-chaos-game-->
  <div class="wrap settings">
    <h1>Settings</h1>

    <section class="engines">
      <!--    censys-->
      <h2>Censys</h2>
      <div class="credential">
        <p>Censys.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="censys ...">
        </span>
      </div>
      <div class="credential">
        <p>Censys.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="censys ...">
        </span>
      </div>
      <!--    shodan -->
      <h2>Shodan</h2>
      <div class="credential">
        <p>Shodan.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="shodan ...">
        </span>
      </div>
      <div class="credential">
        <p>Shodan.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="shodan ...">
        </span>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Settings'
}
</script>