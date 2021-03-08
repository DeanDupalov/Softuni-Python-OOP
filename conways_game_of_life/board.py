from typing import List


class Board:
    __NO_CELL = False
    __CELL = True
    __DISPLAY_VALUES = {
        __NO_CELL: '.',
        __CELL: 'O'
    }
    __board: List[List[bool]]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__board = [[self.__NO_CELL for col in range(width)] for row in range(height)]

    def next_generation(self) -> None:
        next_gen = []
        for row_idx, row in enumerate(self.__board):
            next_gen.append([])
            for col_idx, cell in enumerate(row):
                neighbors_count = self._get_neighbors(row_idx, col_idx)

                should_live = neighbors_count == 3 or (cell and neighbors_count == 2)
                next_gen[-1].append(should_live)

        self.__board = next_gen

    def _get_neighbors(self, row: int, col: int):

        neighbors = 0
        can_go_up = row - 1 >= 0
        can_go_down = row + 1 < self.height
        can_go_left = col - 1 >= 0
        can_go_right = col + 1 < self.width

        UP = LEFT = -1
        RIGHT = DOWN = 1
        if can_go_right:
            neighbors += int(self.__board[row][col + RIGHT])

        if can_go_left:
            neighbors += int(self.__board[row][col + LEFT])

        if can_go_down:
            neighbors += int(self.__board[row + DOWN][col])

        if can_go_up:
            neighbors += int(self.__board[row + UP][col])

        if can_go_up and can_go_right:
            neighbors += int(self.__board[row + UP][col + RIGHT])
        if can_go_down and can_go_right:
            neighbors += int(self.__board[row + DOWN][col + RIGHT])
        if can_go_up and can_go_left:
            neighbors += int(self.__board[row + UP][col + LEFT])
        if can_go_down and can_go_left:
            neighbors += int(self.__board[row + DOWN][col + LEFT])

        return neighbors

    def spawn_cell(self, row: int, col: int):
        self.__board[row][col] = self.__CELL

    def kill_cell(self, row: int, col: int):
        self.__board[row][col] = self.__NO_CELL

    @classmethod
    def from_string(cls, string_repr) -> 'Board':

        rows = string_repr.strip('\n \t').split('\n')
        board = Board(height=len(rows), width=len(rows[0]))

        for row_idx, row in enumerate(rows):
            for col_idx, cell_repr in enumerate(row.strip()):
                if cell_repr == cls.__DISPLAY_VALUES[cls.__CELL]:
                    board.spawn_cell(row_idx, col_idx)

        return board

    @classmethod
    def from_file(cls, file_name: str) -> 'Board':
        with open(file_name) as file:
            lines = file.readlines()
            cls.from_string('\n'.join(lines))

    def __str__(self) -> str:
        rows = [' '.join([self.__DISPLAY_VALUES[col] for col in row]) for row in self.__board]
        return '\n'.join(rows)
