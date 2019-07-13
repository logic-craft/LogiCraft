from editcraftAPI.editor import Editor
import os


class Gate:
    def __init__(self, id, inputs, coord, total_points):
        self.id = id
        self.inputs = inputs
        self.coord = coord
        self.editor = Editor(os.path.abspath(os.path.join("../maps/LogiCraftCopy")))
        self.total_points = total_points
        self.BASE_Y = 50
    
    def get_input_1_coord(self):
        return [self.coord[0] - 1, self.coord[1] + 2]

    def get_input_2_coord(self):
        return [self.coord[0] - 1, self.coord[1]]

    def get_input_coord(self, coord_num=1):
        if len(self.inputs) == 1:
            return [self.coord[0] - 1, self.coord[1] + 1]

        if coord_num == 1:
            return self.get_input_1_coord()

        if coord_num == 2:
            return self.get_input_2_coord()

    def get_output_coord(self):
        return [self.coord[0] + 3, self.coord[1] + 1]
    
    def set_redstone(self, coord, y=50):
        self.editor.set_block(coord[1], y, coord[0], "red_wool")
        self.editor.set_block(coord[1], y + 1, coord[0], "redstone_wire")

    def set_repeater(self, coord, direction):
        self.editor.set_block(coord[1], self.BASE_Y, coord[0], "red_wool")
        self.editor.set_block(coord[1], self.BASE_Y + 1, coord[0], "repeater", {"facing": direction, "delay": "1", "powered": "false", "locked": "false"})

    def place_redstone(self):
        for _input in range(len(self.inputs)):
            if self.inputs[_input] == None:
                continue
             
            points = [self.inputs[_input]["output"]] + self.inputs[_input]["points"] + [self.get_input_coord(_input + 1)]
            self.total_points += points
            print("total points", self.total_points)

            length = 0
            for i in range(len(points) - 1):
                print("new point")
                if points[i][0] == points[i + 1][0]:
                    difference = points[i + 1][1] - points[i][1]
                    multiplier = difference // abs(difference) # 1 or -1
                    skip = 0
                    for j in range(0, difference + multiplier, multiplier):
                        if (skip > 0):
                            skip -= 1
                            continue

                        point = [points[i][0], points[i][1] + j]
                        next_point = [point[0], point[1] + multiplier]
                    
                        if self.editor.get_block_name(point[1], self.BASE_Y, point[0]) == "air" and self.editor.get_block_name(next_point[1], self.BASE_Y, next_point[0]) == "red_wool":
                            self.set_redstone(point, self.BASE_Y + 1)
                            self.set_redstone(next_point, self.BASE_Y + 2)
                            self.set_redstone([next_point[0], next_point[1] + multiplier], self.BASE_Y + 1)
                            self.set_redstone([next_point[0], next_point[1] + 2 * multiplier], self.BASE_Y)
                            skip = 3
                            length += 4
                            continue

                        length += 1
                        print("length5", length, point)
                        if point not in self.total_points and (length > 10):
                            self.set_repeater(point, "west" if multiplier == 1 else "east")
                            length = 0
                        else:
                            self.set_redstone(point)

                elif points[i][1] == points[i + 1][1]:
                    difference = points[i + 1][0] - points[i][0]
                    multiplier = difference // abs(difference) # 1 or -1
                    skip = 0
                    for j in range(0, difference + multiplier, multiplier):
                        if (skip > 0):
                            skip -= 1
                            continue

                        point = [points[i][0] + j, points[i][1]]
                        next_point = [point[0] + multiplier, point[1]]

                        if self.editor.get_block_name(point[1], self.BASE_Y, point[0]) == "air" and self.editor.get_block_name(next_point[1], self.BASE_Y, next_point[0]) == "red_wool":
                            self.set_redstone(point, self.BASE_Y + 1)
                            self.set_redstone(next_point, self.BASE_Y + 2)
                            self.set_redstone([next_point[0] + multiplier, next_point[1]], self.BASE_Y + 1)
                            self.set_redstone([next_point[0] + 2 * multiplier, next_point[1]], self.BASE_Y)
                            skip = 3
                            length += 4
                            continue

                        length += 1
                        print("length5", length, point)
                        if point not in self.total_points and (length > 10):
                            self.set_repeater(point, "north" if multiplier == 1 else "south")
                            length = 0
                        else:
                            self.set_redstone(point)






