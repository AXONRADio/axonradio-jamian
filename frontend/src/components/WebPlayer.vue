<template lang="html">
<div v-on:keyup="pressKeys">
<v-container grid-list-md ml-4 mt-2>
  <v-layout d-flex row wrap>
      <h2>{{song_name}}</h2>
  </v-layout>
  <v-layout mt-2>
      <h3>{{radios}}</h3>
  </v-layout>
  <v-layout mt-3 mb-3>
      <v-divider></v-divider>
  </v-layout>
  <v-layout d-flex row wrap>

      <v-flex xs12 sm12 md9 lg8 mr-4>
       <youtube :video-id="vid_id" ref="youtube"
             @ended="getVideo()" player-width="100%"
             player-height="100%" :player-vars="{autoplay:1}"></youtube>
      </v-flex>

      <v-layout column>

        <v-layout>
          <!-- <v-jumbotron color="primary">  </v-jumbotron> -->
          <v-flex xs6 sm6 md6 lg4 offset-xs2 offset-sm2 offset-md0>
            <v-radio-group v-model="radios" :mandatory="false">
            <v-radio label="Jazz" value="jazz" color="primary"></v-radio>
            <v-radio label="Rock" value="rock" color="primary"></v-radio>
            <v-radio label="Blues" value="blues" color="primary"></v-radio>
            <v-radio label="Pop" value="pop" color="primary"></v-radio>
            <v-radio label="Reggae" value="reggae" color="primary"></v-radio>
            </v-radio-group>
          </v-flex>
          <v-flex xs8 sm8 md7 lg4>
            <v-radio-group v-model="radios" :mandatory="false">
            <v-radio label="Hiphop" value="hiphop" color="primary"></v-radio>
            <v-radio label="Disco/techno/electronic" value="disco" color="primary"></v-radio>
            <v-radio label="Country" value="country" color="primary"></v-radio>
            <v-radio label="Classical" value="classical" color="primary"></v-radio>
            <v-radio label="Metal" value="metal" color="primary"></v-radio>
            </v-radio-group>
          </v-flex>

        </v-layout>

        <v-layout d-flex column >
          <v-flex>
            <v-flex md4 offset-xs3 offset-sm3 offset-md2 offset-lg1>
              <v-btn @click="upvote()" :disabled="votedup == 1" flat color="deep-orange">
                upvote<v-icon right>keyboard_arrow_up</v-icon>
              </v-btn>
            </v-flex>
            <v-flex md4 offset-xs3 offset-sm3 offset-md2 offset-lg1>
              <v-btn @click="getVideo()" @keyup.enter="getVideo" flat >New song!
                <v-icon color="primary" right>skip_next</v-icon>
              </v-btn>
            </v-flex>
            <v-flex md4 offset-xs3 offset-sm3 offset-md2 offset-lg1>
              <v-btn @click="downvote()" :disabled="voteddn == 1" flat color="light-blue">
                downvote<v-icon>keyboard_arrow_down</v-icon>
              </v-btn>
            </v-flex>
          </v-flex>
        </v-layout>
       </v-layout>
   </v-layout>
   <v-layout d-flex row wrap mt-4>
    <v-flex xs12 sm8 md12 lg10>
        <bar-chart v-if="loadedBar" :chart-data="this.mean"></bar-chart>
    </v-flex>
   </v-layout>
</v-container>
</div>
</template>

<script>
import axios from 'axios'
import BarChart from '@/components/BarChart.js'
import LineChart from '@/components/LineChart.js'

export default {
  name: 'WebPlayer',
  components: {
    BarChart,
    LineChart,

  },
  data(){
    return{
      image: 'http://i0.kym-cdn.com/entries/icons/original/000/003/231/dancing-spiderman.gif',
      radios: 'classical',
      song_name: '',
      vid_id: '',
      mean: {},
      loadedBar: false,
      songID: '',
      score: '',
      votedup: false,
      voteddn: false,
    }
  },
  // watch() {
  //   db_data: {
  //     this.getDbData()
  //   }
  // },
  mounted(){
    this.getVideo()
  },

  methods: {
    resetBar(){
      this.loadedBar = false
    },
    resetVotes(){
      this.votedup = false
      this.voteddn = false
    },
    upvote(){
        if(this.votedup == false){
            axios.post('http://167.99.98.179:5000/api/upvote/?genre='
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
            axios.post('http://167.99.98.179:5000/api/downvote/?genre='
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
    pressKeys: function(e){
      if(e.keyCode === 32){
        this.getVideo()
      }
      if(e.keyCode === 65){
        this.upvote()
      }
      if(e.keyCode === 90){
        this.downvote()
      }
    },
    getVideo(){
      this.resetBar()
      this.resetVotes()
      axios.get('http://167.99.98.179:5000/api/video/?genre=' + this.radios)
      .then(response => {
        this.song_name = response.data.name
        this.vid_id = response.data.vidID
        this.mean = response.data.mean
        this.songID = response.data.id
        this.score = response.data.score
        this.loadedBar = true
        console.log(response.data.name)
        console.log(response.data.score)
      })
      .catch(error => {
        console.log(error)
      })
    },
    //https://axonradio-183303.appspot.com

    playVideo() {
      this.player.playVideo()
    }
  },
  computed: {
    player () {
      return this.$refs.youtube.player
    }
  },

}

</script>

<style lang="css">

</style>
