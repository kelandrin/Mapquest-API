#Matthew Littman UCI ID: 38916993

class latlong:
    # contains information about the latitudes and longitudes of its objects
    # as well as direction (North, South, East, or West)

    _lat = 0
    _lng = 0
    _lat_direction = ''
    _lng_direction = ''

    def set_lat_direction(self,lat):
        if lat < 0:
            self._lat_direction = 'S'
        elif lat > 0:
            self._lat_direction = 'N'
        else:
            self._lat = 0

    def set_lng_direction(self,lng):
        if lng < 0:
            self._lng_direction = 'W'
        elif lng > 0:
            self._lng_direction = 'E'
        else:
            self._lng = 0

    def as_iterated_list(self,latlong_list:list):
        # takes in list of latlong objects and prints each on its own line with format:
        # latitude + (N or S) _ longitude + (E or W)

        print('LATLONG')
        for latlong_obj in latlong_list:
           print(str(abs(latlong_obj._lat)) + latlong_obj._lat_direction + ' ' + str(abs(latlong_obj._lng)) + latlong_obj._lng_direction)

class elevation:
    # contains information about the height of the given location

    elevation = 0

    def set_elevation(self,height):
        self.elevation = round(height)

    def as_iterated_list(self,elevation_list:list):
        # takes in a list of elevation objects and prints each height on its own line

        print('ELEVATION')
        for object in elevation_list:
            print(object.elevation)

class time:
    # contains information about how many minutes the entire trip will take rounded to nearest mile

    time = 0

    def set_time(self,minutes):
        self.time = round(minutes)

    def as_string(self):
        print('TOTAL TIME: ' + str(self.time) + ' minutes')

class distance:
    # contains information about how many miles the entire trip will take rounded to nearest mile

    distance = 0

    def set_distance(self,distance):
        self.distance = round(distance)

    def as_string(self):
        print(f'TOTAL DISTANCE: ' + str(self.distance) + ' miles')

class steps:
    # contains information about the list of steps or directions needed to take to get to each destination

    route = []

    def set_route(self,step):
        self.route.append(step)

    def clear_route(self):
        self.route = []

    def as_iterated_list(self,route):
        # takes in the route in list form and prints each step on its own line

        print('DIRECTIONS')
        for step in route:
            print(step)

class Latlong_output_generator:
    # contains the necessary information to output the LATLONG

    def generate(self,route_dict:dict):
        # takes in the route_dict and creates the printable output

        latlong_list = get_latlong(route_dict)
        latlong.as_iterated_list(latlong,latlong_list)

    def _get_keyword(self)-> str:
        return "LATLONG"

class Steps_output_generator:
    # contains the necessary information to output the STEPS

    def generate(self,route_dict:dict):
        # takes in the route_dict and creates the printable output

        steps_obj = get_steps(route_dict)
        steps.as_iterated_list(steps,steps_obj.route)

    def _get_keyword(self)-> str:
        return "STEPS"

class Totaltime_output_generator:
    # contains the necessary information to output the TOTALTIME

    def generate(self,route_dict:dict):
        # takes in the route_dict and creates the printable output

        time_obj = _get_time(route_dict)
        time.as_string(time_obj)

    def _get_keyword(self)-> str:
        return "TOTALTIME"

class Totaldistance_output_generator:
    # contains the necessary information to output the TOTALDISTANCE
    def generate(self,route_dict):
        # takes in the route_dict and creates the printable output

        distance_obj = _get_distance(route_dict)
        distance.as_string(distance_obj)

    def _get_keyword(self)-> str:
        return "TOTALDISTANCE"

class Elevation_output_generator:
    # contains the necessary information to output the ELEVATION

    def generate(self,route_dict):
        # takes in the route_dict and creates the printable output

        elevation_obj_list = _get_elevation(route_dict)
        elevation.as_iterated_list(elevation,elevation_obj_list)

    def _get_keyword(self)-> str:
        return "ELEVATION"

class list_output_generators:
    # contains the list of all of the different output generators

    generators = [Steps_output_generator,Elevation_output_generator,Totaldistance_output_generator,Totaltime_output_generator,Latlong_output_generator]

    def make_list_output_generators(self, input_list: list) -> 'list of classes':
        # takes in the input_list and creates the appropriate output generators

        generator_list = []
        for input in input_list:
            for generator in self.generators:
                if generator._get_keyword(generator) == input:
                    generator_list.append(generator)

        return generator_list

def generate_and_print(generator_list: list, route_dict: dict):
    # takes in the generator list and the route dictionary and generates the output/prints to shell

    print('')
    for generator in generator_list:
        generator.generate(generator, route_dict)
        print('')

def get_latlong(route_dict:dict) -> 'list of latlong objects':
    # takes in the route_dict and creates a list of latlong objects and returns that list

    location_data = route_dict['locations']
    latlng_list = []
    for item in location_data:
        latlng = latlong()
        value = item['latLng']
        latlng._lat = value['lat']
        latlng._lng = value['lng']
        latlng.set_lat_direction(latlng._lat)
        latlng.set_lng_direction(latlng._lng)
        latlng_list.append(latlng)

    return latlng_list

def get_steps(route_dict:dict) -> 'steps object':
    # takes in the route_dict and creates a step object, appends the steps to the object, and returns that object

    steps_obj = steps()
    for attribute in route_dict['legs']:
        for detail in attribute['maneuvers']:
            steps_obj.set_route(detail['narrative'])

    return steps_obj

def _get_time(route_dict:dict)-> 'time object':
    # takes in route_dict and returns time object with time in number of minutes (int)

    time_obj = time()
    drive_time = route_dict['time']
    time_obj.set_time(drive_time/60)

    return time_obj

def _get_distance(route_dict:dict)-> 'distance object':
    # takes in route_dict and returns distance object with distance in number of miles (int)

    distance_obj = distance()
    drive_distance = route_dict['distance']
    distance_obj.set_distance(drive_distance)

    return distance_obj

def _get_elevation(route_dict:dict)-> 'list of elevation objects':
    # takes in route_dict and returns an elevation object with elevations in feet (int)

    elevation_obj_list = []
    elevation_data = route_dict['elevations']
    for item in elevation_data:
        elevation_obj = elevation()
        elevation_obj.set_elevation(item)
        elevation_obj_list.append(elevation_obj)

    return elevation_obj_list

def collect_elevation(elevation_dict:dict)-> int:
    # takes in an elevation_dictionary and returns the elevation contained
    # Note: there is only one elvation per elevation dictionary because each location has its own url and
    # therefore its own dictionary

    elevation_data = elevation_dict['elevationProfile']
    for elevation in elevation_data:
        elevation = elevation['height']

    return elevation