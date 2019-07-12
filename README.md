# LogiCraft
## Problem
The department of specific sciency matters has a Science Education sub-department that wants to create software to improve science education amoung younger teens and children. One area of science education that is not easily accessible for younger kids is computer science.

## Solution
To improve engagement in computer science amongst kids, we want to create software that will make learning computer science concepts fun and interactive in a relatable way. A major section of computer science is learning and understanding how computers work on a lower level. Logic gates is an essential learning step in understanding the inner workings of computers. Nowadays video games make up a large portion of kids time and intrests so we want to leverage this to help make learning about computer science more fun.

Minecraft is a world building game most popular amoung a younger audience. Minecraft has a powerful mechanic called redstone which can essentially represent electrical components. Inparticular, logic gates are  easily represented using the redstone mechanics. By allowing users of LogiCraft™ to create and convert logic gate schematics into a minecraft world, users can see a visualisation and begin to explore and understand logic gates in a familiar context.

LogiCraft is composed of three main parts: EditCraftAPI, SchematiCraft, LogiCraftCore

### EditCraftAPI
EditCraftAPI is going to be the section of our project that will allow us to interface with minecraft world files and give us the needed capabilites to read/write block data.
Minecraft uses a proprietary file type to save data called NBT. We have been able to find an NBT parser python library which we will use to create our API.

Note: No existing solutions exist for the Java Edition (Atleast not in current versions of Minecraft)

### SchematiCraft

### LogiCraftCore
LogiCraftCore is going to be responsible for connecting and converting the SchematiCraft data into block data for the EditCraftAPI.
This will require:
 - Parsing the SchemtiCraft output
 - Converting individual gates and wires into block data
 - Ensuring block data doesn't overlap/is valid
 - Calling the EditCraftAPI to place the blocks in the correct coordinates

