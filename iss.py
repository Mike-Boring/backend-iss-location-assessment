#!/usr/bin/env python

__author__ = 'Mike Boring'
# used for reference:
# https://projects.raspberrypi.org/en/projects/where-is-the-space-station/5

import requests
import turtle
import time

iss_current_longitude = 0
iss_current_latitude = 0
iss_current_timestamp = 0
passover_risetime = 0


def currently_in_space():
    """
    Return data of who is currently in space.
    """
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
    """
    Find the current coordinates of the ISS.
    """
    req = requests.get(
        'http://api.open-notify.org/iss-now.json')
    converted_content = req.json()  # convert json
    global iss_current_latitude
    global iss_current_longitude
    global iss_current_timestamp
    iss_current_timestamp = converted_content['timestamp']
    iss_position = converted_content['iss_position']
    iss_current_longitude = iss_position['longitude']
    iss_current_latitude = iss_position['latitude']
    print('\nInternational Space Station Location:')
    print('Current Timestamp:', iss_current_timestamp)
    print('Current Longitude:', iss_current_longitude)
    print('Current Latitude:', iss_current_latitude)
    return


def run_the_turtle():
    """
    Run the turtle to plot ISS on map, Indianapolis and Next Passover Date.
    """
    # setup the screen and background
    screen = turtle.Screen()
    screen.register_shape('iss.gif')
    screen.setup(720, 360)
    screen.bgpic("map.gif")
    # setup the iss graphic
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)  # face upwards
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss.penup()
    iss.goto(float(iss_current_longitude), float(iss_current_latitude))
    iss.pendown()

    # Map Indianapolis on map and next passover date
    indianapolis_lat = 39.7684
    indianapolis_lon = -86.1581
    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(float(indianapolis_lon), float(indianapolis_lat))
    location.dot(10)
    location.color('yellow')
    style = ('Courier', 15)
    location.write('Next ISS passover for\nIndianapolis, Indiana is\n' +
                   passover_risetime + '.', font=style, align='left')
    location.hideturtle()
    turtle.done()
    return


def iss_passover():
    """
    Retireve the next ISS passover date
    """
    req = requests.get(
        'http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=-86.1581')
    converted_content = req.json()  # convert json
    global passover_risetime
    passover_risetime = time.ctime(
        converted_content['response'][0]['risetime'])
    return


def main():
    currently_in_space()
    find_space_station()
    iss_passover()
    run_the_turtle()


if __name__ == '__main__':
    main()
