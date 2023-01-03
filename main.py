#!C:\Users\ernie\OneDrive\Repos\RogueLikeTutorial\venv\Scripts\python.exe
import math
import random

import tcod


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "./resources/dejavu10x10_gs_tc.png",
        32,
        8,
        tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order='F')
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == '__main__':
    main()