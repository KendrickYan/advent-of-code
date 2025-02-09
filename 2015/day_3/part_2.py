def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()

def count_houses_received(inp: str) -> int:
    coords = {
        'x' : 0,
        'y' : 0
    }

    visited = ['0,0']

    for direction in inp:
        match direction:
            case '>':
                coords['x'] += 1
            case '^':
                coords['y'] += 1
            case '<':
                coords['x'] -= 1
            case 'v':
                coords['y'] -= 1

        current_pos = f'{coords["x"]},{coords["y"]}'
        if current_pos not in visited:
            visited.append(current_pos)

    return visited

def main() -> None:
    ans_input = get_input()
    santa_input = ans_input[::2]
    robo_input = ans_input[1::2]
    santa_houses = count_houses_received(santa_input)
    robo_houses = count_houses_received(robo_input)
    print(len(set(santa_houses) | set(robo_houses)))

if __name__ == '__main__':
    main()