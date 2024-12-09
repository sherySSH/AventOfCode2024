from dataclasses import dataclass

@dataclass
class Position:
    x : int
    y : int

def read_file(fpath : str) -> list:
    with open(fpath) as f:
        content : str = f.read()

    content = content.split("\n")
    content = [list(line) for line in content]
    return content

def search_right(grid : list, position : tuple, expected_word : str, searched_word : str):
    print(position)
    searched_letter = grid[position.y][position.x]
    expected_letter = expected_word[len(searched_word)] 
    searched_word = searched_word + searched_letter

    position.x = position.x + 1

    if searched_letter == expected_letter and expected_word == searched_word:
        return 1
    elif searched_letter == expected_letter and expected_word != searched_word:
        return search_right(grid, position, expected_word, searched_word)
    else:
        return 0


if __name__ == "__main__":

    grid = read_file("input.txt")
    result = search_right(grid, Position(x=6, y=0), 'XMAS', '')
    print(result)