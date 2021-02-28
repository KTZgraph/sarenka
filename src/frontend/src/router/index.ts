import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Public from '@/public/Public.vue';
//vulnerabilities
import CVEs from '@/public/vulnerabilities/CVEs.vue';
import CWEs from '@/public/vulnerabilities/CWEs.vue';
import CWEsTop25 from '@/public/vulnerabilities/CWEsTop25.vue';
// core
import Settings from '@/public/core/Settings.vue';
import Sources from '@/public/core/Sources.vue';
// products
import Products from '@/public/products/Products.vue';
// search
import Search from '@/public/search/Search.vue';
//technologies
import Technologies from '@/public/technologies/Technologies.vue';
//tools
import Tools from '@/public/tools/Tools.vue';
//cheet_sheets
import CheatSheets from '@/public/cheat_sheets/CheatSheets.vue';
//vendors
import Vendors from '@/public/vendors/Vendors.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    name: 'Public',
    component: Public,
    children: [
      // {path: '/', redirect: '/sources'},
      {path: '/sources', component: Sources},
      {path: '/cves', component: CVEs},
      {path: '/cwes', component: CWEs},
      {path: '/cwes-top-25', component: CWEsTop25},
      {path: '/settings', component: Settings},
      {path: '/products', component: Products},
      {path: '/search', component: Search},
      {path: '/technologies', component: Technologies},
      {path: '/tools', component: Tools},
      {path: '/cheat-sheets', component: CheatSheets},
      {path: '/vendors', component: Vendors},
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
