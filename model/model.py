from displays.WidgetsV2.MyGrid import *
from model.air_flow import CoughGrid

import numpy as np

class Model(Grid):
    def __init__(self,SCREEN,pos,WH,cols,rows,back_col,info_string):
        super().__init__(SCREEN, pos, WH, cols, rows, back_col, autodraw=True, autoclick=False)
        self.loading = True
        
        self._doors = []
        self._students = []
        self._teachers = []
        self._student_chairs = []
        self._teacher_chairs = []
        
        self._tick = 0
        self._cough_grid = CoughGrid(rows, cols)
        self._trace_grid = [[0 for col in cols] for row in rows]
        
        self._cough_trace_sum = np.zeros((rows,cols))
        
        self._timestamps=[]

    
    ## Has three modes: setup, going and end
    # In setup:
    #  loads parameters, conditions and grid tiles into self._tiles                                                                 Y!
    #  Finds all doors and chairs                                                                                                   Y!
    #  Creates the cough and trace grids, cough grid will be class I suspect
    #  Creates a student for every student chair in list, a teacher for every teacher chair in list
    #  Adds all pathfinding for all agents, allocates first stu to first stu chair and so on (maybe use multiprocessing if too slow)
    #  Finally gets this model going
    #
    # In going, and when a tick is sent through:
    #  Add one to tick counter
    #  Agent stuff happens, according to their state machines
    #  Update the cough and trace grids
    #  Update the timestamp of teachers and students infected
    #  Add cough and trace values to cough trace sum to identify worst squares later
    #
    # In end:
    #  Return timestamps and cough trace sum to give info on numbers infected over time and worst squares

    ### Setup
    def load_all(self,load_string):
        save_sections = load_string.split("\n")
        self.conditions = [int(i) for i in save_sections.pop(0).split("|")]
        parameters = [float(i) for i in save_sections.pop(0).split("|")]
        self.cough_chance = parameters.pop(0)
        self.trace_chance = parameters.pop(0)
        self.student_inf_start = parameters.pop(0)
        self.teacher_inf_start = parameters.pop(0)
        self.ceiling_height = parameters.pop(0)
        self.vacc_perc = parameters.pop(0)
        grid_string = "\n".join(save_sections)
        self.load_state(grid_string)
        
    def find_doors_chairs(self):
        for row_index,row in enumerate(self._tiles):
            for col_index,tile in enumerate(row):
                if tile.name == "door":
                    self._doors.append((col_index,row_index))
                elif tile.name[:-1] == "Schair":
                    self._student_chairs.append((col_index,row_index))
                elif tile.name[:-1] == "Tchair":
                    self._teacher_chairs.append((col_index,row_index))
                    
    def add_agents(self):
        pass
                    
                    
        
        
