import ISS_Info
import turtle
import time

screen = turtle.Screen()
screen.setup(750,450)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("REAL.png")
screen.register_shape("mmm.gif")

iss = turtle.Turtle()
iss.shape("mmm.gif")
iss.penup()

while True:
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("position: \n latitude: {}, longitude: {}".format(lat,lon))
    iss.goto(float(lon),float(lat))
    time.sleep(1)


