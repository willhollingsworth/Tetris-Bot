from PIL import ImageGrab, ImageOps,Image,ImageStat
import pyautogui as py
import win32gui
from time import sleep
import pygetwindow as gw
import numpy as np




def build_grid(x,y):
    global layout
    layout = []
    for row in range(y):
        templist = []
        for column in range(x):
            templist.append('.')
        layout.append(templist)

def print_grid():
    global layout
    for x in layout:
        for y in x:
            print(y,end=' ')
        print()

def flip_coords(coords):
    ''' using an x -> y ^ coord system - start counting at 1
        converts from written style into python array style'''
    global layout
    return [len(layout) - coords[1],coords[0]-1 ]

def check_outofbounds(coords,debug=0):
    ''' check if given coords are outside of layout'''
    global layout
    x_length = len(layout[0])
    y_length = len(layout)
    if coords[0] > x_length or coords[0] < 1:
        if debug : print('x cord OOB')
        return 1
    elif coords[1] > y_length or coords[1] < 1:
        if debug : print('y cord OOB')
        return 1
    else:
        return 0

def check_occupied(coords,debug=0):
    ''' check if given coords is occupied'''
    global layout
    f1 = flip_coords(coords)[0]
    f2 = flip_coords(coords)[1]
    if layout[f1][f2] == 'x':
        if debug : print('position occupied')
        return 1 
    return 

def run_checks(coords):
    if len(coords) == 2:
        if check_outofbounds(coords):
            return
        if check_occupied(coords):
            return 
    else:
        for x in coords:
            if check_outofbounds(x):
                return
            if check_occupied(x):
                return   
    return True


def write_to_layout(coords):
    global layout
    f1 = flip_coords(coords)[0]
    f2 = flip_coords(coords)[1]
    layout[f1][f2] = 'x'

def part_rotator(part,rotations):
    ''' rotate part by given rotations, return the new part'''
    new_part = []
    for x in part:
        temp = x
        for y in range(rotations):
            temp = [temp[1]*-1,temp[0]]
        new_part.append(temp)
    return new_part

def draw_part(start_pos,part,rotations=0):
    ''' draw the given part onto the layout'''
    global layout
    part_coords = part_gen_coords(start_pos,part,rotations)
    for x in part_coords:
        if run_checks(x):
            continue
        else: return
    for x in part_coords:
        write_to_layout(x)
    
def part_gen_coords(start_pos,part,rotations=0,flipped=0):
    ''' given a start coordinates, part, rotation and optionally a flip state
        output the coords of such a part'''
    current_position = start_pos[:]
    part_coords = [start_pos[:]]
    part = part_rotator(part,rotations)
    for x in part:
        # print('currently',current_position,'step',x,end=' ')
        if flipped:
            current_position[1] += x[0]
            current_position[0] += x[1]
        else:
            current_position[0] += x[0]
            current_position[1] += x[1]
        # print('final spot',current_position)
        part_coords.append(current_position[:])
    return part_coords

def find_highest_free_point(column):
    '''find the highest free point for given column'''
    global layout
    for x in range(len(layout)):
        if layout[x][column-1] == 'x':
            return len(layout) - x + 1   
    return 1

def score_coords(coords):
    global layout
    height = len(layout)
    score = 0
    for x in coords:
        score += height - x[1]
    return score

def try_all_part_positions(part):
    ''' given a part try each possible combination of positions and rotations 
        total should be columns x 4 (rotations possibility)'''
    global layout
    columns = len(layout[1]) 
    scores = []
    for column in range(1,columns+1):
        row = find_highest_free_point(column)
        for x in range(4):
            part_cords = part_gen_coords([column,row],part,x)
            if run_checks(part_cords):
                scores.append(score_coords(part_cords))
            else:
                scores.append(0)
    return scores

def pick_best_score(scores):
    best = [0,0]
    for x in range(len(scores)):
        if scores[x] > best[1]:
            best = [x,scores[x]]
    return best

def convert_score_to_move(score):
    rotation = score[0] % 4
    column = int(score[0] / 4) + 1
    return [column,rotation]