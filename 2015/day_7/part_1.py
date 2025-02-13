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

def provide_signals(instruction_lines: list[str]) -> dict:
    '''Takes instructions and assign values to wires that have already been provided, then remove that instruction.
    
    eg. "0 -> c" means assign "c" : 0 in the wire dictionary.
    
    Returns the wire instructions.'''
    wire_dct = {}

    for line in instruction_lines:
        words_list = line.split(' ')

        # Take words_lists that provide constants to wires
        if len(words_list) == 3 and words_list[0].isdigit():
            wire_dct[words_list[2]] = int(words_list[0])

            # Remove the instruction
            instruction_lines.remove(line)
            
    logging.debug(f'New instruction_lines:\n{instruction_lines}')

    return wire_dct, instruction_lines

def main() -> None:
    write_logs('part_1.log')
    instruction_lines = get_input().splitlines()
    logging.debug(f'New instruction_lines:\n{instruction_lines}')
    wire_dct, instruction_lines = provide_signals(instruction_lines)
    logging.debug(wire_dct)

if __name__ == '__main__':
    main()