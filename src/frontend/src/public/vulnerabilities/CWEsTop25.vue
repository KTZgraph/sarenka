<template>
  <div class="wrap">
    <h2>Top 25 Common Weakness Enumeration</h2>
    <div class="table-responsive">
      <table class="table table-striped table-sm">
        <thead>
        <tr>
          <th>#</th>
          <th>CWE-ID</th>
          <th>Name</th>
          <th>Weakness Abstraction</th>
          <th>Status</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="cwe in cwesTop25" :key="cwe.cwe_id">
          <td>{{ cwe.cwe_id }}</td>
          <td>{{ cwe.name }}</td>
          <td>{{ cwe.weakness_abstraction }}</td>
          <td>{{ cwe.status }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import {ref, onMounted} from 'vue';
import axios from 'axios';

export default {
  name: 'CWEsTop25',
  setup() {
    const cwesTop25 = ref([]);

    const load = async () => {
      const response = await axios.get('vulns/cwes');
      cwesTop25.value = response.data.data;
      // console.log("cwesTop25.value", cwesTop25.value);
      console.log("cwesTop25.value", response.data.data);
    };

    onMounted(load);

    return {
      cwesTop25,
      load
    }
  }
}
</script>