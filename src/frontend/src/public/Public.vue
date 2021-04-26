<template>
    <Navbar />
    <div class="container-fluid">
    <div class="row">
    <Menu />

      <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
        <router-view/><!-- dostępne po dispatch data dla user-->
      </main>
    </div>

  </div>
</template>

<script>
import { useRouter } from 'vue-router';

import Menu from '@/components/Menu';
import Navbar from '@/components/Header';

export default {
  name: 'Public',
  components: {
    Menu,
    Navbar
  },
  setup(){
    const router = useRouter()
  }
  
}
</script>