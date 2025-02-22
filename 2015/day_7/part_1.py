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

    return wire_dct, instruction_lines

def connect_wires(wire_dct: dict, instruction_line: str) -> dict:
    '''Connect the wires according to the given instruction and add them to the wire_dct.
    
    Returns the updated wire_dct with the new assigned wires.'''

    words_list = instruction_line.split(' ')
    wire_keys = wire_dct.keys()

    logging.debug(f'Connecting {instruction_line}')
    if len(words_list) == 5:
        
        output_wire = words_list[4]
        if words_list[0] in wire_keys:
            wire_1 = wire_dct[words_list[0]]
        else:
            wire_1 = int(words_list[0])
            
        if words_list[2] in wire_keys:
            wire_2 = wire_dct[words_list[2]]
        else:
            wire_2 = int(words_list[2])
        
        match words_list[1]:
            case 'AND':
                value = wire_1 & wire_2
            case 'OR':
                value = wire_1 | wire_2
            case 'RSHIFT':
                value = wire_1 >> wire_2
            case 'LSHIFT':
                value = wire_1 << wire_2        
        
    elif len(words_list) == 4:
        if words_list[0] == 'NOT':
            output_wire = words_list[3]
            value = ~ wire_dct[words_list[1]]

    elif len(words_list) == 3:
        output_wire = words_list[2]
        value = wire_dct[words_list[0]]
    
    # Connect wire and update the wire_dct
    wire_dct[output_wire] = value
    # logging.debug(f'UPDATED wire_dct: {wire_dct}')

    return wire_dct

def find_lines(wire_dct: dict, instruction_lines: list[str]) -> dict:
    '''Find all of the possible wires given the wire_dct.
    
    Returns the most updated wire_dct'''

    ignored_lines = []
    for line in instruction_lines:
        do_connection = False
        wire_keys = wire_dct.keys()
        words_list = line.split(' ')

        # If any of the input wires are not in wire_keys, ignore the line.
        if len(words_list) == 5:

            if not all(word.isdigit() or word in wire_keys for word in (words_list[0], words_list[2])):
                ignored_lines.append(line)
                # logging.debug(f'1) Ignoring line: {line}')
                continue
            
        elif len(words_list) == 4:
            # So lines like 'NOT cn -> co'

            if words_list[1] not in wire_keys:
                ignored_lines.append(line)
                # logging.debug(f'2) Ignoring line: {line}')
                continue

        elif len(words_list) == 3:
            # So lines like 'lx -> a'
            if words_list[0] not in wire_keys:
                ignored_lines.append(line)
                continue
        
        else:
            print(f'WHAT IS THIS: {line}')
            continue

        wire_dct = connect_wires(wire_dct, line)

    # Keep recursively calling the function until no lines are ignored.
    if len(ignored_lines) != 0:
        logging.debug(f'Some lines are still ignored. Going through instructions with updated wire_dct now.')
        wire_dct = find_lines(wire_dct, ignored_lines)

    return wire_dct

def main() -> None:
    # write_logs('part_1.log')
    instruction_lines = get_input().splitlines()
    wire_dct, instruction_lines = provide_signals(instruction_lines)
    wire_dct = find_lines(wire_dct, instruction_lines)
    print(f'Value of a: {wire_dct['a']}')

if __name__ == '__main__':
    main()