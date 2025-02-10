def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()

def generate_lights() -> dict:
    lights = {}
    for i in range(1000):
        for j in range(1000):
            lights[f'{i},{j}'] = 0
    return lights

def toggle_lights(coords: str, action: str, lights: dict) -> dict:
    match action:
        case 'toggle':
            lights[coords] += 2
        case 'on':
            lights[coords] += 1
        case 'off':
            if lights[coords] > 0:
                lights[coords] -= 1
    return lights

def switch_lights(instruction: str, lights: dict) -> dict:
    instruction = instruction.split()
    coords_2 = instruction[-1]
    if 'toggle' in instruction:
        coords_1 = instruction[1]
        action = 'toggle'
    elif 'on' in instruction:
        coords_1 = instruction[2]
        action = 'on'
    elif 'off' in instruction:
        coords_1 = instruction[2]
        action = 'off'

    for x in range(int(coords_1.split(',')[0]), int(coords_2.split(',')[0]) + 1):
        for y in range(int(coords_1.split(',')[1]), int(coords_2.split(',')[1]) + 1):
            coords = f'{x},{y}'
            lights = toggle_lights(coords, action, lights)

    return lights

def main() -> None:
    lights = generate_lights()
    puzzle_input = get_input().splitlines()
    for line in puzzle_input:
        lights = switch_lights(line, lights)
    print(sum(lights.values()))

if __name__ == '__main__':
    main()