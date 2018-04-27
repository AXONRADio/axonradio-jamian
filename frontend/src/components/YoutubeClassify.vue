<template lang="html">
  <v-container grid-list-md>
     <v-layout>
       <v-text-field v-model="url"
       placeholder="Paste your youtube link here only accepts songs between 1 and 8 minutes long"
       multi-line>
     </v-text-field>
     </v-layout>
     <v-layout>
       <youtube :video-id="vid_id" ref="youtube"
            @ended="getVideo()" player-width="100%"
            player-height="100%" :player-vars="{autoplay:1}"></youtube>
     </v-layout>
     <v-layout>
       <v-btn @click="prediction()">Predict your song!</v-btn>
       <p>{{url}}</p>
       <p>{{vid_id}}</p>
     </v-layout>
     <v-layout>
         <bar-chart v-if="loadedBar" :chart-data="this.mean"></bar-chart>
     </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'
import BarChart from '@/components/BarChart.js'
export default{
  components:{
    BarChart
  },
  data(){
    return{
      url: '',
      vid_id: '',
      loadedBar: false,
      mean: {},
      song_name: ''
    }
  },
  methods:{
      resetState: function(){
        this.loadedBar = false
      },
      prediction: function(){
          this.resetState()
          this.youTubeGetID()
          axios.post('http://localhost:5000/api/predict?vid_id=' + this.vid_id)
          .then(response => {
            this.mean = response.data.mean
            this.song_name = response.data.name
            this.loadedBar = true
              console.log(response.data)
           })
           .catch(error =>{
              console.log(error)
           })
       },
       youTubeGetID: function(){
         this.url = this.url.split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/);
         this.vid_id =  (this.url[2] !== undefined) ? this.url[2].split(/[^0-9a-z_\-]/i)[0] : this.url[0];
       }
  },
  computed: {
    //vid_id: this.YouTubeGetID()
  }

}


</script>

<style lang="css">
</style>
