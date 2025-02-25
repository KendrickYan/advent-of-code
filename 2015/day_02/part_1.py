def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def calc_indiv_sqft(dimension: str) -> int:
    l, b, h = map(int, dimension.split('x'))
    min_wrapper = 2*l*b + 2*b*h + 2*l*h
    slack = min([l*b, b*h, l*h])
    return min_wrapper + slack

def calc_total_sqft(packing_list: list) -> int:
    total_list = map(calc_indiv_sqft, packing_list)
    return sum(total_list)
    
def main() -> None:
    packing_list = get_input().split()
    print(calc_total_sqft(packing_list))

if __name__ == '__main__':
    main()