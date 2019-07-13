import  sys
from editor import Editor

def main(world_folder):
    """Create and run editor"""
    editor = Editor(world_folder)
    print(editor.get_block_name(1, 120, 3))
    and_gate(editor)
    or_gate(editor, 10, 0)
    
def or_gate(editor, x, y):
    editor.set_block(x+0, 50, y+3, "pink_wool")
    editor.set_block(x+1, 50, y+3, "pink_wool")
    editor.set_block(x+2, 50, y+3, "pink_wool")
    editor.set_block(x+0, 50, y+4, "pink_wool")
    editor.set_block(x+1, 50, y+4, "pink_wool")
    editor.set_block(x+2, 50, y+4, "pink_wool")
    editor.set_block(x+0, 50, y+5, "pink_wool")
    editor.set_block(x+1, 50, y+5, "pink_wool")
    editor.set_block(x+2, 50, y+5, "pink_wool")
    editor.set_block(x+0, 50, y+6, "pink_wool")
    editor.set_block(x+1, 50, y+6, "pink_wool")
    editor.set_block(x+2, 50, y+6, "pink_wool")

    editor.set_block(x+0, 51, y+4, "redstone_wire", {"power": "0"})
    editor.set_block(x+2, 51, y+4, "redstone_wire", {"power": "0"})
    editor.set_block(x+1, 51, y+4, "redstone_wire", {"power": "0"})
    editor.set_block(x+1, 51, y+5, "redstone_wire", {"power": "0"})
    
    editor.set_block(x+0, 51, y+3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(x+2, 51, y+3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(x+1, 51, y+6, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})

def and_gate(editor):
    editor.set_block(0, 50, 3, "yellow_wool")
    editor.set_block(1, 50, 3, "yellow_wool")
    editor.set_block(2, 50, 3, "yellow_wool")
    editor.set_block(0, 50, 4, "yellow_wool")
    editor.set_block(1, 50, 4, "yellow_wool")
    editor.set_block(2, 50, 4, "yellow_wool")
    editor.set_block(0, 51, 4, "yellow_wool")
    editor.set_block(1, 51, 4, "yellow_wool")
    editor.set_block(2, 51, 4, "yellow_wool")
    editor.set_block(0, 50, 5, "yellow_wool")
    editor.set_block(1, 50, 5, "yellow_wool")
    editor.set_block(2, 50, 5, "yellow_wool")
    editor.set_block(0, 50, 6, "yellow_wool")
    editor.set_block(1, 50, 6, "yellow_wool")
    editor.set_block(2, 50, 6, "yellow_wool")

    editor.set_block(1, 52, 4, "redstone_wire", {"power": "15"})

    editor.set_block(0, 52, 4, "redstone_torch")
    editor.set_block(2, 52, 4, "redstone_torch")

    editor.set_block(1, 51, 5, "redstone_wall_torch", {"lit": "false", "facing": "south"})
    
    editor.set_block(0, 51, 3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(2, 51, 3, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})
    editor.set_block(1, 51, 6, "repeater", {"facing": "north", "delay": "1", "powered": "flase", "locked": "false"})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 arg required")
        sys.exit()
    main(sys.argv[1])