<template>
  <nav class="menu-main active">
    <ul>
      <li>
        <router-link to="/home" active-classes="active" class="nav-link">Home</router-link>
        <div class="menu-ico"><i class="fas fa-heart"></i></div>
      </li>
      <li>
        <router-link to="/sources" active-classes="active" class="nav-link">Sources</router-link>
        <div class="menu-ico"><i class="fas fa-table"></i></div>
      </li>
      <li>
        <router-link to="/products" active-classes="active" class="nav-link">Products</router-link>
        <div class="menu-ico"><i class="fas fa-laptop-code"></i></div>
      </li>
      <li>
        <router-link to="/search" active-classes="active" class="nav-link">Search</router-link>
        <div class="menu-ico"><i class="fas fa-search"></i></div>
      </li>
      <li>
        <router-link to="/people" active-classes="active" class="nav-link">Search</router-link>
        <div class="menu-ico"><i class="fas fa-user"></i></div>
      </li>
      <li>
        <router-link to="/technologies" active-classes="active" class="nav-link">Technologies</router-link>
        <div class="menu-ico"><i class="fas fa-digital-tachograph"></i></div>
      </li>
      <li>
        <router-link to="/tools" active-classes="active" class="nav-link">Tools</router-link>
        <div class="menu-ico"><i class="fas fa-tools"></i></div>
      </li>
      <li>
        <router-link to="/vendors" active-classes="active" class="nav-link">Vendors</router-link>
        <div class="menu-ico"><i class="fas fa-building"></i></div>
      </li>
      <li>
        <router-link to="/cves" active-classes="active" class="nav-link">CVEs</router-link>
        <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
      </li>
      <li>
        <router-link to="/cwes" active-classes="active" class="nav-link">CWEs</router-link>
        <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
      </li>
      <li>
        <router-link to="/cwes-top-25" active-classes="active" class="nav-link">Top CWEs</router-link>
        <div class="menu-ico"><i class="fas fa-fire-alt"></i></div>
      </li>
      <li>
        <router-link to="/cheat-sheets" active-classes="active" class="nav-link">Cheat Sheet</router-link>
        <div class="menu-ico"><i class="far fa-file-alt"></i></div>
      </li>
    </ul>
    <button class="menu-main active"><i class="fas fa-arrow-left menu-main"></i></button>
  </nav>
</template>

<script>
import {useRouter} from 'vue-router';
import {useStore} from 'vuex';

export default {
  name: 'Menu',
  setup() {
    const router = useRouter();
    const store = useStore();
  }
}
</script>

<style scoped>
body {
  font-size: .875rem;
}

.feather {
  width: 16px;
  height: 16px;
  vertical-align: text-bottom;
}

/*
 * Sidebar
 */

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100; /* Behind the navbar */
  padding: 48px 0 0; /* Height of navbar */
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 5rem;
  }
}

.sidebar-sticky {
  position: relative;
  top: 0;
  height: calc(100vh - 48px);
  padding-top: .5rem;
  overflow-x: hidden;
  overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
}

@supports ((position: -webkit-sticky) or (position: sticky)) {
  .sidebar-sticky {
    position: -webkit-sticky;
    position: sticky;
  }
}

.sidebar .nav-link {
  font-weight: 500;
  color: #333;
}

.sidebar .nav-link .feather {
  margin-right: 4px;
  color: #999;
}

.sidebar .nav-link.active {
  color: #007bff;
}

.sidebar .nav-link:hover .feather,
.sidebar .nav-link.active .feather {
  color: inherit;
}

.sidebar-heading {
  font-size: .75rem;
  text-transform: uppercase;
}

/*
 * Navbar
 */

.navbar-brand {
  padding-top: .75rem;
  padding-bottom: .75rem;
  font-size: 1rem;
  background-color: rgba(0, 0, 0, .25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar .navbar-toggler {
  top: .25rem;
  right: 1rem;
}

.navbar .form-control {
  padding: .75rem 1rem;
  border-width: 0;
  border-radius: 0;
}

.form-control-dark {
  color: #fff;
  background-color: rgba(255, 255, 255, .1);
  border-color: rgba(255, 255, 255, .1);
}

.form-control-dark:focus {
  border-color: transparent;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, .25);
}
</style>

