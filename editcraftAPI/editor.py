from editcraftAPI.chunkrow import *

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