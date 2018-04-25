<template lang="html">


  <div>
  <v-container grid-list-md>

    <v-layout d-flex row wrap>
      <v-flex xs12 sm8 md8>
        <h2>Now playing: {{song_name}}</h2>
        <h3>genre: {{this.radios}}</h3>
      </v-flex>
      <v-flex md2>
        <img src="http://i0.kym-cdn.com/entries/icons/original/000/003/231/dancing-spiderman.gif">
      </v-flex>
    <v-divider></v-divider>
    </v-layout>

    <v-layout d-flex row wrap>

    <v-layout  d-flex column>

      <v-flex md4>
        <youtube :video-id="vid_id" ref="youtube"
             @ended="getVideo()" player-width="100%"
             player-height="100%" :player-vars="{autoplay:1}"></youtube>
      </v-flex>
    </v-layout>
    <v-layout d-flex row wrap>


      <v-flex xs12 sm8 md6 offset-md0>
        <v-radio-group v-model="radios" :mandatory="false">
        <v-radio label="Jazz" value="jazz"></v-radio>
        <v-radio label="Rock" value="rock"></v-radio>
        <v-radio label="Blues" value="blues"></v-radio>
        <v-radio label="Pop" value="pop"></v-radio>
        <v-radio label="Reggae" value="reggae"></v-radio>
      </v-radio-group>
    </v-flex>
    <v-flex xs12 sm8 md6>
      <v-radio-group v-model="radios" :mandatory="false">
        <v-radio label="Hiphop" value="hiphop"></v-radio>
        <v-radio label="Disco" value="disco"></v-radio>
        <v-radio label="Country" value="country"></v-radio>
        <v-radio label="Classical" value="classical"></v-radio>
        <v-radio label="Metal" value="metal"></v-radio>
      </v-radio-group>
    </v-flex>
    </v-layout>


    <v-layout column>
      <v-flex>
        <v-btn @click="upvote()" :disabled="votedup == 1" flat icon color="deep-orange">
          <v-icon>thumb_up</v-icon>
        </v-btn>
      </v-flex>
      <v-flex>
        <v-btn @click="getVideo()" flat icon large>
          <v-icon>play_circle_filled</v-icon>
        </v-btn>
      </v-flex>
      <v-flex>
       <v-btn @click="downvote()" :disabled="voteddn == 1" flat icon color="light-blue">
         <v-icon>thumb_down</v-icon>
       </v-btn>
     </v-flex>
    </v-layout>

    <v-layout d-flex row wrap align-center>
    <v-flex xs12 sm6 md4>
        <bar-chart v-if="loaded" :chart-data="this.mean"></bar-chart>
    </v-flex>

    <v-flex xs12 sm6 md4 offset-md3>
      <doughnut-chart v-if="loaded" :chart-data="this.db_data"></doughnut-chart>
      <p class='text-sm-center'>Distribution of songs in db</p>
    </v-flex>
  </v-layout>

  </v-layout>

  </v-container>

  </div>

</template>

<script>
import axios from 'axios'
import BarChart from '@/components/BarChart.js'
import LineChart from '@/components/LineChart.js'
import DoughnutChart from '@/components/DoughnutChart.js'
export default {
  name: 'app',
  components: {
    BarChart,
    LineChart,
    DoughnutChart
  },
  data(){
    return{
      radios: 'jazz',
      song_name: '',
      vid_id: '',
      mean: {},
      loaded: false,
      songID: '',
      score: '',
      votedup: false,
      voteddn: false,
      db_data: {}
    }
  },
  mounted(){
    this.getVideo()
    this.getDbData()
    this.votedup = false
  },
  methods: {
    resetState(){
      this.loaded = false
      this.votedup = false
      this.voteddn = false
    },
    upvote(){
        if(this.votedup == false){
            axios.post('http://localhost:5000/api/upvote/?genre='
                    + this.radios + '&songID=' + this.songID)
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              console.log(error)
            })
            this.votedup = true
            this.voteddn = false
        }
    },
    downvote(){
        if(this.voteddn == false){
            axios.post('http://localhost:5000/api/downvote/?genre='
                       + this.radios + '&songID=' + this.songID)
            .then(response => {
              console.log(response.data)
            })
            .catch(error => {
              console.log(error)
            })
            this.voteddn = true
            this.votedup = false
        }
    },
    getVideo(){
      this.resetState()
      axios.get('http://localhost:5000/api/video/' + this.radios + '/')
      .then(response => {
        this.song_name = response.data.name
        this.vid_id = response.data.vidID
        this.mean = response.data.mean
        this.songID = response.data.id
        this.score = response.data.score
        this.loaded = true
        console.log(response.data.name)
        console.log(response.data.score)
      })
      .catch(error => {
        console.log(error)
      })
    },
    //https://axonradio-183303.appspot.com
    getDbData(){
      this.resetState()
      axios.get('http://localhost:5000/api/data/')
      .then(response => {
        this.db_data = response.data
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      });
      this.loaded=true
    },
    playVideo() {
      this.player.playVideo()
    }
},
  computed: {
    player () {
      return this.$refs.youtube.player
    }
  },
  ready: function() {
    this.getDbData()

    setInterval(function(){
      this.getDbData()
    }.bind(this), 30)
  }
}

</script>

<style lang="css">

</style>
