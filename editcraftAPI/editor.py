import os
import nbt
import sys
from nbt.chunk import *
from nbt.world import WorldFolder
from nbt.nbt import *

CHUNK_SIZE = 16
REGION_SIZE = 32

class Editor():
    def __init__(self, path):
        self.path = os.path.normpath(path)
        self.world_folder = WorldFolder(self.path)
    
    def set_block(self, x, y, z, name, properties=None):
        """Sets the block type to the given coords"""
        chunk_x = x % CHUNK_SIZE
        chunk_y = y % CHUNK_SIZE
        chunk_z = z % CHUNK_SIZE
        region = self.get_region(x, z)
        region_nbt = self.get_region_nbt(x, z, region)
        section_id = self.get_section_id(x, y, z, region_nbt['Level']['Sections'])
        chunk_row = ChunkRow(region_nbt, section_id, chunk_y, chunk_z)
        chunk_row[chunk_x] = (name, properties)
        self.set_region_nbt(x, z, region, chunk_row.region_nbt)
    
    def get_block_id(self, x, y, z):
        """gets block id from given coords"""
        pass
    
    def get_block_name(self, x, y, z):
        """gets block name from given coords"""
        chunk_x = x % CHUNK_SIZE
        chunk_y = y % CHUNK_SIZE
        chunk_z = z % CHUNK_SIZE
        region = self.get_region(x, z)
        region_nbt = self.get_region_nbt(x, z, region)
        section_id = self.get_section_id(x, y, z, region_nbt['Level']['Sections'])
        chunk_row = ChunkRow(region_nbt, section_id, chunk_y, chunk_z)
        return chunk_row[chunk_x].name
        
    def get_region_nbt(self, x, z, region):
        """Returns correct region nbt for given x, y coords"""
        return region.get_nbt(x%(REGION_SIZE*CHUNK_SIZE)//CHUNK_SIZE, z%(REGION_SIZE*CHUNK_SIZE)//CHUNK_SIZE)

    def get_region(self, x, z):
        """Returns correct region nbt for given x, y coords"""
        return self.world_folder.get_region(x//(REGION_SIZE*CHUNK_SIZE), z//(REGION_SIZE*CHUNK_SIZE))
    
    def set_region_nbt(self, x, z, region, region_nbt):
        """Writes nbt to file"""
        region.write_chunk(x%(REGION_SIZE*CHUNK_SIZE)//CHUNK_SIZE, z%(REGION_SIZE*CHUNK_SIZE)//CHUNK_SIZE, region_nbt)

    def get_section_id(self, x, y, z, sections):
        """gets the corrrect section of the region"""
        #TODO: Actually fiquer this out
        return 1
        

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
        print(self.palette)
        print(self.row_index)
        print(self._calc_block_state(),2305843009213693952, sys.maxsize)
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
        row_state = ("%0.16X" % row_state)[::-1]
        return [Block(self.palette[int(palette_index, 16)], palette_index) for palette_index in row_state]

    def _calc_block_state(self):
        """Returns the value of the blockstate for tje chunk row"""
        state = "".join([block.palette_index for block in self.blocks[::-1]])
        print(state[::-1])
        return int(state, 16)

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
<<<<<<< HEAD
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'].append(TAG_Compound())
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'][-1].tags.append(TAG_String(name="Name",value="minecraft:" + block_name))
=======
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'].insert(2, TAG_Compound())
        self.region_nbt['Level']['Sections'][self.section_id]['Palette'][2].tags.append(TAG_String(name="Name",value="minecraft:" + block_name))
>>>>>>> 1a4bdc4c98f6fd7b21693d943493c373939cf51d
        #####This is to add properties when we need them #####
        if properties is not None:
            properties_tag=TAG_Compound()
            properties_tag.name="Properties"
            for k,v in properties.items():
                properties_tag.tags.append(TAG_String(name=k,value=v))
<<<<<<< HEAD
            self.region_nbt['Level']['Sections'][self.section_id]['Palette'].tags[-1].tags.append(properties_tag)
=======
            self.region_nbt['Level']['Sections'][self.section_id]['Palette'].tags[2].tags.append(properties_tag)
>>>>>>> 1a4bdc4c98f6fd7b21693d943493c373939cf51d






    

