<template lang="html">
  <div>
    <v-layout align-center justify-center mt-4>
      <h1>Top songs by genre!</h1>
    </v-layout>
    <v-layout mt-3>
        <v-divider></v-divider>
    </v-layout>
    <v-layout mt-5>
      <v-flex offset-xs2 offset-sm1 offset-md1 offset-lg1 sm8 md6 lg4 xl1>
        <v-btn block @click="setVidId(jazzid)" class="red lighten-2" light>Jazz: {{jazz.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(rockid)" color="red lighten-1" light>Rock: {{rock.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(bluesid)" color="pink lighten-3" light>Blues: {{blues.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(popid)" color="pink lighten-2" light>Pop: {{pop.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(reggaeid)" color="purple lighten-3" light>Reggae: {{reggae.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(hiphopid)" color="purple lighten-2" light>HipHop: {{hiphop.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(discoid)" color="deep-purple lighten-3" light>Disco: {{disco.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(countryid)" color="deep-purple lighten-2" light>Country: {{country.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(classicalid)" color="indigo lighten-3" light>Classical: {{classical.slice(0,40)}}</v-btn>
        <v-btn block @click="setVidId(metalid)" color="indigo lighten-2" light>Metal: {{metal.slice(0,40)}}</v-btn>
      </v-flex>
      <v-flex md6 ml-5 mr-5>
        <youtube :video-id="vid_id" ref="youtube"
           @ended="getVideo()"  :player-vars="{autoplay:1}"></youtube>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'topSongs',
  data(){
    return{
      jazz: '',
      jazzid: '',
      rock: '',
      rockid: '',
      blues: '',
      bluesid: '',
      pop: '',
      popid: '',
      reggae: '',
      reggaeid: '',
      hiphop: '',
      hiphopid: '',
      disco: '',
      discoid: '',
      country: '',
      countryid: '',
      classical: '',
      classicalid: '',
      metal: '',
      metalid: '',
      vid_id: '',
    }
  },
  mounted(){
    this.getTopData()
  },
  methods:{
    getTopData(){
      axios.get('http://localhost:5000/api/top/')
      .then(response => {
        this.jazz = response.data.jazz.name
        this.jazzid = response.data.jazz.vidID
        this.rock = response.data.rock.name
        this.rockid = response.data.rock.vidID
        this.blues = response.data.blues.name
        this.bluesid = response.data.blues.vidID
        this.pop = response.data.pop.name
        this.popid = response.data.pop.vidID
        this.reggae = response.data.reggae.name
        this.reggaeid = response.data.reggae.vidID
        this.hiphop = response.data.hiphop.name
        this.hiphopid = response.data.hiphop.vidID
        this.disco = response.data.disco.name
        this.discoid = response.data.disco.vidID
        this.country = response.data.country.name
        this.countryid = response.data.country.vidID
        this.classical = response.data.classical.name
        this.classicalid = response.data.classical.vidID
        this.metal = response.data.metal.name
        this.metalid = response.data.metal.vidID
        console.log(response.data.jazz.vidID)
      })
    },
    setVidId: function(e){
        this.vid_id = e
    }
  }
}
</script>

<style lang="css">
</style>
