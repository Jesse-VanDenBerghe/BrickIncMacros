import sys
import os

# Add the parent directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ochestrator import wait, WAIT_LONG
from utils.adb import tapAt, createFullScreenShot
from utils.image import areColorsMatching, getColorAtPixelFromImage, draw_centered_circle
from PIL import Image


class GridOfTruth:
    def __init__(self, start, end, traps, special_coordinates):
        self.start = start
        self.end = end
        self.traps = traps
        self.special_coordinates = special_coordinates

    def print(self) -> str:
        print("\n--- 5x5 Grid ---")
        for y in range(5):
            row_chars = []
            for x in range(5):
                pos = (x, y)
                if pos == self.start:
                    row_chars.append(" S ")
                elif pos == self.end:
                    row_chars.append(" E ")
                elif pos in self.traps:
                    row_chars.append(" -2")
                elif pos in self.special_coordinates:
                    row_chars.append(f" {self.special_coordinates[pos]:02d}")
                else:
                    row_chars.append(" --")

            print("".join(row_chars))
        print("------------------------\n")



def find_longest_path(start, end, traps, grid_size, special_coordinates):

    def traverse_path(current, goal, traps, visited):
        if current == goal:
            return [goal]

        possible_paths = []

        for neighbour in get_neighbours(current):
            if is_valid(neighbour, traps, visited):
                result = traverse_path(
                        neighbour,
                        goal,
                        traps,
                        visited | {neighbour}
                        )

                if result is not None:
                    possible_paths.append([current] + result)

        if not possible_paths:
            return None

        return max(possible_paths, key=calculate_path_score)

    def calculate_path_score(path):
        return sum(special_coordinates.get(coord, 1) for coord in path)

    def get_neighbours(pos):
        x, y = pos
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def is_valid(pos, traps, visited):
        x, y = pos
        return (
                0 <= x < grid_size and
                0 <= y < grid_size and
                pos not in visited
                )

    path_found = traverse_path(start, end, set(traps), {start})
    return (calculate_path_score(path_found) , path_found)


# Creates the 5 possible paths
def find_best_path_of_truth():
    CREATE_COORDINATES_IN_DIALOG = 639, 1593
    CREATE_COORDINATES_IN_OVERVIEW = 1082, 1739

    # First creation starts on dialog
    tapAt(*CREATE_COORDINATES_IN_DIALOG)
    wait(WAIT_LONG)

    for i in range(4):
        tapAt(*CREATE_COORDINATES_IN_OVERVIEW)
        wait()
        tapAt(*CREATE_COORDINATES_IN_DIALOG)
        wait(WAIT_LONG)

    wait(2)

    return find_best_path_of_truth_in_options()


def find_best_path_of_truth_in_options():
    results = []

    for i in range(5):
        select_option(i)
        results.append(calculate_path_of_thruth())

    print()
    print(results)

    index, (value, path) = max(enumerate(results), key=lambda x: x[1][0])

    return (index, value, path)


def get_option_coordinate(index: int):
    X_VALUE = 1195
    OPTION_1_Y = 875
    OPTION_5_Y = 1515
    y_delta = (OPTION_5_Y - OPTION_1_Y) / 4
    return (X_VALUE, OPTION_1_Y + (int(y_delta) * index))


def select_option(index: int):
    (x, y) = get_option_coordinate(index)
    tapAt(x, y)
    wait(WAIT_LONG)

TOP_LEFT = 255, 825
BOTTOM_RIGHT = 915, 1485


def calculate_path_of_thruth():
    imageUrl = "path_of_thruth_scan.png"
    createFullScreenShot(imageUrl)
    screenshotImage = Image.open(imageUrl).convert('RGB')
    grid = scan_grid(screenshotImage, TOP_LEFT, BOTTOM_RIGHT, 5)
    grid.print()
    path_of_truth = find_longest_path(grid.start, grid.end, grid.traps, 5, grid.special_coordinates)
    print(path_of_truth)
    return path_of_truth


def scan_grid(image: Image, top_left, bottom_right, grid_size=5) -> GridOfTruth:
    start = None
    end = None
    traps = []
    special_coordinates = {}

    for y in range(grid_size):
        for x in range(grid_size):
            coord = get_grid_coordinate(x, y)
            relativeCoord = (x, y)
            if is_start_tile(image, coord):
                start = relativeCoord
            elif is_end_tile(image, coord):
                end = relativeCoord
            elif is_trap_tile(image, coord):
                traps.append(relativeCoord)
                special_coordinates[relativeCoord] = -2
            else:
                special_coordinates[relativeCoord] = get_tile_value(image, coord)

    return GridOfTruth(
        start,
        end,
        traps,
        special_coordinates
    )


def traverse_path(path):
    START_COORD = 1082, 1864
    CONFIRM_COORD = 877, 1704

    tapAt(*START_COORD)
    wait(WAIT_LONG)

    tapAt(*CONFIRM_COORD)
    wait(WAIT_LONG)

    for relativeCoord in path:
        (x, y) = get_grid_coordinate(*relativeCoord)
        tapAt(x, y)
        wait()

    tapAt(*CONFIRM_COORD)
    wait()

def get_grid_coordinate(x, y):
    TOP_LEFT = 255, 825
    BOTTOM_RIGHT = 915, 1485
    left, top = TOP_LEFT
    right, bottom = BOTTOM_RIGHT
    x_jumps = (right - left) / 4
    y_jumps = (bottom - top) / 4
    coord = (left + (x * x_jumps), top + (y * y_jumps))
    return coord


def is_start_tile(image, coord) -> bool:
    START_COLOR = 69, 114, 140
    x, y = coord
    pixel_color = getColorAtPixelFromImage(image, x, y)
    return areColorsMatching(pixel_color, START_COLOR, 32)


def is_end_tile(image, coord) -> bool:
    END_COLOR = 128, 79, 205
    x, y = coord
    pixel_color = getColorAtPixelFromImage(image, x, y)
    return areColorsMatching(pixel_color, END_COLOR)


def is_trap_tile(image, coord) -> bool:
    TRAP_COLOR = 103, 45, 40
    x, y = coord
    pixel_color = getColorAtPixelFromImage(image, x, y)
    return areColorsMatching(pixel_color, TRAP_COLOR)


def get_tile_value(image, coord) -> int:
    PATHCOLORS = {
        (124, 118, 99): 1,  # Common
        (0, 148, 19): 2,  # Rare
        (0, 99, 181): 4,  # Epic
        (206, 175, 0): 10,  # Legendary
    }
    x, y = coord
    pixel_color = getColorAtPixelFromImage(image, x, y)
    return PATHCOLORS.get(pixel_color, -2)


def print_grid(grid_size, path, traps):
    path_map = {pos: i for i, pos in enumerate(path)} if path else {}
    traps_set = set(traps)

    print(f"\n--- 5x5 Grid (Longest Path: {len(path)} steps) ---")
    for y in range(grid_size):
        row_chars = []
        for x in range(grid_size):
            pos = (x, y)

            if pos in traps_set:
                row_chars.append(" XX")
            elif pos in path_map:
                row_chars.append(f" {path_map[pos]:02d}")
            else:
                row_chars.append(" --")

        print("".join(row_chars))
    print("----------------------------------------------\n")


def path_of_truth(times: int):
    CONFIRM_AFTER_RUN_COORD = 636, 1766

    for i in range(times):
        (index, value, path) = find_best_path_of_truth()
        select_option(index)
        traverse_path(path)
        wait(15)
        tapAt(*CONFIRM_AFTER_RUN_COORD)


path_of_truth(3)
