#Matthew Littman UCI ID: 38916993

import urllib.parse         # used for turning a string into a properly formatted url using ascii
import urllib.request       # used when trying to open the response from MapQuests APIs
import json                 # used when taking the response written in JSON and turning it into python code
import output_generator

def build_direction_url(location_list:list) -> str:
    # takes in a list of locations given by the user and returns a url string that can connect
    # to MapQuest's Open Direction API

    BASE_DIRECTIONS_URL = 'http://open.mapquestapi.com/directions/v2/route'
    Consumer_Key = 'y67GjRNHX1slJtZlN15zZegLI96IB8Hn'

    query_parameters = [('key', Consumer_Key)]
    for location in location_list:
        if location == location_list[0]:
            query_parameters.append(('from',location))
        else:
            query_parameters.append(('to',location))

    return BASE_DIRECTIONS_URL + '?' + urllib.parse.urlencode(query_parameters)

def build_elevation_url(route_dict:dict) -> list:
    # takes in the route_dictionary, finds the latitudes and longitudes of the locations previously given by the user
    # and returns a list of url strings for each location
    # that can connect to MapQuest's Open Elevation API

    BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'
    Consumer_Key = 'y67GjRNHX1slJtZlN15zZegLI96IB8Hn'

    latlong_list = output_generator.get_latlong(route_dict)
    elevation_url_list = []

    for latlong in latlong_list:
        str_lat_long = str(latlong._lat) + ',' + str(latlong._lng)
        query_parameters = [('key', Consumer_Key),('unit','f'),('latLngCollection',str_lat_long)]
        url = BASE_ELEVATION_URL + '?' + urllib.parse.urlencode(query_parameters)
        elevation_url_list.append(url)

    return elevation_url_list

def get_direction_data(url:str) -> dict:
    # takes in the previously built Direction URL
    # attempts to get the data for the route from MapQuest and
    # if successful, returns a dictionary containing all the information about the route

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode(encoding = 'utf-8')
        print(data)
        route_dict = json.loads(data)
        route_dict = route_dict['route']
    except:
        print('\n'+ 'MAPQUEST ERROR',end ='')
        quit()

    response.close()

    return route_dict

def get_elevation_data(elevation_url_list:list,route_dict:dict) -> dict:
    # takes in the list of elevation urls and the route_dictionary and
    # attempts to update the dictionary by adding the elevations as one of the entries and
    # returns the updated dictionary

    elevations_list = []
    for elevation_url in elevation_url_list:
        try:
            response = urllib.request.urlopen(elevation_url)
            data = response.read().decode(encoding='utf-8')
            elevation_dict = json.loads(data)
            elevation = output_generator.collect_elevation(elevation_dict)
            elevations_list.append(elevation)
            route_dict.update({'elevations': elevations_list})
        except:
            print('\n' + 'MAPQUEST ERROR', end='')
            quit()

    response.close()

    return route_dict