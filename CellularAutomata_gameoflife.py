import random
import turtle as Display

width = 100
height = 100
cell_size = 4
grid = [[" "]*width for _ in range(height)]

def get_neighbor_num(area : list[list],pos : tuple[int,int]) -> int :
    """Returns the number of live cells around a cell"""
    num = 0
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

    for dir in directions :
        new_pos = (pos[0] + dir[0],pos[1] + dir[1])
        if new_pos[0] in range(len(area)) and new_pos[1] in range(len(area[0])) :
            if area[new_pos[0]][new_pos[1]] == "*" :
                num += 1

    return num

def add_live_cell(area : list[list], centre : bool, max_cell : int) -> None :
    """Adds a live cell randomly in the area"""
    for _ in range(max_cell+1) :
        if (centre) :
            x_range = (int(len(area)//2.5),int(len(area)//1.5))
            y_range = (int(len(area[0])//2.5),int(len(area[1])//1.5))
        else :
            x_range = (0,len(area)-1)
            y_range = (0,len(area[1])-1) 

        rpos = (random.randint(x_range[0],x_range[1]),random.randint(y_range[0],y_range[1]))
        area[rpos[0]][rpos[1]] = "*"

def live_cell_info(area : list[list]) -> int :
    """Returns the total number of live cells in the area"""
    num = 0
    cell_pos = []

    for y,row in enumerate(area) : 
        num += row.count("*")
        for x in range(len(row)) :
            if area[y][x] == "*" :
                cell_pos.append((x,y))

    return num,cell_pos

def cell_rules(area : list[list],pos : tuple[int,int]) -> None :
    """Applies these rules to the area"""

    Cell_num = get_neighbor_num(area,pos) 

    #Rule 1
    if Cell_num < 2 and area[pos[0]][pos[1]] == "*" :
        area[pos[0]][pos[1]] = " " 
    #Rule 2
    if Cell_num in [2,3] and area[pos[0]][pos[1]] == "*" :
        area[pos[0]][pos[1]] = "*"
    #Rule 3
    if Cell_num > 3 and area[pos[0]][pos[1]] == "*" :
        area[pos[0]][pos[1]] = " "
    #Rule 4
    if Cell_num == 3 and area[pos[0]][pos[1]] == " " :
        area[pos[0]][pos[1]] = "*"

def update_display(Drawer, cell_pos : tuple[int,int]) -> None :
    """Displays the cells onto the turtle screen"""

    for y,x in cell_pos :

        Drawer.penup()
        Drawer.setpos(((x * cell_size) - (width*2),(y * cell_size) - (height*2)))
        Drawer.pendown()

        Drawer.begin_fill()
        for _ in range(4) :
            Drawer.forward(cell_size)
            Drawer.right(90)
        Drawer.end_fill()

#======================================================#
Display.title("Cellular Automata : The Game of Life")
Display.tracer(False)
Display.hideturtle()

while True :

    cell_info = live_cell_info(grid)

    if cell_info[0] < int(width*0.25) :
        add_live_cell(grid,True,10)
    
    for row in range(len(grid)) :
        for cell in range(len(grid[0])) :
            cell_rules(grid,(row,cell))

    Display.clear()
    update_display(Display,cell_info[1])
    Display.update()
