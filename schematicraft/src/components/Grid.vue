<template>
  <div>
    <div class="grid">
      <v-stage :config="configKonva">
        <v-layer>
          <v-line
            :config="{
          points: [Math.round(i * padding) + 0.5, 0, Math.round(i * padding) + 0.5, configKonva.height],
          stroke: '#ddd',
          strokeWidth: 1
        }"
            v-for="i in configKonva.width / padding"
            v-bind:key="`vertical${i}`"
          />
          <v-line :config="{
          points: [0, 0, 10, 10],
        }" />

          <v-line
            :config="{
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
            <v-wedge :config="{
            radius: 1.5 * padding,
            angle: 180,
            rotation: -90,
            draggable: true,
            stroke: 'black',
            x: logicGate.position.x,
            y: logicGate.position.y
          }" 
          v-if="logicGate.logicType.name === 'AND'"
            @mouseover="showDragCursor"
            @mouseleave="showDefaultCursor"

          />

            <v-line :config="{
              x: logicGate.position.x,
              y: logicGate.position.y,
              points: [0.2 * padding, 0, 0, padding, 1.5 * padding, 0, 0, -padding],
              stroke: 'black',
              closed: true,
              tension: 0.5,
              draggable: true
            }" 
               v-if="logicGate.logicType.name === 'OR'"
          />

          <v-line :config="{
              x: logicGate.position.x,
              y: logicGate.position.y,
              points: [0.2 * padding, 0, 0, padding, 1.5 * padding, 0, 0, -padding],
              stroke: 'black',
              closed: true,
              tension: 0.5,
              draggable: true
            }" 
               v-if="logicGate.logicType.name === 'XOR'"
            @mouseover="showDragCursor"
            @mouseleave="showDefaultCursor"

          />

          <v-line :config="{
              x: logicGate.position.x,
              y: logicGate.position.y,
              points: [-0.4 * padding, -padding, 0 * padding, 0, -0.4 * padding, padding],
              stroke: 'black',
              tension: 0.5,
          }" 
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name === 'XOR'"
          />

            <v-line :config="{
              x: logicGate.position.x,
              y: logicGate.position.y,
              points: [0, padding, 1 * padding, 0, 0, -padding],
              stroke: 'black',
              closed: true,
              draggable: true
            }" 
            v-if="logicGate.logicType.name === 'NOT'"
          />

            <v-circle
              :config="{
            x: logicGate.position.x + (1.3 * padding),
            y: logicGate.position.y,
            radius: padding / 4,
            stroke: 'black',
            strokeWidth: 2
          }"
            v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name === 'NOT'"
            @mouseover="showDragCursor"
            @mouseleave="showDefaultCursor"
          />
 

          

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name !== 'LIGHT' && logicGate.logicType.name !== 'SWITCH'"
              :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [1.5 * padding, 0, 2.5 * padding, 0],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && (logicGate.logicType.name === 'LIGHT' || logicGate.logicType.name === 'SWITCH')"
              :config="{
            x: logicGate.position.x - padding,
            y: logicGate.position.y,
            points: [3 * padding, 0, 3.5 * padding, 0],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name === 'SWITCH'"
              :config="{
                x: logicGate.position.x + padding / 2,
                y: logicGate.position.y,
                points: [0, 0, 0, -2 * padding],
                stroke: 'black',
              }"
            />






            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
              :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, -padding, -(1.5 * padding), -padding],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
              :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, padding, - (1.5 * padding), padding],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 1 && logicGate.logicType.name !== 'LIGHT' && logicGate.logicType.name !== 'SWITCH'"
              :config="{
            x: logicGate.position.x,
            y: logicGate.position.y,
            points: [0, 0, -1.5 * padding, 0],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name === 'LIGHT'"
              :config="{
            x: logicGate.position.x - 0.6 * padding,
            y: logicGate.position.y - 1.1 * padding,
            points: [0, 0, padding * 2.1, padding * 2.1],
            stroke: 'black',
          }"
            />

            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name === 'LIGHT'"
              :config="{
            x: logicGate.position.x + 1.6 * padding,
            y: logicGate.position.y - 1.1 * padding,
            points: [0, 0, -2.1 * padding, padding * 2.1],
            stroke: 'black',
          }"
            />




            <v-line
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 1 && (logicGate.logicType.name === 'LIGHT')"
              :config="{
            x: logicGate.position.x - padding,
            y: logicGate.position.y,
            points: [0, 0, -0.5 * padding, 0],
            stroke: 'black',
          }"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length == 2"
              :config="{
            x: logicGate.position.x - (1.5 * padding),
            y: logicGate.position.y - padding,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === 0 ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              @click="logicGateCircleClicked(index, true, 0)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length === 2"
              :config="{
            x: logicGate.position.x - (1.5 * padding),
            y: logicGate.position.y + padding,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === 1 ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              @click="logicGateCircleClicked(index, true, 1)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.logicType.name !== 'LIGHT' && logicGate.logicType.name !== 'SWITCH'"
              :config="{
            x: logicGate.position.x + 2.5 * padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === undefined ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              class="logic-gate-connector"
              @click="logicGateCircleClicked(index, false)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && (logicGate.logicType.name === 'LIGHT' || logicGate.logicType.name === 'SWITCH')"
              :config="{
            x: logicGate.position.x + 2.5 * padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === undefined ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              class="logic-gate-connector"
              @click="logicGateCircleClicked(index, false)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length == 1 && logicGate.logicType.name !== 'LIGHT' && logicGate.logicType.name !== 'SWITCH'"
              :config="{
            x: logicGate.position.x - 1.5 * padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === 0 ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              class="logic-gate-connector"
              @click="logicGateCircleClicked(index, true, 0)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
            />

            <v-circle
              v-if="(!snapbox.isShowingSnapBox || index !== snapbox.indexCurrentlyDragged) && logicGate.inputs.length == 1 && logicGate.logicType.name === 'LIGHT'"
              :config="{
            x: logicGate.position.x - 1.5 * padding,
            y: logicGate.position.y,
            radius: padding / 4,
            fill: connector.connectorIndex === index && connector.inputIndex === 0 ? 'blue' : 'red',
            stroke: 'black',
            strokeWidth: 1
          }"
              class="logic-gate-connector"
              @click="logicGateCircleClicked(index, true, 0)"
              @mouseover="onCircleHover"
              @mouseleave="onCircleHoverOut"
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

            <v-circle 
            :config="{
              x: logicGate.position.x + 0.5 * padding,
              y: logicGate.position.y,
              radius: 1.5 * padding,
              stroke: 'black',
              strokeWidth: 2,
              draggable: true
            }"
            v-if="logicGate.logicType.name === 'LIGHT' || logicGate.logicType.name === 'SWITCH'"
            @mouseover="showDragCursor"
            @mouseleave="showDefaultCursor"
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
          @mouseover="showDragCursor"
          @mouseleave="showDefaultCursor"

          />

        </v-layer>
      </v-stage>
    </div>
    <div>
      
      <div v-for="logicType in logicTypes" :key="logicType.name">
        <img
            :src="logicType.image"
            @click="addLogicGateToGrid(logicType)"
            class="logic-type"
            :width="logicType.width"
        />
      </div>

      <button class="uk-button uk-button-primary side-btns" uk-toggle="target: #modal">Instructions</button>
      <button class="uk-button uk-button-secondary side-btns" @click="downloadSchematic()">Download</button><br />

      <div id="modal" uk-modal>
        <div class="uk-modal-dialog uk-modal-body modal-body">
            <h1>Instructions</h1>
            <h2>Logic Gates</h2>
            <img :src="require('@/assets/lg_cheatsheet.jpg')"/>
            <h2>Using LogiCraft</h2>
            <ol>
              <li>Click on a logic gate on the side panel</li>
              <li>Drag logic gate from center to wanted position and repeat with other logic gates</li>
              <li>Connect logic gates by cliking on one's output and then clicking on another one's input</li>
              <li>Click download</li>
              <li>Double click file to extract</li>
              <li>Move folder into minecraft saves file</li> 
              <li>Open Minecraft and select the new world. Have fun!</li> 
            </ol>
            
            <button class="uk-modal-close uk-button uk-button-primary" type="button">Got it!</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      configKonva: {
        width: 1100,
        height: 800
      },
      logicTypes: [
        {
          name: "AND",
          image: require("@/assets/andGate.svg"),
          amountOfInputs: 2,
          width: "120px",
        },
        {
          name: "OR",
          image: require("@/assets/orGate.svg"),
          amountOfInputs: 2,
          width: "120px",
        },
        {
          name: "NOT",
          image: require("@/assets/notGate.svg"),
          amountOfInputs: 1,
          width: "120px",
        },

      {
        name: "LIGHT",
        image: require("@/assets/lightBulb.webp"),
        amountOfInputs: 1,
        width: "80px"
      },
      {
        name: "SWITCH",
        image: require("@/assets/power.jpg"),
        amountOfInputs: 0,
        width: "70px"
      },
      {
        name: "XOR",
        image: require("@/assets/xorGate.svg"),
        amountOfInputs: 2,
        width: "120px"
      }
      ],
      padding: 20,
      logicGates: [],
      snapbox: {
        isShowingSnapBox: false,
        indexCurrentlyDragged: null,
        position: { x: 0, y: 0 }
      },
      connector: {
        connectorIndex: null,
        isInput: null,
        inputIndex: null
      }
    };
  },
  methods: {
    addLogicGateToGrid(logicType) {
      const inputs = [];

      for (let i = 0; i < logicType.amountOfInputs; i++) {
        inputs.push(null); 
      }

      this.logicGates.push({
        logicType,
        position: {
          x: this.configKonva.width / 2 - this.padding / 2,
          y: this.configKonva.height / 2 - this.padding / 2
        },
        inputs
      });
    },
    onLogicGateDragged(index) {
      this.snapbox.isShowingSnapBox = true;
      this.snapbox.indexCurrentlyDragged = index;
    },
    onLogicGateDragEnd(index) {
      this.snapbox.isShowingSnapBox = false;
      this.logicGates[index].position.x = this.snapbox.position.x;
      this.logicGates[index].position.y = this.mapSnapPosToDragPos(
        this.snapbox.position.y
      );
    },
    onLogicGateDragMoved(event) {
      this.snapbox.position.x =
        Math.round(event.target.x() / this.padding) * this.padding;
      this.snapbox.position.y =
        this.mapWedgePosToSnapBox(
          Math.round((event.target.y() + this.padding / 2) / this.padding) *
            this.padding
        ) -
        this.padding / 2;
    },
    mapWedgePosToSnapBox(positionY) {
      return positionY - this.padding * 1.5;
    },
    mapSnapPosToDragPos(positionY) {
      return positionY + this.padding * 1.5;
    },
    logicGateCircleClicked(index, isInput, currentInputIndex) {
      if (this.connector.connectorIndex !== null) {
        // Cannot connect input to input
        if (
          (this.connector.isInput && isInput) ||
          (!this.connector.isInput && !isInput)
        ) {
          return;
        }

        const logicGateInputIndex = this.connector.isInput
          ? this.connector.connectorIndex
          : index;
        const logicGateOutputIndex = this.connector.isInput
          ? index
          : this.connector.connectorIndex;
        const inputIndex = this.connector.inputIndex !== null
          ? this.connector.inputIndex
          : currentInputIndex;
        console.log("this.connector.inputIndex is: ", this.connector.inputIndex);
        console.log("logic game input index is: ", logicGateInputIndex);
        console.log("logicGateOutputIndex is: ", logicGateOutputIndex);
        console.log("input index is: ", inputIndex);
        this.$set(
          this.logicGates[logicGateInputIndex].inputs,
          inputIndex,
          logicGateOutputIndex
        );
        console.log("I have set up the connection");
        console.log(this.logicGates[logicGateInputIndex].inputs);
        this.connector.connectorIndex = null;
        this.connector.isInput = null;
        this.connector.inputIndex = null;
      } else {
        this.connector.connectorIndex = index;
        this.connector.isInput = isInput;
        this.connector.inputIndex = currentInputIndex === undefined ? null : currentInputIndex ;
        console.log("I have set the input index to: ", this.connector.inputIndex);
      }
    },
    getPathIntesections(startingPosition, endingPosition) {
      console.log(startingPosition);
      console.log(endingPosition);
      if (
        startingPosition.x === endingPosition.x ||
        startingPosition.y === endingPosition.y
      ) {
        return [];
      } else {
        
        return [endingPosition.x - 1.5 * this.padding, startingPosition.y];
      }
    },
    calculateLinePath(logicGateOutput, logicGateIndex, logicGateInputIndex) {
      const startingPosition = this.logicGates[logicGateOutput].position;
      const endingPosition = this.logicGates[logicGateIndex].position;
      let endPositionSkewY;

      if (this.logicGates[logicGateIndex].inputs.length === 1) {
        endPositionSkewY = 0;
      } else if (logicGateInputIndex === 0) {
        endPositionSkewY = -this.padding;
      } else {
        endPositionSkewY = this.padding;
      }

      const pathIntersections = this.getPathIntesections(
        startingPosition,
        endingPosition
      );
      const startPositionPadded = [
        startingPosition.x + 2.5 * this.padding,
        startingPosition.y
      ];
      const endPositionPadded = [
        endingPosition.x - 1.5 * this.padding,
        endingPosition.y + endPositionSkewY
      ];
      const itIs = [
        ...startPositionPadded,
        ...pathIntersections,
        ...endPositionPadded
      ];

      console.log(itIs);
      return itIs;
    },
    async downloadSchematic() {
      // [{
      //    "type": "AND",
      //     inputs: [{
      //       "id": 2,
      //       "points": [(3, 4), (5, 2)]
      //      }],
      //    },
      //    "2": {}]

      const logicGatesData = this.logicGates.map((logicGate, index) => {
        const transformedInputs = logicGate.inputs
        .map(input => {
          if (input === null) return null;
          const startingPosition = this.logicGates[input].position;
          const endingPosition = logicGate.position;
          const pathIntersections = this.getPathIntesections(
            startingPosition,
            endingPosition
          );
          const unpaddedPathIntersections = pathIntersections.map(
            (pathIntersection, index) => {
              const alteredPathIntersection = pathIntersection / this.padding + 0.5
              if (index % 2 === 1) {
                return this.configKonva.height / this.padding - alteredPathIntersection + 1;
              }
              return alteredPathIntersection
            }
          );

          

          return {
            id: input,
            points: unpaddedPathIntersections.length ? [unpaddedPathIntersections] : []
          };
        });

        return {
          type: logicGate.logicType.name,
          inputs: transformedInputs,
          coordinate: [(logicGate.position.x / this.padding), this.configKonva.height / this.padding - ((logicGate.position.y / this.padding) + 1.5) + 1 ]
        };
      });

      console.log(logicGatesData);

      const res = await fetch("http://localhost:5000/api/schematic", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(logicGatesData)
      });

      const blob = await res.blob()
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "level.zip";
      document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
      a.click();    
      a.remove();  //afterward
    },
    onCircleHover() {
      document.body.style.cursor = "pointer";
    },
    onCircleHoverOut() {
      document.body.style.cursor = "default";
    },
    showDragCursor() {
      document.body.style.cursor = "grab";
    },
    showDefaultCursor() {
      document.body.style.cursor = "default";
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

.side-btns {
  width: 210px;
  margin-top: 20px;
}

.modal-body {
  width: 800px;
}
</style>
