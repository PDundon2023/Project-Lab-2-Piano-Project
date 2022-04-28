import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017
from time import sleep
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)

mcp = MCP23017(i2c, address=0x24)
mcp2 = MCP23017(i2c, address=0x20)

pin0_24 = mcp.get_pin(0)
pin0_24.direction = Direction.OUTPUT

pin1_24 = mcp.get_pin(1)
pin1_24.direction = Direction.OUTPUT

pin2_24 = mcp.get_pin(2)
pin2_24.direction = Direction.OUTPUT

pin3_24 = mcp.get_pin(3)
pin3_24.direction = Direction.OUTPUT

pin4_24 = mcp.get_pin(4)
pin4_24.direction = Direction.OUTPUT

pin5_24 = mcp.get_pin(5)
pin5_24.direction = Direction.OUTPUT

pin8_24 = mcp.get_pin(8)
pin8_24.direction = Direction.OUTPUT

pin9_24 = mcp.get_pin(9)
pin9_24.direction = Direction.OUTPUT

pin10_24 = mcp.get_pin(10)
pin10_24.direction = Direction.OUTPUT

pin11_24 = mcp.get_pin(11)
pin11_24.direction = Direction.OUTPUT

pin12_24 = mcp.get_pin(12)
pin12_24.direction = Direction.OUTPUT

pin13_24 = mcp.get_pin(13)
pin13_24.direction = Direction.OUTPUT


######
pin0_20 = mcp2.get_pin(0)
pin0_20.direction = Direction.OUTPUT

pin1_20 = mcp2.get_pin(1)
pin1_20.direction = Direction.OUTPUT

pin2_20 = mcp2.get_pin(2)
pin2_20.direction = Direction.OUTPUT

pin3_20 = mcp2.get_pin(3)
pin3_20.direction = Direction.OUTPUT

pin4_20 = mcp2.get_pin(4)
pin4_20.direction = Direction.OUTPUT

pin5_20 = mcp2.get_pin(6)
pin5_20.direction = Direction.OUTPUT

pin8_20 = mcp2.get_pin(8)
pin8_20.direction = Direction.OUTPUT

pin9_20 = mcp2.get_pin(9)
pin9_20.direction = Direction.OUTPUT

pin10_20 = mcp2.get_pin(10)
pin10_20.direction = Direction.OUTPUT

pin11_20 = mcp2.get_pin(11)
pin11_20.direction = Direction.OUTPUT

pin12_20 = mcp2.get_pin(12)
pin12_20.direction = Direction.OUTPUT

pin13_20 = mcp2.get_pin(13)
pin13_20.direction = Direction.OUTPUT


def solenoid_vec(sol_vec):
    ## IC1?

    pin0_24.value = sol_vec[4]
    pin1_24.value = sol_vec[5]
    pin2_24.value = sol_vec[6]
    pin3_24.value = sol_vec[7]
    pin4_24.value = sol_vec[8]
    pin5_24.value = sol_vec[9]
    pin8_24.value = sol_vec[0]
    pin9_24.value = sol_vec[1]
    pin10_24.value = sol_vec[2]
    pin11_24.value = sol_vec[3]
    pin12_24.value = sol_vec[10]
    pin13_24.value = sol_vec[11]

    ##
    pin0_20.value = sol_vec[12]
    pin1_20.value = sol_vec[13]
    pin2_20.value = sol_vec[14]
    pin3_20.value = sol_vec[15]
    pin4_20.value = sol_vec[16]
    pin5_20.value = sol_vec[17]
    pin8_20.value = sol_vec[18]
    pin9_20.value = sol_vec[19]
    pin10_20.value = sol_vec[20]
    pin11_20.value = sol_vec[21]
    pin12_20.value = sol_vec[22]
    pin13_20.value = sol_vec[23]




  


# we have an array of size 24 #
# from left to right we have C  D  E  F  G  A  B  C  D  E   F   G   A   B   C 
# -------------------------- 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
# this constitues the first 15 entries for the array #
# the remaining entrires in the array correspond to the black keys #

# off_all makes sure that all solenoids are set to 0, in other words no keys are being pressed #

off_all = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# C_progression is the progression of keys for C -> E -> A #
C_progression = np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])

# C_E_progression is just the progression for C -> E #
C_E_progression = np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# BA_progression is the progression for B -> E -> A #
BA_progression = np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])

# BG_progression is the progression for B -> E -> G #
BG_progression = np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])

# BE_progression is the progrssion for just B -> E #
BE_progression = np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# B_note plays the note B #
B_note = np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# C_note plays the note C #
C_note = np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# C_chord plays the chord CEA #
C_chord  = np.array([0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0])

# BA_chord plays the chord BEA #
BA_chord = np.array([0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0])

# BG_chord plays the chord BEG #
BG_chord = np.array([0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0])


# Intro #
for i in range(2):
  for n in range(len(C_progression)):
      solenoid_vec(C_progression[n])
      sleep(1)
  for n in range(len(C_E_progression)):
    solenoid_vec(C_E_progression[n])
    sleep(1)
  for n in range(len(BA_progression)):
    solenoid_vec(BA_progression[n])
    sleep(1)
  for n in range(len(BG_progression)):
    solenoid_vec(BG_progression[n])
    sleep(1)
  for n in range(len(BE_progression)):
    solenoid_vec(BE_progression[n])
    sleep(1)
    
# Transition #
for j in range(2):
  for i in range(5):
    for n in range(len(C_progression)):
      solenoid_vec(C_progression[n])
      sleep(0.5)
    for n in range(len(C_note)):
      solenoid_vec(C_note[n])
      sleep(0.5)
  for i in range(5):
    for n in range(len(BG_progression)):
      solenoid_vec(BG_progression[n])
      sleep(0.5)
    for n in range(len(B_note)):
      solenoid_vec(B_note[n])
      sleep(0.5)

# Melody #
for i in range(10):     
  for n in range(8):
    solenoid_vec(C_chord)
    sleep(0.5)
  for n in range(3):
    solenoid_vec(BA_chord)
    sleep(0.5)
  for n in range(5):
    solenoid_vec(BG_chord)
    sleep(0.5)