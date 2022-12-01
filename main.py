from random import randint
import pickle
from os import path

tops = {}
if path.exists('tops.pkl'):
    with open('tops.pkl', 'rb') as pickle_file:
        tops = pickle.load(pickle_file)


class Tankas:
    x, y = 0, 0
    direction = 'n'
    shots = {'n': 0, 'e': 0, 'w': 0, 's': 0}
    total_shots = 0
    successful_shots = 0
    points = 10
    commander = ''

    def movement(self, move_direction):
        if move_direction == 'n':
            Tankas.y += 1
        if move_direction == 'e':
            Tankas.x += 1
        if move_direction == 'w':
            Tankas.x -= 1
        if move_direction == 's':
            Tankas.y -= 1
        self.direction = move_direction
        return self.direction

    def shooting(self):
        self.shots[self.direction] += 1
        self.total_shots = sum(self.shots.values())
        return self.total_shots

    def info(self):
        return f'------\n' \
               f'Direction: {self.direction}\n' \
               f'Coordinates: {self.x}, {self.y}\n' \
               f'Shots info:{self.shots}\n' \
               f'Shooting attempts:{self.total_shots}\n' \
               f'Points left: {self.points}\n' \
               f'------'

    def count_points(self):
        if self.points <= 0:
            return False
        else:
            return True

    def aim(self):
        if target.target_x == tank.x:
            if target.target_y < tank.y and tank.direction == 's':
                self.total_shots += 1
                return True
            elif target.target_y > tank.y and tank.direction == 'n':
                self.total_shots += 1
                return True
            else:
                return False
        if target.target_y == tank.y:
            if target.target_x < tank.x and tank.direction == 'w':
                self.total_shots += 1
                return True
            elif target.target_x > tank.x and tank.direction == 'e':
                self.total_shots += 1
                return True
            else:
                return False


class Target:
    def __init__(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y


tank = Tankas()
target = Target(randint(-4, 5), randint(-4, 5))

print(target.target_x, target.target_y)


while tank.count_points():
    menu = input("Choose action: \nMOVE: n/e/s/w  ||  SHOOT: sh  ||  INFO: i  ||  QUIT: q\n"
                 "Wanna enter your name ? yes   ||  See the scoreboard: top")
    print(target.target_x, target.target_y)
    if menu == 'yes':
        tank.commander = input("Your name: ")
    else:
        tank.commander = "Default"
    if menu == 'top':
        for keys, values in tops.items():
            print(f'{keys} : {values}')

    if menu == 'n':
        tank.movement('n')
    if menu == 'e':
        tank.movement('e')
    if menu == 'w':
        tank.movement('w')
    if menu == 's':
        tank.movement('s')
    if menu == 'sh':
        tank.shooting()
        if tank.aim() is True:
            print("Successful shot !")
            tank.points += 10
            tank.successful_shots += 1
            target = Target(randint(-4, 5), randint(-4, 5))
        else:
            print("Missed :(")
            tank.points -= 5
    if menu == 'i':
        print(tank.info())
    if menu == 'q':
        print("------\n"
              "Game ends")
        break
    if not tank.count_points():
        print(f'------\n'
              f'Game over. Targets destroyed: {tank.successful_shots}')
        tops[tank.commander] = tank.successful_shots
        print(tops)
        with open('tops.pkl', 'wb') as pickle_file:
            pickle.dump(tops, pickle_file)







