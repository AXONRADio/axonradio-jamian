<template lang="html">
  <v-container grid-list-md ml-4 mt-2>
     <v-layout>
     </v-layout>
     <v-layout>
        <h2>Your Song: {{song_name}}</h2>
     </v-layout>
     <v-layout mt-2>
       <h3>Predicted Genre: {{genre}}</h3>
     </v-layout>
     <v-layout mt-3>
       <v-text-field v-model="url" @keyup.enter="prediction()"
       placeholder="Paste your youtube link here"
       >
     </v-text-field>

     </v-layout>
     <v-layout mt-1>
       <v-btn color='primary' flat @click="prediction()" :loading="loading" :disabled="loading">
         Predict your song <v-icon right>fingerprint</v-icon><span slot="loader">Predicting song...</span>
       </v-btn>
     </v-layout>
     <v-layout mt-4 d-flex row wrap>
       <v-flex sm12 md10 lg8>
       <youtube :video-id="vid_id" ref="youtube"
            player-width="100%"
            player-height="100%" :player-vars="{autoplay:1}"></youtube>
       </v-flex>
       <v-flex xs10 sm11 md10 lg5>
       <bar-chart v-if="loadedBar" :chart-data="this.mean"></bar-chart>
       </v-flex>
     </v-layout>
     <v-layout>
     </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
import BarChart from '@/components/BarChart.js'
import VueButtonSpinner from 'vue-button-spinner'
export default{
  name: 'YoutubeClassify',
  components:{
    BarChart,
    VueButtonSpinner
  },
  data(){
    return{
      loading: false,
      url: '',
      vid_id: '',
      loadedBar: false,
      mean: {},
      song_name: '',
      genre: ''
    }
  },
  methods:{
      resetState: function(){
        this.loadedBar = false
      },
      resetURL: function(){
        this.url = ''
      },
      prediction: function(){
          if (this.url == 0) {
            console.log("No link was entered")
          }
          else{
            this.loading = true
            this.resetState()
            this.youTubeGetID()
            axios.post('http://167.99.98.179:5000/api/predict?vid_id=' + this.vid_id)
            .then(response => {
              this.mean = response.data.mean
              this.song_name = response.data.name
              this.genre = response.data.genre
              this.loadedBar = true
              this.loading = false
              console.log(response.data)
              })
              .catch(error =>{
                this.loading = false
                console.log(error)
              })
              this.resetURL()
            }
       },
       youTubeGetID: function(){
         this.url = this.url.split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/);
         this.vid_id =  (this.url[2] !== undefined) ? this.url[2].split(/[^0-9a-z_\-]/i)[0] : this.url[0];
       }
  }
}
</script>

<style lang="css">
</style>
