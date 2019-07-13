import  sys
from editor import Editor

def main(world_folder):
    """Create and run editor"""
    editor = Editor(world_folder)
    print(editor.get_block_name(1, 120, 3))
    and_gate(editor)
    or_gate(editor, 10, 0)
    not_gate(editor, 15, 0)
    

def not_gate(editor, x, y):
    editor.set_block(x+0, 50, y+0, "green_wool")
    editor.set_block(x+1, 50, y+0, "green_wool")
    

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
    editor.set_block(x+1, 51, y+0, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})

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