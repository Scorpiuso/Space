from turtle import *
import turtle

#Jupiter, Saturn, Uranus, Neptune, Pluto

wn = turtle.Screen()
wn.bgcolor("Black")


murcuryAnswer = "Murcury: Smallest planet. Fastest orbit of 87 days."


venusAnswer = "Venus: 227 earth days to year. Second planet."


earthAnswer = "Earth: We live in Earth. 364.25 days in year. Has oceans and land"


marsAns = "Mars: 4th planet. Second smallest. 687 earth days to years."


jupA = "Jupiter: Biggest planet, 16 earths can fit it, 12 earth years to one orbit."


satA = "Saturn: Has rings, 6th planet, 29 earth years for orbit."


uranusA = "Uranus: 7th planet, largest planet radius."


nepA = "Neptune: 165 earth years for one orbit. 2.7 billion miles from sun."


plutoA = "Dwarf planet. Not an actual PLANET"

roundsforever = 0

pluto = turtle.Turtle()
pluto.color("Grey")
pluto.shape("circle")

neptune = turtle.Turtle()
neptune.shape("circle")
neptune.color("Dark Blue")

uranus = turtle.Turtle()
uranus.color("Light Blue")
uranus.shape("circle")

pOrb = turtle.Turtle()
pOrb.color("White")
pOrb.pu()
pOrb.speed(0)
pOrb.right(90)
pOrb.forward(900)
pOrb.left(90)
pOrb.pd()
pOrb.circle(1000)
pOrb.hideturtle()

uOrb = turtle.Turtle()
uOrb.color("White")
uOrb.pu()
uOrb.speed(0)
uOrb.right(90)
uOrb.forward(700)
uOrb.left(90)
uOrb.pd()
uOrb.circle(800)
uOrb.hideturtle()

saturn = turtle.Turtle()
saturn.color("Yellow")
saturn.shape("circle")


earth = turtle.Turtle()
earth.color("Green")
earth.shape("circle")

jupiter = turtle.Turtle()
jupiter.color("Brown")
jupiter.shape("circle")

nOrb = turtle.Turtle()
nOrb.color("White")
nOrb.pu()
nOrb.speed(0)
nOrb.right(90)
nOrb.forward(800)
nOrb.left(90)
nOrb.pd()
nOrb.circle(900)
nOrb.hideturtle()

sOrb = turtle.Turtle()
sOrb.color("White")
sOrb.pu()
sOrb.speed(0)
sOrb.right(90)
sOrb.forward(600)
sOrb.left(90)
sOrb.pd()
sOrb.circle(700)
sOrb.hideturtle()

jOrbit = turtle.Turtle()
jOrbit.color("White")
jOrbit.pu()
jOrbit.speed(0)
jOrbit.right(90)
jOrbit.forward(500)
jOrbit.left(90)
jOrbit.pd()
jOrbit.circle(600)
jOrbit.hideturtle()

eOrb = turtle.Turtle()
eOrb.pu()
eOrb.speed(0)
eOrb.color("White")
eOrb.right(90)
eOrb.forward(300)
eOrb.left(90)
eOrb.pd()
eOrb.circle(400)
eOrb.hideturtle()

mars = turtle.Turtle()
orbitM = turtle.Turtle()
orbitM.color("White")
orbitM.pu()
orbitM.speed(0)
orbitM.right(90)
orbitM.forward(400)
orbitM.left(90)
orbitM.pd()
orbitM.circle(500)
orbitM.hideturtle()

mars.color("Red")
mars.shape("circle")

orbitM.color("White")



textSun = turtle.Turtle()
textSun.color("Green")
textM = turtle.Turtle()
textM.color("White")
textV = turtle.Turtle()
textV.color("White")
textE = turtle.Turtle()
textE.color("White")
textMa = turtle.Turtle()
textMa.color("White")
textJ = turtle.Turtle()
textJ.color("White")
textS = turtle.Turtle()
textS.color("White")
textU = turtle.Turtle()
textU.color("White")
textN = turtle.Turtle()
textN.color("White")
textP = turtle.Turtle()
textP.color("White")

venus = turtle.Turtle()
venus.pu()
venus.color("Orange")
venus.shape("circle")
orbit2 = turtle.Turtle()
orbit2.color("White")
orbit2.speed(0)
orbit2.pu()
orbit2.right(90)
orbit2.forward(200)
orbit2.left(90)
orbit2.pd()
orbit2.circle(300)
orbit2.hideturtle()
murcury = turtle.Turtle()
murcury.color("Dark Gray")
murcury.shape("circle")
sun = turtle.Turtle()
sun.color("Yellow")
sun.speed(0)
sun.shape("circle")
orbit = turtle.Turtle()
orbit.color("White")
orbit.pu()
orbit.speed(0)
orbit.right(90)
orbit.forward(100)
orbit.right(-90)
orbit.pd()
orbit.circle(200)
orbit.hideturtle()
sun.hideturtle()

earth.pu()
earth.color("Black")
earth.speed(0)
earth.right(90)
earth.forward(300)
earth.left(90)
earth.circle(400)
earth.color("Green")
earth.speed(4)

sun.begin_fill()
sun.fillcolor("Yellow")
sun.circle(100)
sun.end_fill()

# To direct the planet

murcury.pu()
murcury.speed(0)
murcury.right(90)
murcury.forward(100)
murcury.speed(5)
murcury.right(-90)

venus.speed(0)
venus.right(90)
venus.forward(200)
venus.left(90)
venus.speed(4)

mars.speed(0)
mars.pu()
mars.right(90)
mars.forward(400)
mars.left(90)
mars.speed(4)

jupiter.pu()
jupiter.speed(0)
jupiter.right(90)
jupiter.forward(500)
jupiter.left(90)
jupiter.pu()
jupiter.speed(4)

saturn.pu()
saturn.speed(0)
saturn.right(90)
saturn.forward(600)
saturn.left(90)
saturn.pu()
saturn.speed(4)

uranus.pu()
uranus.speed(0)
uranus.right(90)
uranus.forward(700)
uranus.left(90)
uranus.pu()
uranus.speed(4)

neptune.pu()
neptune.speed(0)
neptune.right(90)
neptune.forward(800)
neptune.left(90)
neptune.pu()
neptune.speed(4)

pluto.pu()
pluto.speed(0)
pluto.right(90)
pluto.forward(900)
pluto.left(90)
pluto.pu()
pluto.speed(4)

# to add text to planet

textSun.pu()
textSun.width(10)
textSun.speed(0)
textSun.left(90)
textSun.forward(100)
textSun.right(90)
textSun.backward(70)
textSun.write("The Sun: A star, Not a planet...")
textSun.hideturtle()

textM.pu()
textM.speed(0)
textM.right(90)
textM.forward(120)
textM.left(90)
textM.backward(100)
textM.right(90)
textM.forward(20)
textM.left(90)
textM.write(murcuryAnswer)
textM.hideturtle()

textV.pu()
textV.speed(0)
textV.right(90)
textV.forward(220)
textV.left(90)
textV.backward(100)
textV.right(90)
textV.forward(20)
textV.write(venusAnswer)
textV.hideturtle()

textE.pu()
textE.speed(0)
textE.right(90)
textE.forward(320)
textE.left(90)
textE.backward(100)
textE.right(90)
textE.forward(20)
textE.write(earthAnswer)
textE.hideturtle()

textMa.pu()
textMa.speed(0)
textMa.right(90)
textMa.forward(420)
textMa.left(90)
textMa.backward(100)
textMa.right(90)
textMa.forward(20)
textMa.write(marsAns)
textMa.hideturtle()

textJ.pu()
textJ.speed(0)
textJ.right(90)
textJ.forward(520)
textJ.left(90)
textJ.backward(100)
textJ.right(90)
textJ.forward(20)
textJ.write(jupA)
textJ.hideturtle()

textS.pu()
textS.speed(0)
textS.right(90)
textS.forward(620)
textS.left(90)
textS.backward(100)
textS.right(90)
textS.forward(20)
textS.write(satA)
textS.hideturtle()

textU.pu()
textU.speed(0)
textU.right(90)
textU.forward(720)
textU.left(90)
textU.backward(100)
textU.right(90)
textU.forward(20)
textU.write(uranusA)
textU.hideturtle()

textN.pu()
textN.speed(0)
textN.right(90)
textN.forward(820)
textN.left(90)
textN.backward(100)
textN.right(90)
textN.forward(20)
textN.write(nepA)
textN.hideturtle()

textP.pu()
textP.speed(0)
textP.right(90)
textP.forward(920)
textP.left(90)
textP.backward(100)
textP.right(90)
textP.forward(20)
textP.write(plutoA)
textP.hideturtle()

while roundsforever < 1:
  murcury.circle(200)
  venus.circle(300)
  earth.circle(400)
  mars.circle(500)
  jupiter.circle(600)
  saturn.circle(700)
  uranus.circle(800)
  neptune.circle(900)
  pluto.circle(1000)


  ## How this was made: First off, I create new turtles in python and made them a certain color depending on the planet it is supposed to be. Then I would make new turtles for the orbit of the planet that is the white rings around the sun. I would make the colored turtles make circles on the orbit so that it would look like it is orbiting the sun, but is actually drawing circles with its pen up! Then I put text under each planet/star telling maybe a few facts about the planet/star.

  ## Github in description. Give me a game idea next video and the best one will get a shoutout and i will make that game in html and javascript. SUBSCRIBE!!!!!
