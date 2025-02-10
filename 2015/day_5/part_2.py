def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def count_nice_strings(inp: str) -> int:
    con_1, con_2 = False, False
    for index, letter in enumerate(inp):
        if index == len(inp) - 1:
            break

        # condition 1
        new_inp = inp.replace(f'{letter}{inp[index + 1]}', '')
        if len(new_inp) + 2 != len(inp):
            con_1 = True

        if index == len(inp) - 2:
            break

        # condition 2
        if letter == inp[index + 2]:
            con_2 = True

    return int(con_1 and con_2)

def main() -> None:
    ans_input = get_input().split()
    bool_list = list(map(count_nice_strings, ans_input))
    print(sum(bool_list))

if __name__ == '__main__':
    main()