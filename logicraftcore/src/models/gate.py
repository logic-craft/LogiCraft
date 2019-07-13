from editcraftAPI.editor import Editor
import os


class Gate:
    def __init__(self, id, inputs, coord):
        self.id = id
        self.inputs = inputs
        self.coord = coord
        self.editor = Editor(os.path.abspath(os.path.join("../maps/LogiCraftCopy")))
        self.BASE_Y = 50
    
    def get_input_1_coord(self):
        return [self.coord[0] - 1, self.coord[1] + 2]

    def get_input_2_coord(self):
        return [self.coord[0] - 1, self.coord[1]]

    def get_input_coord(self, coord_num=1):
        if coord_num == 1:
            return self.get_input_1_coord()
        elif coord_num == 2:
            return self.get_input_2_coord()


    def get_output_coord(self):
        return [self.coord[0] + 4, self.coord[1] + 1]
    
    def set_redstone(self, coord):
        self.editor.set_block(coord[1], self.BASE_Y, coord[0], "red_wool")
        self.editor.set_block(coord[1], self.BASE_Y + 1, coord[0], "redstone_wire")

    def place_redstone(self):
        for _input in range(len(self.inputs)):
            points = [self.inputs[_input]["output"]] + self.inputs[_input]["points"] + [self.get_input_coord(2)]
            
            for i in range(len(points) - 1):

                if points[i][0] == points[i + 1][0]:
                    difference = points[i][1] - points[i + 1][1]
                    multiplier = difference // abs(difference) # 1 or -1
                    for j in range(0, difference + multiplier, multiplier):
                        self.set_redstone([points[i + 1][0], points[i + 1][1] + j])

                elif points[i][1] == points[i + 1][1]:
                    difference = points[i][0] - points[i + 1][0]
                    multiplier = difference // abs(difference) # 1 or -1
                    for j in range(0, difference + multiplier, multiplier):
                        self.set_redstone([points[i + 1][0] + j, points[i + 1][1]])






