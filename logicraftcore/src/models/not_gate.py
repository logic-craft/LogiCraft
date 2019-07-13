from models.gate import Gate

class Not(Gate):
    
    def place_gate(self):
        x = self.coord[0]
        z = self.coord[1]
        self.editor.set_block(z+0, self.BASE_Y, x+0, "pink_wool")
        self.editor.set_block(z+1, self.BASE_Y, x+0, "pink_wool")
        self.editor.set_block(z+2, self.BASE_Y, x+0, "pink_wool")
        self.editor.set_block(z+0, self.BASE_Y, x+1, "pink_wool")
        self.editor.set_block(z+1, self.BASE_Y, x+1, "pink_wool")
        self.editor.set_block(z+2, self.BASE_Y, x+1, "pink_wool")
        self.editor.set_block(z+0, self.BASE_Y, x+2, "pink_wool")
        self.editor.set_block(z+1, self.BASE_Y, x+2, "pink_wool")
        self.editor.set_block(z+2, self.BASE_Y, x+2, "pink_wool")
        self.editor.set_block(z+0, self.BASE_Y, x+3, "pink_wool")
        self.editor.set_block(z+1, self.BASE_Y, x+3, "pink_wool")
        self.editor.set_block(z+2, self.BASE_Y, x+3, "pink_wool")

        self.editor.set_block(z+0, 51, x+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(z+2, 51, x+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(z+1, 51, x+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(z+1, 51, x+2, "redstone_wire", {"power": "0"})
        
        self.editor.set_block(z+0, 51, x+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
        self.editor.set_block(z+2, 51, x+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
        self.editor.set_block(z+1, 51, x+3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})