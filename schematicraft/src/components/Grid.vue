<template>
  <div>
    <v-stage :config="configKonva">
      <v-layer>
        <v-line :config="{
          points: [Math.round(i * padding) + 0.5, 0, Math.round(i * padding) + 0.5, configKonva.height],
          stroke: '#ddd',
          strokeWidth: 1
        }"
        v-for="i in configKonva.height / padding"
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
</template>

<script>
export default {
  data() {
    return {
      configKonva: {
        width: 500,
        height: 500,
      },
      configCircle: {
        x: 100,
        y: 100,
        radius: 70,
        fill: "red",
        stroke: "black",
        strokeWidth: 4
      },
      padding: 20
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
