def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()

def calc_indiv_ft(dimension: str) -> int:
    l, b, h = map(int, dimension.split('x'))
    volume = l*b*h
    smallest_perimeter = min([2*(l+b), 2*(b+h), 2*(l+h)])
    return volume + smallest_perimeter

def calc_total_ft(packing_list: list) -> int:
    total_list = map(calc_indiv_ft, packing_list)
    return sum(total_list)
    
def main() -> None:
    packing_list = get_input().split()
    print(calc_total_ft(packing_list))

if __name__ == '__main__':
    main()