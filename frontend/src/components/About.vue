<template lang="html">
   <div id="axon" class="about">
      <v-parallax src="https://media.wired.com/photos/5926e6c5af95806129f50ffd/master/w_1132,c_limit/Cerebellum-multicolor-closeup-11.jpg"
                  height="200">
      <v-layout column align-center justify-center>
        <h1 class="white--text">Welcome to AXONRADio!</h1>
        <h2 class="white--text">A smarter radio station</h2>
      </v-layout>
      </v-parallax>
      <v-parallax  height="2000">

      <v-layout column align-center justify-center>
        <h2>What is it?</h2>
        <p>It's a great way to find new music,
          support and find musicians around the world,
          pretend you're an american idol judge, and help
          researchers classify music!</p>
      </v-layout>

      <v-layout column align-center justify-center>
        <h2>How does it work?</h2>
        <p>We use an algorithm to search for random
          youtube music links then we feed them into
          a neural net which can predict genres. You
          tell us what genre you want to listen to
          and we'll give you back a bunch of songs! The
          graphs below each song show the confidence the
          neural net had in its classifications</p>
      </v-layout>
      <v-parallax height="300" src="https://cdn5.f-cdn.com/contestentries/1183465/2462734/5a1121aa3897e_thumb900.jpg"></v-parallax>
      <v-layout column align-center justify-center>
         <h2>Can I test the classifier on songs I choose?</h2>
         <p>Yes, you can! Just use the genre predictor.
         Paste a link in the genre predictor and it will tell you
         what genre it thinks it is!</p>
      </v-layout>
      <v-layout id="axon" column align-center justify-center>
        <h2>How many songs are there to listen to?</h2>
        <p>The database is always getting bigger! Check the Stats
        page to see the current total number of songs and a breakdown
        of individual genres.</p>
      </v-layout>

      <v-parallax height="300" src="https://media.wired.com/photos/5926e6c6cefba457b079b836/master/w_1132,c_limit/Motor-and-Parietal-cortex1.jpg">  </v-parallax>
      <v-layout column align-center justify-center>
        <h2>Why did I get a video that has nothing to do with music?</h2>
        <p>Due to the nature of how AXONRADio works you will sometimes
        get very random videos that do not seem to relate to the genre you
        are listening too or even music at all. This is why there is an
        option to downvote songs. Videos with a low enough score will not be played.
        By upvoting or downvoting songs you help to make the database better for everyone
        listening including yourself!</p>
      </v-layout>

    </v-parallax>
  </div>

</template>

<script>

export default {
  data(){
    return{
      gradient: 'to top,  #7B1FA2, #E1BEE7'
    }
  }
}
</script>

<style lang="css">
p{
 font-size: 20px;
 color: white;
}

.about{
  background-color: black;
}
#axon img{
  width: 100%;
}

</style>
