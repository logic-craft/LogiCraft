from models.gate import Gate

class Xor(Gate):
    
    def place_gate(self):
        z = self.coord[0]
        x = self.coord[1]
        self.editor.set_block(x+0, 50, z+0, "orange_wool")
        self.editor.set_block(x+1, 50, z+0, "orange_wool")
        self.editor.set_block(x+2, 50, z+0, "orange_wool")
        self.editor.set_block(x+0, 50, z+1, "orange_wool")
        self.editor.set_block(x+1, 50, z+1, "orange_wool")
        self.editor.set_block(x+2, 50, z+1, "orange_wool")
        self.editor.set_block(x+0, 50, z+2, "orange_wool")
        self.editor.set_block(x+1, 50, z+2, "orange_wool")
        self.editor.set_block(x+2, 50, z+2, "orange_wool")
        self.editor.set_block(x+0, 50, z+3, "orange_wool")
        self.editor.set_block(x+1, 50, z+3, "orange_wool")
        self.editor.set_block(x+2, 50, z+3, "orange_wool")

        self.editor.set_block(x+2, 51, z+0, "orange_wool")
        self.editor.set_block(x+0, 51, z+0, "orange_wool")
        self.editor.set_block(x+2, 52, z+1, "orange_wool")
        self.editor.set_block(x+0, 52, z+1, "orange_wool")
        
        self.editor.set_block(x+0, 52, z+2, "orange_wool")
        self.editor.set_block(x+2, 52, z+2, "orange_wool")
        self.editor.set_block(x+0, 54, z+1, "orange_wool")
        self.editor.set_block(x+2, 54, z+1, "orange_wool")
        self.editor.set_block(x+1, 53, z+1, "orange_wool")
        

        self.editor.set_block(x+0, 51, z+3, "redstone_wire", {"power": "0", "north": "side"})
        self.editor.set_block(x+1, 51, z+3, "redstone_wire", {"power": "0", "north": "side"})
        self.editor.set_block(x+2, 51, z+3, "redstone_wire", {"power": "0", "north": "side"})
        self.editor.set_block(x+0, 52, z+0, "redstone_wire", {"power": "0", "north": "side"})
        self.editor.set_block(x+2, 52, z+0, "redstone_wire", {"power": "0", "north": "side"})
        self.editor.set_block(x+0, 53, z+2, "redstone_wire", {"power": "15", "north": "side"})
        self.editor.set_block(x+2, 53, z+2, "redstone_wire", {"power": "15", "north": "side"})
        self.editor.set_block(x+1, 54, z+1, "redstone_wire", {"power": "15", "north": "side"})

        self.editor.set_block(x+0, 53, z+1, "redstone_torch")
        self.editor.set_block(x+2, 53, z+1, "redstone_torch")

        self.editor.set_block(x+0, 52, z+3, "redstone_wall_torch", {"lit": "false", "facing": "south"})
        self.editor.set_block(x+2, 52, z+3, "redstone_wall_torch", {"lit": "false", "facing": "south"})
        self.editor.set_block(x+1, 53, z+2, "redstone_wall_torch", {"lit": "false", "facing": "south"})
 