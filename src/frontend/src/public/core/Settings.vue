<template>
  <div class="wrap">
    <h1>Settings</h1>
    <!--    censys-->
    <h2>Censys</h2>
    <div class="search">
      <p>Censys.io</p>
        <span class="con">
            <input type="text" name="search" placeholder="censys ...">
        </span>
    </div>
    <div class="search">
      <p>Censys.io</p>
      <span class="con">
            <input type="text" name="search" placeholder="censys ...">
        </span>
    </div>
    <!--    shodan -->
    <h2>Shodan</h2>
    <div class="search">
      <p>Shodan.io</p>
      <span class="con">
            <input type="text" name="search" placeholder="shodan ...">
        </span>
    </div>
    <div class="search">
      <p>Shodan.io</p>
      <span class="con">
            <input type="text" name="search" placeholder="shodan ...">
        </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Settings'
}
</script>