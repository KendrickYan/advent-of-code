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

class PasswordIncrementer:

    # increase rightmost letter by 1 step until all rules are met

    def __init__(self, current_pass: str) -> None:
        self.result = self.increment_password(current_pass)
        # self.result = self.run(current_pass)

    def increment_password(self, current_pass: str) -> str:
        # takes current password, increments rightmost letter by 1 step and returns the new password
        bcurrent_pass = current_pass.encode()
        pass

    def meets_rule_1(self, password: str) -> bool:
        # Rule 1: >= 3 consecutive letters (like abc or xyz)
        pass

    def meets_rule_2(self, password: str) -> bool:
        # Rule 2: does NOT contain i, o, l
        pass

    def meets_rule_3(self, password: str) -> bool:
        # Rule 3: >= 2 different pairs (like aa AND bb)
        pass

    def run(self, current_pass: str) -> str:
        while True:
            trial_password = self.increment_password(current_pass)
            if self.meets_rule_1 is True or self.meets_rule_2 is True or self.meets_rule_3 is True:
                return trial_password

if __name__ == '__main__':
    write_logs('part_1.log')
    puzzle_input = 'cqjxjnds'
    pass_inc = PasswordIncrementer(puzzle_input)
    print(f'Next password: {pass_inc.result}')