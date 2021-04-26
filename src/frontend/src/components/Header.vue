<template>
    <header class="header-main">
      <router-link to="/settings" class="header-url"><i class="fas fa-cog"></i><strong>Settings</strong></router-link>
    </header>
</template>

<script>
import {useRouter} from 'vue-router';
import { useStore } from 'vuex';
export default {
    name: "Header",
    
    setup(){
      const router = useRouter();
      const store = useStore();

    
    }
}
</script>