import os
import logging, logging.handlers

def write_logs(filename: str = 'general.log', log_level: int = logging.DEBUG) -> None:
    """
    Create a logs folder if it does not already exist. Write simple logs into a file in the logs folder.

    Parameter
    ---------
    filename : str, default: general.log
        The name of the log file, with .log extension. By default, the log file will be written in ./logs/general.log.

    log_level : int, default: logging.debug
        The lowest level of logs that will be saved. By default, log at debug level.

    Returns
    -------
    None

    Other Parameters
    ----------------
    imported_module : os
        Used to check if logs folder exists and creates it if it does not.

    imported_module : logging
        Used to write and configure the log file.

    imported_module : logging.handlers
        Used to handle rotation of log files. logging.handlers.RotatingFileHandler is set to 10MB, 5 files.

    Notes
    -----
    Just using a simple basicConfig to write the logs. Planning to use more personalised logs in the future.
    """

    if not os.path.exists('logs'):
        os.makedirs('logs', exist_ok=True)
    logging.basicConfig(filename='logs/' + filename, filemode='w', format='[%(asctime)s] %(levelname)s | %(name)s - %(message)s', level=log_level, datefmt='%Y-%m-%d %H:%M:%S')
    logging.handlers.RotatingFileHandler(filename='logs/' + filename, maxBytes=10*1024*1024, backupCount=5) # 10MB, 5 files max

def get_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()
    
def generate_wires() -> dict:
    '''Generates the dictionary that will hold the bits (value) represented by the letters (key)'''
    dct = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        dct[letter] = 0
    return dct
    
def provide_signals(instruction_lines: list[str], wire_dct: dict) -> list:
    '''Takes instructions and assign values to wires that have already been provided, then remove that instruction.
    
    eg. "0 -> c" means assign "c" : 0 in the wire dictionary.
    
    Returns the new instructions.'''
    for line in instruction_lines:
        line.split(' ')
        logging.debug(f'line: {line}')

def main() -> None:
    write_logs('part_1.log')
    instruction_lines = get_input().splitlines()
    wire_dct = generate_wires()
    # logging.debug(wire_dct)
    provide_signals(instruction_lines, wire_dct)

if __name__ == '__main__':
    main()