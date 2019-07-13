from models.gate import Gate

class Not(Gate):

    def place_gate(self):
        x = self.coord[0]
        z = self.coord[1]
        self.editor.set_block(z+0, 50, x+0, "green_wool")
        self.editor.set_block(z+1, 50, x+0, "green_wool")
        self.editor.set_block(z+2, 50, x+0, "green_wool")
        self.editor.set_block(z+0, 50, x+1, "green_wool")
        self.editor.set_block(z+1, 50, x+1, "green_wool")
        self.editor.set_block(z+2, 50, x+1, "green_wool")
        self.editor.set_block(z+0, 50, x+2, "green_wool")
        self.editor.set_block(z+1, 50, x+2, "green_wool")
        self.editor.set_block(z+2, 50, x+2, "green_wool")
        self.editor.set_block(z+1, 51, x+1, "green_wool")

        self.editor.set_block(z+1, 51, x+2, "redstone_wall_torch", {"lit": "true", "facing": "south"})
    
        self.editor.set_block(z+1, 51, x+0, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
