<template>
  <div>
    <div class="grid">
    <v-stage :config="configKonva">
      <v-layer>
        <v-line :config="{
          points: [Math.round(i * padding) + 0.5, 0, Math.round(i * padding) + 0.5, configKonva.height],
          stroke: '#ddd',
          strokeWidth: 1
        }"
        v-for="i in configKonva.width / padding"
        v-bind:key="i" 
        />

        <v-line :config="{
          points: [0, 0, 10, 10],
        }"
        />
        
        

        <v-line :config="{
          points: [0, Math.round(j * padding), configKonva.width, Math.round(j * padding)],
          stroke: '#ddd',
          strokeWidth: 1
        }"
        v-for="j in configKonva.height / padding"
        v-bind:key="j" 
        />

      </v-layer>
    </v-stage>
    </div>
    <div>
      <img 
      :src="logicType.image"
      v-for="logicType in logicTypes"
      v-bind:key="logicType"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      configKonva: {
        width: 1100,
        height: 800,
      },
      logicTypes: [{
        name: "and",
        image: require("@/assets/andGate.svg")
      }],
      padding: 20
    }

  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .grid {
    float: left;
  }
</style>
