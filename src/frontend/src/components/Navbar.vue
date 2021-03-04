<template>
  <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-md-3 col-lg-2 mr-0 px-3" href="#">SARENKA</a>
  <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-toggle="collapse" data-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
  <ul class="navbar-nav px-3">
    <li class="nav-item text-nowrap">
      <router-link to="/settings" class="p-2 text-white">Settings</router-link>
    </li>
  </ul>
</nav>
</template>

<script>
import {useRouter} from 'vue-router';
import { useStore } from 'vuex';
export default {
    name: "Navbar",
    
    setup(){
      const router = useRouter();
      const store = useStore();

    
    }
}
</script>