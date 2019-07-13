from models.gate import Gate

class Light(Gate):

    def place_gate(self):
        z = self.coord[0]
        x = self.coord[1]
        self.editor.set_block(x+0, 50, z+0, "gray_wool")
        self.editor.set_block(x+1, 50, z+0, "gray_wool")
        self.editor.set_block(x+2, 50, z+0, "gray_wool")
        self.editor.set_block(x+0, 50, z+1, "gray_wool")
        self.editor.set_block(x+1, 50, z+1, "gray_wool")
        self.editor.set_block(x+2, 50, z+1, "gray_wool")
        self.editor.set_block(x+0, 50, z+2, "gray_wool")
        self.editor.set_block(x+1, 50, z+2, "gray_wool")
        self.editor.set_block(x+2, 50, z+2, "gray_wool")
        
        self.editor.set_block(x+1, 51, z+1, "gray_wool")
        self.editor.set_block(x+1, 53, z+1, "gray_wool")

        self.editor.set_block(x+1, 52, z+1, "redstone_torch")
        self.editor.set_block(x+1, 54, z+1, "redstone_torch", {"lit": "false"})
        self.editor.set_block(x+1, 55, z+1, "redstone_lamp")
        self.editor.set_block(x+0, 54, z+1, "redstone_lamp")
        self.editor.set_block(x+2, 54, z+1, "redstone_lamp")
        self.editor.set_block(x+1, 54, z+0, "redstone_lamp")
        self.editor.set_block(x+1, 54, z+2, "redstone_lamp")

        self.editor.set_block(x+1, 51, z+2, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
        self.editor.set_block(x+1, 51, z+0, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
