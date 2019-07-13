import  sys
from editor import Editor

def main(world_folder):
    """Create and run editor"""
    editor = Editor(world_folder)
    print(editor.get_block_name(1, 120, 3))
    editor.set_block(1, 50, 3, "redstone_torch")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 arg required")
        sys.exit()
    main(sys.argv[1])