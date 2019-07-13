import  sys
from editor import Editor

def main(world_folder):
    """Create and run editor"""
    editor = Editor(world_folder)
    print(editor.get_block_name(1, 120, 3))
    editor.set_block(0, 51, 4, "redstone_torch")
    editor.set_block(2, 51, 4, "redstone_torch")
    editor.set_block(1, 50, 5, "redstone_wall_torch", {"lit": "true", "facing": "south"})
    editor.set_block(0, 50, 4, "white_wool")
    editor.set_block(1, 50, 4, "white_wool")
    editor.set_block(2, 50, 4, "white_wool")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 arg required")
        sys.exit()
    main(sys.argv[1])