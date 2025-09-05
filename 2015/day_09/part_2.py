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
    
class FindLongestRoute:
    '''
    Takes a list of distances.
    
    Returns the distance of the longest route between any 2 locations.
    '''

    def __init__(self, distances_list: list[str]) -> None:
        self.distances_data = self.parse_input(distances_list)
        logging.debug(f'self.distances_data: {self.distances_data}')
        self.found_routes = []

        self.run()
        self.result = max(self.found_routes) if len(self.found_routes) > 0 else 'NOT FOUND'

    def parse_input(self, distances_list: list[str]) -> list[tuple[str, str, int]]:
        '''Parses the input into a list of tuples. Sort the list in order of longest distance'''
        distances_data = []
        for distance in distances_list:
            distance_line = distance.split(' ')
            distances_data.append((distance_line[0], distance_line[2], int(distance_line[-1])))

        # Sort the list in order of longest distance
        distances_data = sorted(distances_data, key=lambda x: x[2], reverse=True)
        return distances_data

    def start_route(self, starting_route_index: int) -> None:
        '''Starts the route-finding algorithm. Takes the starting route as an index of self.distances_data'''

        # Since it is the starting city
        if self.current_city == '':

            # Take the first distance as the starting cities.
            starting_route = self.distances_data[starting_route_index]
            self.route_distance += starting_route[2]
            logging.debug(f'starting_route: {starting_route}')

            remaining_routes = self.distances_data.copy()

            # Remove that route
            remaining_routes.remove(starting_route)

            # Find the next longest distance with a common city
            for route in remaining_routes:
                if len(set(starting_route).intersection(route)) == 1:

                    common_city = set(starting_route).intersection(route)

                    # The first city in the route is the one that is not the common city in the next route (actually next distance, poor naming convention here)
                    first_city = starting_route[0] if starting_route[1] in common_city else starting_route[1]
                    
                    # Add the starting cities to the order
                    self.route_order.extend([first_city, list(common_city)[0]])

                    # Set the UNCOMMON city to self.current_city
                    self.current_city = route[0] if route[0] != common_city else route[1]

                    # Add the current city to the order
                    self.route_order.append(self.current_city)

                    # Tally the distance of the entire route
                    self.route_distance += route[2]

                    logging.debug(f'intersection: {common_city}, route: {route}, self.current_city: {self.current_city}, self.route_distance: {self.route_distance}')

                    # Remove that route
                    remaining_routes.remove(route)

                    break # find the next route with common city

    def go_next_city(self) -> int:
        '''From the starting route, go to the next nearest city until all cities are visted or stuck at a dead end.
        
        Returns exit code. 0 for no error. 1 for reaching dead end.'''

        exit_code = 0

        remaining_routes = self.distances_data.copy()

        while len(remaining_routes) > 0:

            # logging.debug(f'* remaining_routes: {remaining_routes}')
            logging.debug(f'** self.route_order: {self.route_order}')
            
            for route in remaining_routes:
                # logging.debug(f'Checking {route} for {self.current_city}')

                if self.current_city in route and len(set(self.route_order).intersection(route)) == 1:

                    # logging.debug(f'intersection: {set(self.route_order).intersection(route)}')

                    # Set the new self.current_city
                    self.current_city = route[0] if route[0] != self.current_city else route[1]

                    # Add the current city to the order
                    self.route_order.append(self.current_city)

                    # Tally the distance of the entire route
                    self.route_distance += route[2]

                    logging.debug(f'route: {route}, self.current_city: {self.current_city}, self.route_distance: {self.route_distance}')
                    
                    # Remove that route
                    remaining_routes.remove(route)

                    break
                
            else:
                logging.info(f'Failed route: {self.route_order}')
                exit_code = 1
                break # out of the for loop if route is not found

        return exit_code

    def run(self) -> None:
        for i in range(len(self.distances_data)):

            # Reset variables
            self.current_city = ''
            self.route_distance = 0
            self.route_order = []
            
            self.start_route(i)

            if self.go_next_city() == 0:
                print(f'Successful route: {self.route_order}, total distance: {self.route_distance}')

def main() -> None:
    write_logs('part_2.log')
    distances_list = get_input().splitlines()
    longest_route = FindLongestRoute(distances_list)
    print(f'Answer: {longest_route.result}')    

if __name__ == '__main__':
    # 863 is too high
    main()