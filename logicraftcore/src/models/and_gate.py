
from models.gate import Gate

class And(Gate):
    
    def place_gate(self):
        x = self.coord[0]
        z = self.coord[1]
        self.editor.set_block(x+0, self.BASE_Y, z+0, "pink_wool")
        self.editor.set_block(x+1, self.BASE_Y, z+0, "pink_wool")
        self.editor.set_block(x+2, self.BASE_Y, z+0, "pink_wool")
        self.editor.set_block(x+0, self.BASE_Y, z+1, "pink_wool")
        self.editor.set_block(x+1, self.BASE_Y, z+1, "pink_wool")
        self.editor.set_block(x+2, self.BASE_Y, z+1, "pink_wool")
        self.editor.set_block(x+0, self.BASE_Y, z+2, "pink_wool")
        self.editor.set_block(x+1, self.BASE_Y, z+2, "pink_wool")
        self.editor.set_block(x+2, self.BASE_Y, z+2, "pink_wool")
        self.editor.set_block(x+0, self.BASE_Y, z+3, "pink_wool")
        self.editor.set_block(x+1, self.BASE_Y, z+3, "pink_wool")
        self.editor.set_block(x+2, self.BASE_Y, z+3, "pink_wool")

        self.editor.set_block(x+0, 51, z+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(x+2, 51, z+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(x+1, 51, z+1, "redstone_wire", {"power": "0"})
        self.editor.set_block(x+1, 51, z+2, "redstone_wire", {"power": "0"})
        
        self.editor.set_block(x+0, 51, z+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
        self.editor.set_block(x+2, 51, z+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
        self.editor.set_block(x+1, 51, z+3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})