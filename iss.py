#!/usr/bin/env python

__author__ = 'Mike Boring'

import requests


def currently_in_space():
    req = requests.get(
        'http://api.open-notify.org/astros.json')
    converted_content = req.json()  # convert json
    people_list = converted_content['people']  # list of people
    print('Number of Astronauts in Space is:', len(people_list))
    print('Current Astronauts in Space:')
    for person in people_list:
        print('Name:', person['name'])
        print('Spacecraft:', person['craft'])
    return


def find_space_station():
    req = requests.get(
        'http://api.open-notify.org/iss-now.json')
    converted_content = req.json()  # convert json
    current_time_stamp = converted_content['timestamp']  # timestamp
    iss_position = converted_content['iss_position']
    print('\nInternational Space Station Location:')
    print('Current Timestamp:', current_time_stamp)
    print('Current Longitude:', iss_position['longitude'])
    print('Current Latitude:', iss_position['latitude'])
    return


def main():
    currently_in_space()
    find_space_station()


if __name__ == '__main__':
    main()
