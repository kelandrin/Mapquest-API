#Matthew Littman UCI ID: 38916993
import mapquest_api
import output_generator
from output_generator import list_output_generators     # list_output_generators is the class used to make the list of output_generators

def main():
    # collecting inputs
    location_num = get_num()
    locations_list = get_list_of_values(location_num)
    input_num = get_num()
    input_list = get_list_of_values(input_num)

    # building direction url
    direction_url = mapquest_api.build_direction_url(locations_list)

    # getting data from MapQuest route as a dictionary
    route_dict = mapquest_api.get_direction_data(direction_url)
    check_for_NO_ROUTE_FOUND(route_dict)

    # building elevation url
    elevation_url = mapquest_api.build_elevation_url(route_dict)

    # getting data from MapQuest elevation and adding to current route_dict
    route_dict = mapquest_api.get_elevation_data(elevation_url,route_dict)

    # uses generators to create output
    generator_list = list_output_generators.make_list_output_generators(list_output_generators,input_list)
    output_generator.generate_and_print(generator_list,route_dict)

    # print copyright message
    _print_copyright()

def _read_query() -> str:
    return input()

def get_num() -> int:
    number = int(_read_query())
    return number

def get_list_of_values(number_of_values:int) -> list:
    # takes in a number x and asks user x times for input and makes a list out of those inputs

    list_of_values = []
    for i in range(number_of_values):
        value = _read_query()
        list_of_values.append(value)
    return list_of_values

def check_for_NO_ROUTE_FOUND(route_dict:dict)-> None:
    # checks to see if no route is possible given the destinations or if the place entered doesn't exist

    if _check_if_path_exists(route_dict) == False or _check_if_place_exists(route_dict) == False:
        print('\n' + 'NO ROUTE FOUND', end = '')
        quit()

def _check_if_path_exists(route_dict:dict) -> bool:
    error_code = route_dict['routeError']['errorCode']
    if error_code == 2:
        return False
    else:
        return True

def _check_if_place_exists(route_dict:dict) -> bool:
    steps_obj = output_generator.get_steps(route_dict)
    if steps_obj.route[-1] == 'Welcome to US.':
        return False
    else:
        output_generator.steps.clear_route(output_generator.steps)
        return True

def _print_copyright()-> None:
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')

if __name__ == '__main__':
    main()

'''
3
Huntington Beach, CA
1111 Figueroa St, Los Angeles, CA
3799 S Las Vegas Blvd, Las Vegas, NV
5
LATLONG
STEPS
TOTALTIME
TOTALDISTANCE
ELEVATION'''