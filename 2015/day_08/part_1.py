import os
import logging, logging.handlers
import ast

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
    
class SubtractStringLengths:
    '''
    Takes a list of strings. Subtracts the number of characters of code for string literals with the number of characters in memory for the value of the strings.
    
    Returns the total difference.
    '''

    def __init__(self, strings_list: list[str]) -> None:
        self.strings_list = strings_list
        self.total_literal = 0
        self.total_memory = 0
        self.run()
        self.difference = self.total_literal - self.total_memory

    def count_literal(self, string: str) -> None:
        '''Counts characters as they appear in source code.'''
        self.total_literal += len(string)

    def count_memory(self, string: str) -> None:
        '''Counts characters as they are stored in memory.'''
        self.total_memory += len(ast.literal_eval(string))

    def run(self) -> None:
        for string in self.strings_list:
            self.count_literal(string)
            self.count_memory(string)

def main() -> None:
    # write_logs('part_1.log')
    puzzle_input = get_input().splitlines()
    result = SubtractStringLengths(puzzle_input)
    print(result.difference)

if __name__ == '__main__':
    main()