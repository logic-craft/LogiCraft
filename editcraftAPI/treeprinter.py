import os
import nbt
from nbt.chunk import *
from nbt.world import WorldFolder
from nbt.nbt import NBTFile

world_folder = os.path.normpath("/home/campbell/.minecraft/saves/glass2/")
world = WorldFolder(world_folder)
#print(nbtt.pretty_tree())
print(world.get_region(0,0).get_nbt(0,0)['Level']['Sections'][1].pretty_tree())
#print(world.get_region(0,0).get_chunks())
for i, state in enumerate (world.get_region(0,0).get_nbt(1,0)['Level']['Sections'][1]['BlockStates']):
    print(state, i)


