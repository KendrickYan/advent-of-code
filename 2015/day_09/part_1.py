# Travelling Salesman Problem, except Santa does not return back to starting city.
# Also known as Shortest Hamiltonian path variant.

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
        self.distances_data = self.parse_data(distances_list)
        self.total_num_cities = len(self.distances_data.keys())
        logging.debug(f'self.distances_data:\n{self.distances_data}')
        self.all_paths = []
        self.current_path = []
        self.next_city = ''
        self.cost = 0
        self.path_taken = [] 
        self.result = 0

        self.path_taken, self.result = self.run()

    def parse_data(self, data: list[str]) -> dict[str, list[tuple[str, int]]]:
        parsed_data = {}
        for line in data:
            sep_words = line.split(' ')
            city_1 = sep_words[0]
            city_2 = sep_words[2]
            dist = int(sep_words[-1])
            key_list = parsed_data.keys()

            if city_1 in key_list:
                parsed_data[city_1].append((city_2, dist))
            else:
                parsed_data[city_1] = [(city_2, dist)]

            if city_2 in key_list:
                parsed_data[city_2].append((city_1, dist))
            else:
                parsed_data[city_2] = [(city_1, dist)]

        parsed_data = {k : sorted(v, key=lambda x: x[1]) for k, v in parsed_data.items()}
        return parsed_data

    def greedy_path_from(self, current_city: str) -> int | None:
        next_closest_city = ''
        for value in self.distances_data[current_city]:
            if value[0] in self.current_path:
                continue
            next_closest_city = value[0]
            self.cost += value[1]
            self.current_path.append(next_closest_city)
            return self.greedy_path_from(next_closest_city)
        else:
            return 0

    def run(self) -> tuple[list[str], int]:
        for starting_city in self.distances_data.keys():
            self.current_path.append(starting_city)
            ret = self.greedy_path_from(starting_city)
            if ret is not None and ret == 0:
                logging.debug(f'Completed path: {self.current_path}, Cost: {self.cost}')
                self.all_paths.append((self.current_path, self.cost))
                self.current_path = []
                self.cost = 0
                continue
        sorted_paths = sorted(self.all_paths, key=lambda x: x[1])
        return sorted_paths[0]

def main() -> None:
    write_logs('part_1.log')
    distances_list = get_input().splitlines()
    shortest_route = FindShortestRoute(distances_list)
    print(f'Answer: {shortest_route.result}')
    print(f'Path taken: {shortest_route.path_taken}')

if __name__ == '__main__':
    main()