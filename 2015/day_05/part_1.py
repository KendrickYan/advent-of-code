def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def count_nice_strings(inp: str) -> int:
    con_1, con_2, con_3 = False, False, True
    vowel_counter = 0

    for index, letter in enumerate(inp):

        # condition 1: count number of vowels
        if letter in 'aeiou':
            vowel_counter += 1

        # condition 2: check consecutive repeating letter
        if index >= len(inp) - 1:
            break
        
        if letter == inp[index + 1]:
            con_2 = True

        # condition 3: does not contain given letter pairs
        if letter + inp[index + 1] in ['ab', 'cd', 'pq', 'xy']:
            con_3 = False
    
    if vowel_counter >= 3:
        con_1 = True

    return int(con_1 and con_2 and con_3)

def main() -> None:
    ans_input = get_input().split()
    bool_list = list(map(count_nice_strings, ans_input))
    print(sum(bool_list))

if __name__ == '__main__':
    main()