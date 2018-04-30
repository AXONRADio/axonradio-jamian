<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer
      clipped
      fixed
      v-model="drawer"
      app
    >
      <v-list>

        <v-list-tile to='/'>
          <v-list-tile-action>
            <v-icon>radio</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Radio</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile to='/youtubeClassify'>
          <v-list-tile-action>
            <v-icon>fingerprint</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Genre Predictor</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to='/topSongs'>
          <v-list-tile-action>
            <v-icon>star</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Top Songs</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to='/stats'>
          <v-list-tile-action>
            <v-icon>assessment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Stats</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile to='/about'>
          <v-list-tile-action>
            <v-icon>info</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>About</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>AXONRADio</v-toolbar-title>
    </v-toolbar>

    <v-content>
      <router-view/>
      <!-- router goes here -->
    </v-content>

    <v-footer app fixed>
      <span>&copy; 2018</span>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'bubble_chart',
        title: 'Inspire'
      }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  },
  name: 'App'


}
</script>
