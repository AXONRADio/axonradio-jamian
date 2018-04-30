<template lang="html">
  <v-container d-flex>
  <v-layout mt-5>
    <v-flex mt-5 xs10 sm8 md8 offset-sm2>
      <h1 class="text-xs-center">Song Database</h1>
      <v-divider></v-divider>
      <doughnut-chart v-if="loadedDough" :chart-data="this.db_data"></doughnut-chart>
      <h2 class="text-xs-center">Total songs in database: {{total}}</h2>
    </v-flex>
  </v-layout>
</v-container>
</template>

<script>
import axios from 'axios'
import DoughnutChart from '@/components/DoughnutChart.js'
export default {
  name: 'Stats',
  components:{
    DoughnutChart
  },
  data(){
    return{
      loadedDough: false,
      db_data: {},
      total: 0,

    }
  },
  mounted(){
    this.getDbData()
  },
  methods:{
    resetDough(){
      this.loadedDough = false
    },
    getDbData(){
      this.resetDough()
      axios.get('http://localhost:5000/api/data/')
      .then(response => {
        this.db_data = response.data.collections
        this.total = response.data.total
        this.loadedDough = true
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      });
    },

  }
}
</script>

<style lang="css">
</style>
