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
            <input type="text" name="search" placeholder="type api id">
        </span>
        <p>Censys.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="type key">
        </span>
      </div>
      <!--    shodan -->
      <h2>Shodan</h2>
      <div class="credential">
        <p>Shodan.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="type username">
        </span>
        <p>Shodan.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="type api key">
        </span>
      </div>
      <button class="submit">Save</button>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Settings'
}
</script>