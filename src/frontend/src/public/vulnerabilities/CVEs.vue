<template>
  <div class="wrap">
    <h1>CVEs</h1>
  </div>

</template>

<script>
import {ref, onMounted} from 'vue';
import axios from 'axios';

export default {
  name: 'CVEs',
  setup(){
    const cves = ref('');

    const load = async () => {
      const response = await axios.get('cves');
      cves.value = response.data.data;
      console.log("cves.value", cves.value);
    };

    // onMounted(load);

    return {
      load
    }
  }
}
</script>