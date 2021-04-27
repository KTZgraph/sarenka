<template>
  <header class="header-main">
    <router-link to="/documentation" class="header-url">
      <div class="header-logo"><img src="../assets/logo_crop_name.png" alt="sarenka logo"></div>
    </router-link>
    <router-link to="/search" class="header-url">
      <div class="header-search"><input type="text" placeholder="search"></div>
    </router-link>
    <router-link to="/settings" class="header-url"><div class="header-settings"><i class="fas fa-cog"></i>Settings</div></router-link>
  </header>
</template>

<script>
import {useRouter} from 'vue-router';
import {useStore} from 'vuex';

export default {
  name: "Header",

  setup() {
    const router = useRouter();
    const store = useStore();


  }
}
</script>