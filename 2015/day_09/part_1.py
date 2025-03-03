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
    
class FindShortestRoute:
    '''
    Takes a list of distances.
    
    Returns the distance of the shortest route between any 2 locations.
    '''

    def __init__(self, distances_list: list[str]) -> None:

        self.distances_dct = self.parse_input(distances_list)
        self.result = self.run()

    def parse_input(self, distances_list: list[str]) -> dict[tuple[str, str], int]:
        '''Parses the input into a dictionary.'''
        distances_dct = {}
        for distance in distances_list:
            distance_line = distance.split(' ')
            distances_dct[(distance_line[0], distance_line[2])] = distance_line[-1]
        return distances_dct

    def find_shortest_between_two(self) -> int:
        '''Returns the shortest distance between any two cities.'''
        current_shortest = float('inf')
        for distance in self.distances_list:
            distance = int(distance.split(' ')[-1])
            if distance < current_shortest:
                current_shortest = distance
        return current_shortest

    def run(self) -> int:
        shortest_distance = self.find_shortest_between_two()
        return shortest_distance

def main() -> None:
    write_logs('part_1.log')
    distances_list = get_input().splitlines()
    shortest_route = FindShortestRoute(distances_list)
    print(shortest_route.result)    

if __name__ == '__main__':
    main()