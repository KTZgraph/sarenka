<template>
  <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <router-link to="/" class="navbar-brand col-md-3 col-lg-2 mr-0 px-3">SARENKA</router-link>
    <nav class="my-2 my-md-0 mr-md-3">
      <!-- user? - rozwiazuje problem jak za pierwszym razem user jest nullem in nie ma zadnych atrybutow -->
      <router-link to="/settings" class="p-2 text-white">Settings</router-link>
    </nav>
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