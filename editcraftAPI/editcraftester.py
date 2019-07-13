""" This iajust for testing"""

import  sys
from editor import Editor

def main(world_folder):
    """Create and run editor"""
    editor = Editor(world_folder)
    #print(editor.get_block_name(1, 120, 3))
    and_gate(editor)
    or_gate(editor, 5, 0)
    not_gate(editor, 10, 0)
    switch(editor, 15, 0)
    light(editor, 20, 0)
    xor_gate(editor, 30, 0)
    d_flip_flop(editor, 25, 0)
    #checker(editor)

def checker(editor):
    editor.set_block(15, 50, 0, "red_wool")
    editor.set_block(15, 50, 1, "green_wool")
    editor.set_block(15, 50, 2, "pink_wool")
    editor.set_block(15, 50, 3, "gray_wool")
    editor.set_block(15, 50, 4, "black_wool")
    editor.set_block(15, 50, 5, "white_wool")
    editor.set_block(15, 50, 6, "orange_wool")
    editor.set_block(15, 50, 7, "blue_wool")
    editor.set_block(14, 50, 6, "orange_wool")
    editor.set_block(14, 50, 7, "blue_wool")

def d_flip_flop(editor, x, z):
    editor.set_block(x+0, 50, z+0, "blue_wool")
    editor.set_block(x+1, 50, z+0, "blue_wool")
    editor.set_block(x+2, 50, z+0, "blue_wool")
    editor.set_block(x+0, 50, z+1, "blue_wool")
    editor.set_block(x+1, 50, z+1, "blue_wool")
    editor.set_block(x+2, 50, z+1, "blue_wool")
    editor.set_block(x+0, 50, z+2, "blue_wool")
    editor.set_block(x+1, 50, z+2, "blue_wool")
    editor.set_block(x+2, 50, z+2, "blue_wool")
    editor.set_block(x+0, 51, z+2, "blue_wool")
    
    editor.set_block(x+0, 51, z+1, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
    editor.set_block(x+1, 51, z+1, "repeater", {"facing": "east", "delay": "1", "powered": "false", "locked": "false"})





def light (editor, x, y):
    editor.set_block(x+0, 50, y+0, "red_wool")
    editor.set_block(x+1, 50, y+0, "red_wool")
    editor.set_block(x+2, 50, y+0, "red_wool")
    editor.set_block(x+0, 50, y+1, "red_wool")
    editor.set_block(x+1, 50, y+1, "red_wool")
    editor.set_block(x+2, 50, y+1, "red_wool")
    editor.set_block(x+0, 50, y+2, "red_wool")
    editor.set_block(x+1, 50, y+2, "red_wool")
    editor.set_block(x+2, 50, y+2, "red_wool")
    
    editor.set_block(x+1, 51, y+1, "redstone_lamp")

    editor.set_block(x+1, 51, y+2, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
    editor.set_block(x+1, 51, y+0, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})


def switch (editor, x, y):
    editor.set_block(x+0, 50, y+0, "red_wool")
    editor.set_block(x+1, 50, y+0, "red_wool")
    editor.set_block(x+2, 50, y+0, "red_wool")
    editor.set_block(x+0, 50, y+1, "red_wool")
    editor.set_block(x+1, 50, y+1, "red_wool")
    editor.set_block(x+2, 50, y+1, "red_wool")
    editor.set_block(x+0, 50, y+2, "red_wool")
    editor.set_block(x+1, 50, y+2, "red_wool")
    editor.set_block(x+2, 50, y+2, "red_wool")
    editor.set_block(x+1, 52, y+1, "red_wool")
    
    editor.set_block(x+1, 52, y+0, "lever")

    editor.set_block(x+1, 51, y+1, "redstone_wire", {"power": "0", "north": "side"})

    editor.set_block(x+1, 51, y+2, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})

def xor_gate(editor, x, y):
    editor.set_block(x+0, 50, y+0, "orange_wool")
    editor.set_block(x+1, 50, y+0, "orange_wool")
    editor.set_block(x+2, 50, y+0, "orange_wool")
    editor.set_block(x+0, 50, y+1, "orange_wool")
    editor.set_block(x+1, 50, y+1, "orange_wool")
    editor.set_block(x+2, 50, y+1, "orange_wool")
    editor.set_block(x+0, 50, y+2, "orange_wool")
    editor.set_block(x+1, 50, y+2, "orange_wool")
    editor.set_block(x+2, 50, y+2, "orange_wool")
    editor.set_block(x+0, 50, y+3, "orange_wool")
    editor.set_block(x+1, 50, y+3, "orange_wool")
    editor.set_block(x+2, 50, y+3, "orange_wool")

    editor.set_block(x+2, 51, y+0, "orange_wool")
    editor.set_block(x+0, 51, y+0, "orange_wool")
    editor.set_block(x+2, 52, y+1, "orange_wool")
    editor.set_block(x+0, 52, y+1, "orange_wool")
    
    editor.set_block(x+0, 52, y+2, "orange_wool")
    editor.set_block(x+2, 52, y+2, "orange_wool")
    editor.set_block(x+0, 54, y+1, "orange_wool")
    editor.set_block(x+2, 54, y+1, "orange_wool")
    editor.set_block(x+1, 53, y+1, "orange_wool")
    

    editor.set_block(x+0, 51, y+3, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+1, 51, y+3, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+2, 51, y+3, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+0, 52, y+0, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+2, 52, y+0, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+0, 53, y+2, "redstone_wire", {"power": "15", "north": "side"})
    editor.set_block(x+2, 53, y+2, "redstone_wire", {"power": "15", "north": "side"})
    editor.set_block(x+1, 54, y+1, "redstone_wire", {"power": "15", "north": "side"})

    editor.set_block(x+0, 53, y+1, "redstone_torch")
    editor.set_block(x+2, 53, y+1, "redstone_torch")

    editor.set_block(x+0, 52, y+3, "redstone_wall_torch", {"lit": "false", "facing": "south"})
    editor.set_block(x+2, 52, y+3, "redstone_wall_torch", {"lit": "false", "facing": "south"})
    editor.set_block(x+1, 53, y+2, "redstone_wall_torch", {"lit": "false", "facing": "south"})
    
    # editor.set_block(0, 51, 0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    # editor.set_block(2, 51, 0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})

def not_gate(editor, x, y):
    editor.set_block(x+0, 50, y+0, "green_wool")
    editor.set_block(x+1, 50, y+0, "green_wool")
    editor.set_block(x+2, 50, y+0, "green_wool")
    editor.set_block(x+0, 50, y+1, "green_wool")
    editor.set_block(x+1, 50, y+1, "green_wool")
    editor.set_block(x+2, 50, y+1, "green_wool")
    editor.set_block(x+0, 50, y+2, "green_wool")
    editor.set_block(x+1, 50, y+2, "green_wool")
    editor.set_block(x+2, 50, y+2, "green_wool")
    editor.set_block(x+1, 51, y+1, "green_wool")

    editor.set_block(x+1, 51, y+2, "redstone_wall_torch", {"lit": "true", "facing": "south"})
 
    editor.set_block(x+1, 51, y+0, "repeater", {"facing": "north", "delay": "1", "powered": "false", "locked": "false"})
    

def or_gate(editor, x, y):
    editor.set_block(x+0, 50, y+0, "pink_wool")
    editor.set_block(x+1, 50, y+0, "pink_wool")
    editor.set_block(x+2, 50, y+0, "pink_wool")
    editor.set_block(x+0, 50, y+1, "pink_wool")
    editor.set_block(x+1, 50, y+1, "pink_wool")
    editor.set_block(x+2, 50, y+1, "pink_wool")
    editor.set_block(x+0, 50, y+2, "pink_wool")
    editor.set_block(x+1, 50, y+2, "pink_wool")
    editor.set_block(x+2, 50, y+2, "pink_wool")

    editor.set_block(x+0, 51, y+1, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+2, 51, y+1, "redstone_wire", {"power": "0", "north": "side"})
    editor.set_block(x+1, 51, y+1, "redstone_wire", {"power": "0", "north": "side"})
    
    editor.set_block(x+0, 51, y+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(x+2, 51, y+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(x+1, 51, y+2, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})

def and_gate(editor):
    editor.set_block(0, 50, 0, "yellow_wool")
    editor.set_block(1, 50, 0, "yellow_wool")
    editor.set_block(2, 50, 0, "yellow_wool")
    editor.set_block(0, 50, 1, "yellow_wool")
    editor.set_block(1, 50, 1, "yellow_wool")
    editor.set_block(2, 50, 1, "yellow_wool")
    editor.set_block(0, 51, 1, "yellow_wool")
    editor.set_block(1, 51, 1, "yellow_wool")
    editor.set_block(2, 51, 1, "yellow_wool")
    editor.set_block(0, 50, 2, "yellow_wool")
    editor.set_block(1, 50, 2, "yellow_wool")
    editor.set_block(2, 50, 2, "yellow_wool")

    editor.set_block(1, 52, 1, "redstone_wire", {"power": "15", "north": "side"})

    editor.set_block(0, 52, 1, "redstone_torch")
    editor.set_block(2, 52, 1, "redstone_torch")

    editor.set_block(1, 51, 2, "redstone_wall_torch", {"lit": "false", "facing": "south"})
    
    editor.set_block(0, 51, 0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(2, 51, 0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 arg required")
        sys.exit()
    main(sys.argv[1])