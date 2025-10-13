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

class LookAndSay:

    def __init__(self, puzzle_input: str, loop_count: int) -> None:
        self.result = self.run(puzzle_input, loop_count)

    def generate_sequence(self, old_sequence: str) -> str:
        new_sequence = []
        count = 1
        prev_num = ''
        for num in old_sequence:
            if prev_num != '':
                if num == prev_num:
                    count += 1
                else:
                    new_sequence.extend([str(count), prev_num])
                    count = 1
            prev_num = num
        else:
            # upon reaching end of given_sequence
            new_sequence.extend([str(count), prev_num])
        return ''.join(new_sequence)

    def run(self, puzzle_input: str, loop_count: int) -> str:
        new_sequence = self.generate_sequence(puzzle_input)
        for c in range(loop_count - 1):
            logging.debug(f'Loop count: {c+1}')
            new_sequence = self.generate_sequence(new_sequence)
        return new_sequence
        
if __name__ == '__main__':
    write_logs('part_2.log')
    puz_input = '1113222113'
    lns = LookAndSay(puz_input, 50)
    # print(f'Result: {lns.result}')
    print(f'Length: {len(lns.result)}')