import os
import nbt
import sys
from nbt.chunk import *
from nbt.world import WorldFolder
from nbt.nbt import *

CHUNK_SIZE = 16
REGION_SIZE = 32

class Block():
    def __init__(self, name, palette_index):
        self.name = name
        self.palette_index = str(palette_index)

class ChunkRow():
    def __init__(self, region_nbt, section_id, y, z):
        self.region_nbt = region_nbt
        self.section_id = section_id
        self.row_index = (y + 1) * CHUNK_SIZE + z
        self.palette = self._read_palette()
        self.blocks = self._read_blocks()

    def __getitem__(self, x):
        """Returns block at the keys index"""
        return self.blocks[x]

    def __setitem__(self, x, block_and_properties):
        """Sets block at keys index to given block"""
        (block_name, properties) = block_and_properties
        self.blocks[x] = Block(block_name, self._get_or_insert_palette(block_name, properties))
        print(len(str(self._calc_block_state())),len("2305843009213693952"), len(str(sys.maxsize)))
        self.region_nbt['Level']['Sections'][self.section_id]['BlockStates'][self.row_index] = self._calc_block_state()

    def _read_palette(self):
        """Returns palette of usable blocks"""
        try:
            tag_palette = self.region_nbt['Level']['Sections'][self.section_id]['Palette']
        except KeyError:
            self._add_to_palette("air")
            tag_palette = self.region_nbt['Level']['Sections'][self.section_id]['Palette']
        return [tag['Name'].value[10:] for tag in tag_palette]

    def _read_blocks(self):
        """Initialises the blocks array"""
        try:
            row_state = self.region_nbt['Level']['Sections'][self.section_id]['BlockStates'][self.row_index]
        except KeyError:
            raise ("Shit dont exist fam fix me up")
            #self._create_block_states()
            #row_state = 0
        print(row_state)
        if (row_state < 0):
            row_state -= (16**15*8)*-1
            row_state = ("%0.16X" % row_state)
            row_state =  row_state[::-1][1:] + ("%0.1X" % (int(row_state[0], 16) + 8))
        else:
            row_state = ("%0.16X" % row_state)[::-1]
        print(row_state)
        print(self.palette)
        return [Block(self.palette[int(palette_index, 16)], palette_index) for palette_index in row_state]

    def _calc_block_state(self):
        """Returns the value of the blockstate for tje chunk row"""
        state = "".join([block.palette_index for block in self.blocks[::-1]])
        print(state)
        heavy = int(state[0], 16)
        if heavy < 8:
            return int(state, 16)
        else:
            state = str(heavy - 8) + state[1:]
            print(state, int(state, 16))
            return int(state, 16) + (16**15*8)*-1


    def _get_or_insert_palette(self, block_name, properties):
        """Returns the id of the block in palette (inserts if doesnt alread exist)"""
        try:
            return self._match_palette(block_name, properties)
        except ValueError:
            self._add_to_palette(block_name, properties)
            self.palette.append(block_name)
            # for i, block in enumerate(self.blocks):
            #     if int(block.palette_index, 16) >= 2:
            #         block.palette_index = "%0.1X" % (int(block.palette_index, 16) + 1)
            #         self.blocks[i] =  block
            return "%0.1X" % (len(self.palette) - 1)

    def _match_palette(self, block_name, properties):
        """Matches block in palette"""
        for  pal_index in [i for i, pal in enumerate(self.palette) if pal == block_name]:
            if properties == None:
                return "%0.1X" % pal_index
            isMatch = True
            for k, v in properties.items():
                try:
                    if self.region_nbt['Level']['Sections'][self.section_id]['Palette'][pal_index]['Properties'][k].value != v:
                        isMatch = False
                        
                        print(k,v,self.region_nbt['Level']['Sections'][self.section_id]['Palette'][pal_index]['Properties'][k])
                        break
                except KeyError:
                    isMatch = False
                    break
            if isMatch:
                return "%0.1X" % pal_index
        raise ValueError("No match")
        


    # def _create_block_states(self):
    #     """Creates the blockstate array"""
    #     if "BlockStates" in self.region_nbt['Level']['Sections'][self.section_id]:
    #         return
    #     self.region_nbt['Level']['Sections'][self.section_id].tags.append(TAG_Long_Array(name="BlockStates", buffer=255))
    #     print(self.region_nbt['Level']['Sections'][self.section_id]["BlockStates"].valuestr())
    #     for i in range(256):
    #         self.region_nbt['Level']['Sections'][self.section_id]["BlockStates"][-1]
        

    def _add_to_palette(self, block_name, properties=None):
        print("addddd")
        """Adds a block into the nbt palette"""
        if "Palette" not in self.region_nbt['Level']['Sections'][self.section_id]:
            self.region_nbt['Level']['Sections'][self.section_id]["Palette"] = TAG_List(name="Palette", type=TAG_Compound)
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'].append(TAG_Compound())
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'][-1].tags.append(TAG_String(name="Name",value="minecraft:" + block_name))
        #####This is to add properties when we need them #####
        if properties is not None:
            properties_tag=TAG_Compound()
            properties_tag.name="Properties"
            for k,v in properties.items():
                properties_tag.tags.append(TAG_String(name=k,value=v))
            self.region_nbt['Level']['Sections'][self.section_id]['Palette'].tags[-1].tags.append(properties_tag)