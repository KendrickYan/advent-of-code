def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def count_floors(instr: str) -> int:
    current_floor = 0
    for char in instr:
        match char:
            case '(':
                current_floor += 1
            case ')':
                current_floor -= 1

    return current_floor

def main() -> None:
    instructions = get_input()
    floor = count_floors(instructions)
    print(floor)

if __name__ == '__main__':
    main()