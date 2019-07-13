
from models.gate import Gate

class And(Gate):
    
    def place_gate(self):
        x = self.coord[0]
        z = self.coord[1]
        self.editor.set_block(z+0, 50, x+0, "yellow_wool")
        self.editor.set_block(z+1, 50, x+0, "yellow_wool")
        self.editor.set_block(z+2, 50, x+0, "yellow_wool")
        self.editor.set_block(z+0, 50, x+1, "yellow_wool")
        self.editor.set_block(z+1, 50, x+1, "yellow_wool")
        self.editor.set_block(z+2, 50, x+1, "yellow_wool")
        self.editor.set_block(z+0, 51, x+1, "yellow_wool")
        self.editor.set_block(z+1, 51, x+1, "yellow_wool")
        self.editor.set_block(z+2, 51, x+1, "yellow_wool")
        self.editor.set_block(z+0, 50, x+2, "yellow_wool")
        self.editor.set_block(z+1, 50, x+2, "yellow_wool")
        self.editor.set_block(z+2, 50, x+2, "yellow_wool")

        self.editor.set_block(z+1, 52, x+1, "redstone_wire", {"power": "15", "north": "side"})

        self.editor.set_block(z+0, 52, x+1, "redstone_torch")
        self.editor.set_block(z+2, 52, x+1, "redstone_torch")

        self.editor.set_block(z+1, 51, x+2, "redstone_wall_torch", {"lit": "false", "facing": "south"})
        
        self.editor.set_block(z+0, 51, x+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
        self.editor.set_block(z+2, 51, x+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})