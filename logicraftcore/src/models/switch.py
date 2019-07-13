from models.gate import Gate

class Switch(Gate):

    def place_gate(self):
        z = self.coord[0]
        x = self.coord[1]
        
        self.editor.set_block(x+0, 50, z+0, "light_blue_wool")
        self.editor.set_block(x+1, 50, z+0, "light_blue_wool")
        self.editor.set_block(x+2, 50, z+0, "light_blue_wool")
        self.editor.set_block(x+0, 50, z+1, "light_blue_wool")
        self.editor.set_block(x+1, 50, z+1, "light_blue_wool")
        self.editor.set_block(x+2, 50, z+1, "light_blue_wool")
        self.editor.set_block(x+0, 50, z+2, "light_blue_wool")
        self.editor.set_block(x+1, 50, z+2, "light_blue_wool")
        self.editor.set_block(x+2, 50, z+2, "light_blue_wool")
        self.editor.set_block(x+1, 52, z+1, "light_blue_wool")
        
        self.editor.set_block(x+1, 52, z+0, "lever")

        self.editor.set_block(x+1, 51, z+1, "redstone_wire", {"power": "0", "north": "side"})

        self.editor.set_block(x+1, 51, z+2, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
