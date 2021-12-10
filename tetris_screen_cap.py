from PIL import ImageGrab, ImageOps,Image,ImageStat
import pyautogui as py
import win32gui
from time import sleep
import pygetwindow as gw
import numpy as np
import os
from tetris_vars import *

script_folder = os.path.dirname(__file__)
screenshot = script_folder+'\\screen.jpg'

def reset_window():
    py.click(400,30)
    # sleep(.5)
    # py.hotkey('ctrl','l')
    # py.write('https://tetris.com/play-tetris')
    # py.press('enter')
    # sleep(6)
    tetris_window = gw.getWindowsWithTitle('Free Online')[0]
    tetris_window.resizeTo(1300,1300)
    tetris_window.move(0,0)

def start_game():
    py.click(600,550) #play
    py.click(600,550) #play
    sleep(3)

def grab_screen():
    global screen
    screen = ImageGrab.grab(bbox=tetris_screen)
    # screen.save('screen.jpg')
    # print(screen)
    # screen.show()

def grab_screen_from_file():
    global screen
    screen = Image.open(screenshot).convert('LA')



def check_filled(display=0):
    global screen
    padding = 11
    centre = 4
    box_coords = []
    na = np.array(screen)
    for column in range(1,tetris_grid[1]+1):
        for row in range(1,tetris_grid[0]+1):
            # setup coordinates to interrogate numpy pixel array
            # it's array is Y,X   (Y-down, X-right)
            # format will be (start y, start x)
            start_row = (row-1) * padding * 2 + padding + (row-1)*centre
            start_col = (column-1) * padding * 2 + padding + (column-1)*centre
            centre_coords =  (start_row,start_col,)
            box_coords.append(centre_coords)
                
            # box_stat = ImageStat.Stat(box).mean
            # box_stat = sum(box_stat)
            # results.append([box_stat])
    # print(box_coords[:30])
    results = []
    for x in box_coords:
        temp = []
        for y in range(centre):
            for z in range(centre):
                temp.append(na[x[1]+y][x[0]+z][0])
        if sum(temp) > 50:
            results.append('x')
        else:
            results.append('.')
    # print(results)
    if display==1:
        for x,y in enumerate(results):
            if x % 10 == 0:
                print()
            print(y, end=' ')


    # print(na)
# reset_window()
# start_game()
if __name__ == '__main__':
    grab_screen_from_file()
    check_filled(1)
# na = np.array(screen)
# # print(sum(na[0][0]))
# for x in na[500]:
#     print(sum(x), end=', ')



#     # grab_screen()

#     # check_filled()
#     na = np.array(screen)
#     print(sum(na[0][0]))
#     # for x in na[510]:
#         # print(sum(x))
#     sleep(.5)