import hashlib

def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def md5_hash(to_be_hashed: str) -> str:
    return hashlib.md5(to_be_hashed.encode()).hexdigest()

def main() -> None:
    num = 0
    while True:
        hash = md5_hash(string := f'ckczppom{num}')
        if hash[:5] == '00000':
            print('md5 hash:', hash)
            print('string:', string)
            break
        num += 1

if __name__ == '__main__':
    main()