#!/usr/bin/env python

__author__ = 'Mike Boring'

import requests


def main():
    req = requests.get(
        'http://api.open-notify.org/astros.json')
    converted_content = req.json()  # convert json
    people_list = converted_content['people']  # list of people
    print('Number of Astronauts in Space is:', len(people_list))
    print('Current Astronauts in Space:')
    for person in people_list:
        print('Name: ', person['name'])
        print('Spacecraft: ', person['craft'])


if __name__ == '__main__':
    main()
