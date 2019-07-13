from models.gate import Gate

class Light(Gate):

    def place_gate(self):
        x = self.coord[0]
        z = self.coord[1]
        self.editor.set_block(z+0, 50, x+0, "red_wool")
        self.editor.set_block(z+1, 50, x+0, "red_wool")
        self.editor.set_block(z+2, 50, x+0, "red_wool")
        self.editor.set_block(z+0, 50, x+1, "red_wool")
        self.editor.set_block(z+1, 50, x+1, "red_wool")
        self.editor.set_block(z+2, 50, x+1, "red_wool")
        self.editor.set_block(z+0, 50, x+2, "red_wool")
        self.editor.set_block(z+1, 50, x+2, "red_wool")
        self.editor.set_block(z+2, 50, x+2, "red_wool")
        self.editor.set_block(z+1, 52, x+1, "red_wool")
        
        self.editor.set_block(z+1, 52, x+0, "lever")

        self.editor.set_block(z+1, 51, x+1, "redstone_wire", {"power": "0", "north": "side"})

        self.editor.set_block(z+1, 51, x+2, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})