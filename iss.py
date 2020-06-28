#!/usr/bin/env python

__author__ = 'Mike Boring'
# used for reference:
# https://projects.raspberrypi.org/en/projects/where-is-the-space-station/5

import requests
import turtle

iss_current_longitude = 0
iss_current_latitude = 0
iss_current_timestamp = 0


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
    global iss_current_latitude
    global iss_current_longitude
    global iss_current_timestamp
    iss_current_timestamp = converted_content['timestamp']  # timestamp
    iss_position = converted_content['iss_position']
    iss_current_longitude = iss_position['longitude']
    iss_current_latitude = iss_position['latitude']
    print('\nInternational Space Station Location:')
    print('Current Timestamp:', iss_current_timestamp)
    print('Current Longitude:', iss_current_longitude)
    print('Current Latitude:', iss_current_latitude)
    return


def run_the_turtle():
    screen = turtle.Screen()
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)  # face upwards
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss.penup()
    iss.goto(float(iss_current_longitude), float(iss_current_latitude))
    print('iss lon:', iss_current_longitude)
    print('iss lat:', iss_current_latitude)
    iss.pendown()

    screen.setup(720, 360)
    screen.bgpic("map.gif")
    turtle.done()
    return


def main():
    currently_in_space()
    find_space_station()
    run_the_turtle()


if __name__ == '__main__':
    main()
