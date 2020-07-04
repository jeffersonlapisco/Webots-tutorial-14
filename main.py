# **************************************************************
# Project extra - Disciplina de robótica Móvel UFC / IFCE / LAPISCO
#       Simulação extra 03 com robô Pioneer 3AT - Webots R2020a
#              Position sensors - encoders
#        Python 3.5 na IDE Pycharm - controller <extern>
#                By: Jefferson S. Almeida
#                       Data: 04/07/2020
# **************************************************************

from controller import Robot
from controller import Motor
from controller import Compass
import math

TIME_STEP = 64
MAX_SPEED = 1.2

robot = Robot()

# bussola
mag = robot.getCompass("compass")
Compass.enable(mag, TIME_STEP)

leftMotor = robot.getMotor('left wheel')
rightMotor = robot.getMotor('right wheel')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

while robot.step(TIME_STEP) != -1:

    # lê o sensor
    north = Compass.getValues(mag)
    phi = math.atan2(north[0], north[2]) * (180/math.pi)
    # converter para faixa de 0 a 360 graus
    if phi < 0:
         phi = phi + 360

    Vl = -0.5 * MAX_SPEED
    Vr = 0.5 * MAX_SPEED

    leftMotor.setVelocity(Vl)
    rightMotor.setVelocity(Vr)

    print("ângulo = %0.2f graus" % phi)
