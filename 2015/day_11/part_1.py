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
        self.result = self.run(current_pass)

    def increment_password(self, current_pass: str, pos: int = -1) -> str:
        # takes current password, increments rightmost letter by 1 step and returns the new password
        chr_to_incr = current_pass[pos]

        if chr_to_incr == 'z':
            new_chr = 'a'
            current_pass = self.increment_password(current_pass, pos-1)
        else:
            new_chr = chr(ord(chr_to_incr) + 1)

        trial_pass = current_pass[0:pos] + new_chr + current_pass[pos:-1]
        
        return trial_pass

    def meets_rule_1(self, password: str) -> bool:
        # Rule 1: >= 3 consecutive letters (like abc or xyz)
        bpassword = password.encode()
        for i, byte in enumerate(bpassword):
            # rule is not met when 2nd last letter is reached
            if i >= len(bpassword) - 2:
                return False
            
            if byte + 1 == bpassword[i+1] and byte + 2 == bpassword[i+2]:
                return True
        else:
            # should never come here
            return False

    def meets_rule_2(self, password: str) -> bool:
        # Rule 2: does NOT contain i, o, l
        for char in password:
            if char in ['i', 'o', 'l']:
                return False
        else:
            return True

    def meets_rule_3(self, password: str) -> bool:
        # Rule 3: >= 2 different pairs (like aa AND bb)
        pair_list = []
        for i, char in enumerate(password):
            # rule is not met when last letter is reached
            if i >= len(password) - 1:
                break
            
            if char == password[i+1] and char not in pair_list:
                pair_list.append(char)
        
        if len(pair_list) >= 2:
            return True
        # should never come here
        return False

    def run(self, current_pass: str) -> str:
        trial_password = current_pass
        while True:
            trial_password = self.increment_password(trial_password)
            if self.meets_rule_1(trial_password) and self.meets_rule_2(trial_password) and self.meets_rule_3(trial_password):
                return trial_password

if __name__ == '__main__':
    write_logs('part_1.log')
    puzzle_input = 'cqjxjnds'
    pass_inc = PasswordIncrementer(puzzle_input)
    print(f'Next password: {pass_inc.result}')
    pass_inc = PasswordIncrementer('cqjxxyzz')
    print(f'Part 2 password: {pass_inc.result}')