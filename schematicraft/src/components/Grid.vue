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
        v-bind:key="`vertical${i}`" 
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
        v-bind:key="`horizontal${j}`" 
        />

      </v-layer>

    <v-layer>
      <v-group
        @dragstart="onLogicGateDragged(index)"
        @dragend="onLogicGateDragEnd(index)"
        @dragmove="event => onLogicGateDragMoved(event)"
        v-for="(logicGate, index) in logicGates"
        v-bind:key="`${index}${logicGate.logicType.name}${logicGate.position.x}${logicGate.position.y}`"
        :config="{
          drawBorder: true,
          width: padding * 4,
          height: padding * 3
        }"
      >
        <v-wedge
          :config="{
            radius: 1.5 * padding,
            angle: 180,
            rotation: -90,
            fill: 'black',
            draggable: true,
            x: logicGate.position.x,
            y: logicGate.position.y
          }"
        />

        <v-line
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
          :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [1.5 * padding, 0, 3 * padding, 0],
            stroke: 'black',
            tension: 1
          }"
        />

        <v-line
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
          :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, -padding, -padding, -padding],
            stroke: 'black',
            tension: 1
          }"
        />

        <v-line
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
          :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, padding, -padding, padding],
            stroke: 'black',
            tension: 1
          }"
        />

        <v-line
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 1"
          :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, 0, -padding, 0],
            stroke: 'black',
            tension: 1
          }"
        />




        <v-circle 
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length == 2"
          :config="{
            x: logicGate.position.x - padding,
            y: logicGate.position.y - padding,
            radius: padding / 4,
            fill: 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
          @click="logicGateCircleClicked(index, true, 0)"
        />

        <v-circle 
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
          :config="{
            x: logicGate.position.x - padding,
            y: logicGate.position.y + padding,
            radius: padding / 4,
            fill: 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
          @click="logicGateCircleClicked(index, true, 1)"
        />



        <v-circle 
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged)"
          :config="{
            x: logicGate.position.x + 3 * padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
          class="logic-gate-connector"
          @click="logicGateCircleClicked(index, false)"
        />

        <v-circle 
          v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length == 1"
          :config="{
            x: logicGate.position.x - padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
          class="logic-gate-connector"
          @click="logicGateCircleClicked(index, true, 0)"
        />



      <v-line
          :config="{
            points: calculateLinePath(input, index, inputIndex),
            stroke: 'black'
          }"
          v-if="input !== null"
          v-for="(input, inputIndex) in logicGate.inputs"
          v-bind:key="inputIndex"
        />
      </v-group>

 


      <v-rect
        v-if="snapbox.isShowingSnapBox"
        :config="{
          x: snapbox.position.x,
          y: snapbox.position.y,
          width: 1.5 * padding,
          height: 3 * padding,
          fill: '#FF7B17',
          opacity: 0.6,
          stroke: '#CF6412',
          strokeWidth: 3,
          dash: [20, 2],
        }"
      />


      </v-layer>
    </v-stage>
    </div>
    <div>
      <img 
      :src="logicType.image"
      v-for="logicType in logicTypes"
      v-bind:key="logicType.name"
      @click="addLogicGateToGrid(logicType)"
      class="logic-type"
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
      padding: 20,
      logicGates: [],
      snapbox: {
        isShowingSnapBox: false,
        indexCurrentlyDragged: null,
        position: {x: 0, y: 0}
      },
      connector: {
        connectorIndex: null,
        isInput: null,
        inputIndex: null
      } 
    }
  },
  methods: {
    addLogicGateToGrid(logicType) {
      this.logicGates.push({
        logicType,
        position: {
          x: this.configKonva.width / 2 - (this.padding / 2),
          y: this.configKonva.height / 2 - (this.padding / 2)
        },
        inputs: [null, null],
      });
    },
    onLogicGateDragged(index) {
      this.snapbox.isShowingSnapBox = true;
      this.snapbox.indexCurrentlyDragged = index;
    },
    onLogicGateDragEnd(index) {
      this.snapbox.isShowingSnapBox = false;
      this.logicGates[index].position.x = this.snapbox.position.x;
      this.logicGates[index].position.y = this.mapSnapPosToDragPos(this.snapbox.position.y);
    },
    onLogicGateDragMoved(event) {
      this.snapbox.position.x = Math.round(event.target.x() / this.padding) * this.padding;
      this.snapbox.position.y = this.mapWedgePosToSnapBox(Math.round((event.target.y() + this.padding / 2) / this.padding) * this.padding) - (this.padding / 2);
    },
    mapWedgePosToSnapBox(positionY) {
      return positionY - (this.padding * 1.5);
    },
    mapSnapPosToDragPos(positionY) {
      return positionY + (this.padding * 1.5);
    },
    logicGateCircleClicked(index, isInput, currentInputIndex) {
      if (this.connector.connectorIndex !== null) {
        // Cannot connect input to input
        if ((this.connector.isInput && isInput) || (!this.connector.isInput && !isInput)) {
          return;
        }

        const logicGateInputIndex = this.connector.isInput ? this.connector.connectorIndex : index;
        const logicGateOutputIndex = this.connector.isInput ? index : this.connector.connectorIndex;
        const inputIndex = this.connector.inputIndex ? this.connector.inputIndex : currentInputIndex;
        this.$set(this.logicGates[logicGateInputIndex].inputs, inputIndex, logicGateOutputIndex);
        console.log(this.logicGates[logicGateInputIndex].inputs);
        this.connector.connectorIndex = null;
        this.connector.isInput = null;
        this.connector.inputIndex = null;
      } else {
        this.connector.connectorIndex = index;
        this.connector.isInput = isInput;
        this.connector.inputIndex = currentInputIndex;
      }
    },
    calculateLinePath(logicGateOutput, logicGateIndex, logicGateInputIndex) {
      const startingPosition = this.logicGates[logicGateOutput].position;
      const endingPosition = this.logicGates[logicGateIndex].position;
      console.log("Need to go from", startingPosition, "to: ", endingPosition);
      let endPositionSkewY;

      console.log(logicGateInputIndex);
      if (this.logicGates[logicGateIndex].inputs.length === 1) {
         endPositionSkewY = 0;
      }
      else if (logicGateInputIndex === 0) {
        endPositionSkewY = -this.padding;
      }
      else {
        endPositionSkewY = this.padding;
      }

      if (startingPosition.x === endingPosition.x || startingPosition.y === endingPosition.y) {
        return [startingPosition.x + 3 * this.padding, startingPosition.y, endingPosition.x - this.padding, endingPosition.y + endPositionSkewY];
      } 

      else {
        let yeet = [startingPosition.x + 3 * this.padding, startingPosition.y, endingPosition.x - this.padding, startingPosition.y, endingPosition.x - this.padding, endingPosition.y + endPositionSkewY];
        console.log(yeet);
        return yeet;
      }
      
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .grid {
    float: left;
  }

  .logic-type {
    cursor: pointer;
  }

  .logic-gate-connector {
    cursor: pointer;
  }
</style>
