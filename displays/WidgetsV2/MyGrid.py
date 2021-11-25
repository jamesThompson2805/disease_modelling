import pygame.draw

import displays.WidgetsV2.MyInteractable
from displays.WidgetsV2.Materials.Materials import *

class Grid(displays.WidgetsV2.MyInteractable.Interactable):
    def __init__(self,SCREEN,pos,WH,cols,rows,back_col,autodraw = True,autoclick=True):
        super().__init__(SCREEN, pos, WH, back_col,autodraw=autodraw,autoclick=autoclick)

        self.materials={
            "blank":Mat,
            "wall":Wall,
            "windowC":WindowC,
            "windowS":WindowS,
            "windowO":WindowO,
            "door":Door,
            "floor":Floor,
            "TchairU":TeacherChairU,
            "TchairD":TeacherChairD,
            "TchairL":TeacherChairL,
            "TchairR":TeacherChairR,
            "SchairU":StudentChairU,
            "SchairD":StudentChairD,
            "SchairL":StudentChairL,
            "SchairR":StudentChairR,
            "desk":Desk
        }

        self._CR = (cols,rows)
        self._tile_sizes = (self.WH[0]/self._CR[0],self.WH[1]/self._CR[1])

        self._tiles = [[Mat for col in range(self._CR[0])] for row in range(self._CR[0])]
        self.selected_mat = None
        self.other_mat = Mat
        self._mouse_down = (0,0,0)
        
        self._undo_stack = []
        self._redo_stack = []
        self._current_state = ""


    def draw(self):
        self._needs_update = 0
        for row in range(self._CR[1]):
            for col in range(self._CR[0]):
                tilePos = (
                    self.pos[0]+col*self._tile_sizes[0],
                    self.pos[1]+row*self._tile_sizes[1],
                    self._tile_sizes[0],
                    self._tile_sizes[1]
                )
                pygame.draw.rect(self._SCREEN, self._tiles[row][col].colour, tilePos)
                if self.tiles[row][col].name[-1]=="U":
                    pygame.draw.rect(self.SCREEN,"red",
                        (int(tilePos[0]+0.5*tilePos[2]),int(tilePos[1]+0.25*tilePos[3]),1,2)
                    )
                elif self.tiles[row][col].name[-1]=="D":
                    pygame.draw.rect(self.SCREEN,"red",
                        (int(tilePos[0]+0.5*tilePos[2]),int(tilePos[1]+0.75*tilePos[3]),1,2)
                    )
                elif self.tiles[row][col].name[-1]=="L":
                    pygame.draw.rect(self.SCREEN,"red",
                        (int(tilePos[0]+0.25*tilePos[2]),int(tilePos[1]+0.5*tilePos[3]),2,1)
                    )
                elif self.tiles[row][col].name[-1]=="R":
                    pygame.draw.rect(self.SCREEN,"red",
                        (int(tilePos[0]+0.75*tilePos[2]),int(tilePos[1]+0.5*tilePos[3]),2,1)
                    )
                elif self.tiles[row][col].name[-1]=="O":
                    pygame.draw.rect(self.SCREEN,"grey",tilePos,2)
                elif self.tiles[row][col].name[-1]=="S":
                    pygame.draw.rect(self.SCREEN,"grey",tilePos,1)



    def mouse_pos_to_square(self,mouse_pos):
        rel_mouse_pos = (mouse_pos[0]-self.pos[0],mouse_pos[1]-self.pos[1])
        rel_square_pos = (
            round((rel_mouse_pos[0]/self._tile_sizes[0])-0.5),
            round((rel_mouse_pos[1]/self._tile_sizes[0])-0.5)
        )
        return rel_square_pos

    def square_to_mouse_pos(self,cell):
        rel_mouse_pos = (
            self.pos[0] + cell[0]*self._tile_sizes[0],
            self.pos[1] + cell[1]*self._tile_sizes[1],
        )
        return rel_mouse_pos

    def action(self):
        self.mouse_down = True
        super().action()


    def additional_mouse_down(self,event):
        self._previous_state = self.save_state()
        self._mouse_down = pygame.mouse.get_pressed(3)
        cell=self.mouse_pos_to_square(self.selected_mouse_pos)
        if self.in_bounds(self.selected_mouse_pos):
            if self._mouse_down[0]:
                if self.selected_mat == Floor:
                    self.add_floor(cell)
                elif self._tiles[cell[1]][cell[0]]==self.selected_mat:
                    self.selected_mat, self.other_mat = self.other_mat, self.selected_mat
            elif self._mouse_down[2]:
                if self.tiles[cell[1]][cell[0]].name[-1]=="C":
                    self.tiles[cell[1]][cell[0]] = WindowO
                elif self.tiles[cell[1]][cell[0]].name[-1]=="O":
                    self.tiles[cell[1]][cell[0]] = WindowS
                elif self.tiles[cell[1]][cell[0]].name[-1]=="S":
                    self.tiles[cell[1]][cell[0]] = WindowC
                elif self.tiles[cell[1]][cell[0]].name[-1]=="U":
                    if self.tiles[cell[1]][cell[0]]==TeacherChairU:
                        self.tiles[cell[1]][cell[0]] = TeacherChairR
                    else:
                        self.tiles[cell[1]][cell[0]] = StudentChairR
                elif self.tiles[cell[1]][cell[0]].name[-1]=="R":
                    if self.tiles[cell[1]][cell[0]]==TeacherChairR:
                        self.tiles[cell[1]][cell[0]] = TeacherChairD
                    else:
                        self.tiles[cell[1]][cell[0]] = StudentChairD
                elif self.tiles[cell[1]][cell[0]].name[-1]=="D":
                    if self.tiles[cell[1]][cell[0]]==TeacherChairD:
                        self.tiles[cell[1]][cell[0]] = TeacherChairL
                    else:
                        self.tiles[cell[1]][cell[0]] = StudentChairL
                elif self.tiles[cell[1]][cell[0]].name[-1]=="L":
                    if self.tiles[cell[1]][cell[0]]==TeacherChairL:
                        self.tiles[cell[1]][cell[0]] = TeacherChairU
                    else:
                        self.tiles[cell[1]][cell[0]] = StudentChairU

    def additional_mouse_up(self,event):
        self._mouse_down = pygame.mouse.get_pressed(3)
        if self._current_state != self.save_state():
            self._undo_stack.append(self._current_state)
            self._current_state = self.save_state()

    def additional_selected_loop(self):
        if  self.in_bounds(self.selected_mouse_pos):
            if self.selected_mat != None and self.selected_mat != Floor:
                cell = self.mouse_pos_to_square(pygame.mouse.get_pos())
                #test valid
                if self.selected_mat.check_and_place(cell,self._tiles):
                    if self._mouse_down[0]:
                        self._tiles[cell[1]][cell[0]] = self.selected_mat
                    rect = pygame.Surface((self._tile_sizes[0],self._tile_sizes[1]),pygame.SRCALPHA,32)
                    colour = (0,255,0, 75)
                    rect.fill(colour)
                    self._SCREEN.blit(rect,self.square_to_mouse_pos(cell))
                else:
                    rect = pygame.Surface((self._tile_sizes[0], self._tile_sizes[1]), pygame.SRCALPHA, 32)
                    colour = (255, 0, 0, 75)
                    rect.fill(colour)
                    self._SCREEN.blit(rect, self.square_to_mouse_pos(cell))


    def save_state(self):
        string = ""
        for row in self.tiles:
            for tile in row:
                string+=tile.name+"|"
            string=string[:-1]+"\n"
        return string


    def load_state(self,string):
        parts = string.split("\n")

        for row in range(self._CR[1]):
            row_string = parts.pop(0).split("|")
            for col in range(self._CR[0]):
                self.tiles[row][col] = self.materials[row_string[col]]
        
        self._needs_update = 1

    
    def add_floor(self,pos):
        desired_mat = Floor
        target_mat = self.tiles[pos[1]][pos[0]]
        if target_mat != desired_mat:
            floorable=True
            to_change=[pos]
            changed=[]
            dirs=[1,0,-1,0]            
            while len(to_change)!=0:
                to_append=[]
                for cell in to_change:
                    for i in range(4):
                        test_pos = (cell[0]+dirs[i],cell[1]+dirs[(i+1)%4])
                        if test_pos[0]>=0 and test_pos[0]<self._CR[0]:
                            if test_pos[1]>=0 and test_pos[1]<self._CR[1]:
                                if self.tiles[test_pos[1]][test_pos[0]]==target_mat:
                                    if test_pos not in to_append and test_pos not in changed:
                                        to_append.append(test_pos)
                            else:
                                floorable=False
                        else:
                            floorable=False
                for i in to_change:
                    changed.append(i)
                to_change = to_append
            if floorable:
                for coord in changed:
                    self.tiles[coord[1]][coord[0]]=desired_mat
        else:
            print("invalid target and desired material")
            
    def undo(self):
        if len(self._undo_stack)!=0:
            self._redo_stack.append(self.save_state())
            self.load_state(self._undo_stack.pop())
    
    def redo(self):
        if len(self._redo_stack)!=0:
            self._undo_stack.append(self.save_state())
            self.load_state(self._redo_stack.pop())
            
    @property
    def tiles(self):
        return self._tiles
    @tiles.setter
    def tiles(self,value):
        self._tiles = value
        self._needs_update = 1


