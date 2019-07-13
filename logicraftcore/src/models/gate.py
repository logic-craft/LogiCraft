from editcraftAPI.editor import Editor

BASE_Y = 51

class Gate:
    def __init__(self, id, inputs, coord):
        self.id = id
        self.coord = coord
        self.editor = Editor("./logicraftcore/maps/LogiCraftCopy")
    
    def get_input_top_coord(self):
        return [self.coord[0] - 1, self.coord[1] + 2]

    def get_input_middle_coord(self):
        return [self.coord[0] - 1, self.coord[1] + 1]

    def get_input_bottom_coord(self):
        return [self.coord[0] - 1, self.coord[1]]

    def get_output_coord(self):
        return [self.coord[0] + 4, self.coord[1] + 1]
    
    def place_redstone(self):
        self.editor.set_redstone()



