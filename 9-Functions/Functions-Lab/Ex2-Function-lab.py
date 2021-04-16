# Richard Cross
# EX2 Functions Lab S2021
import random

#1
def dice_1():
    rnum = random.random() * 6
    rnum = int(rnum + 1)
    print(rnum)

#2
def dice_2():
    diceNum = random.random() * 6
    diceNum = int(diceNum + 1)
    return diceNum

#3
def dice_3(sides):
    diceNum = random.random() * sides
    diceNum = int(diceNum + 1)
    return diceNum

#4
def dice_4( sides = 6 ):
    return dice_3(sides)



# -----------------

dice_1()

print("dice_2() -> ", dice_2())

print("dice_3(9) -> ", dice_3(9))
print("dice_3(2) -> ", dice_3(2))

print("dice_4(3000) -> ", dice_4(3000))
print("dice_4() -> ", dice_4())