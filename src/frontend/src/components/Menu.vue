<template>
  <nav class="menu-main" :class="{active: isActive}">
    <ul>
      <!--      menu with logo as icon-->
      <li>
        <router-link to="/swagger" active-classes="active" class="nav-link">Sarenka
          <div class="menu-ico menu-ico-logo"><img src="../assets/logo_crop.png" alt=""></div>
        </router-link>
      </li>
      <li>
        <router-link to="/sources" active-classes="active" class="nav-link">Sources
          <div class="menu-ico"><i class="fas fa-table"></i></div>
        </router-link>
      </li>
      <li>
        <router-link to="/products" active-classes="active" class="nav-link">Products
          <div class="menu-ico"><i class="fas fa-laptop-code"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/search" active-classes="active" class="nav-link">Search
          <div class="menu-ico"><i class="fas fa-search"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/people" active-classes="active" class="nav-link">Search
          <div class="menu-ico"><i class="fas fa-user"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/technologies" active-classes="active" class="nav-link">Technologies
          <div class="menu-ico"><i class="fas fa-digital-tachograph"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/tools" active-classes="active" class="nav-link">Tools
          <div class="menu-ico"><i class="fas fa-tools"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/vendors" active-classes="active" class="nav-link">Vendors
          <div class="menu-ico"><i class="fas fa-building"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/cves" active-classes="active" class="nav-link">CVEs
          <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
        </router-link>

      </li>
      <li>
        <router-link to="/cwes" active-classes="active" class="nav-link">CWEs
          <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
        </router-link>
      </li>
      <li>
        <router-link to="/cwes-top-25" active-classes="active" class="nav-link">Top CWEs
          <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
        </router-link>
      </li>
      <li>
        <router-link to="/cheat-sheets" active-classes="active" class="nav-link">Cheat Sheet
          <div class="menu-ico"><i class="far fa-file-alt"></i></div>
        </router-link>
      </li>
      <li>
        <router-link to="/cheat-sheets" active-classes="active" class="nav-link">Settings
          <div class="menu-ico"><i class="fas fa-cog"></i></div>
        </router-link>
      </li>
      <li>
        <!-- hinde/show menu -->
        <div class="nav-link" @click="activeMenu">
          <div class="menu-ico"><i class="fas fa-arrow-right"></i></div>
        </div>
      </li>
    </ul>
  </nav>
</template>

<script>
import {useRouter} from 'vue-router';
import {useStore} from 'vuex';

export default {
  name: 'Menu',
  data() {
    return {
      isActive: true
    }
  },
  setup() {
    const router = useRouter();
    const store = useStore();
  },
  methods: {
    activeMenu(event) {
      console.log(this.isActive)
      this.isActive = !this.isActive;
    }
  }
}



</script>

