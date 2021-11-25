import pygame

class Widget:
    widgets = []
    def __init__(self,SCREEN,pos,WH,back_col,autodraw = True):
        self._SCREEN = SCREEN
        self._pos = pos
        self._WH = WH
        self._back_col = back_col

        self._rectPos = (self._pos[0],self._pos[1],self._WH[0],self._WH[1])
        self._needs_update = 1

        if autodraw:
            Widget.widgets.append(self)


    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self,new_pos):
        self._pos =new_pos
        self._rectPos = (self._pos[0],self._pos[1],self._WH[0],self._WH[1])
        self._needs_update = 1


    @property
    def WH(self):
        return self._WH
    @WH.setter
    def WH(self,new_WH):
        self._WH = new_WH
        self._rectPos = (self._pos[0],self._pos[1],self._WH[0],self._WH[1])
        self._needs_update = 1


    @property
    def rectPos(self):
        return self._rectPos

    @property
    def leadingRectCoords(self):
        rectCoords = (
            (self._pos[0],self._pos[1]),
            (self._pos[0]+self._WH[0],self._pos[1]+self._WH[1])

        )
        return rectCoords


    @property
    def counterRectCoords(self):
        rectCoords = (
            (self._pos[0],self._pos[1]+self._WH[1]),
            (self._pos[0]+self._WH[0],self._pos[1])
        )
        return rectCoords


    def draw(self):
        self._needs_update = 0
        pygame.draw.rect(self._SCREEN,self._back_col,self._rectPos)
        pygame.draw.rect(self._SCREEN, "black", self._rectPos,1)

    @property
    def back_col(self):
        return self._back_col
    @back_col.setter
    def back_col(self,new_back_col):
        self._back_col = new_back_col

    @property
    def SCREEN(self):
        return self._SCREEN

    def in_bounds(self,mouse_pos):
        if mouse_pos[0]>self._rectPos[0] and mouse_pos[1]>self._rectPos[1]:
            if mouse_pos[0]<self._rectPos[0]+self._rectPos[2]:
                if mouse_pos[1]<self._rectPos[1]+self._rectPos[3]:
                    return True

    @property
    def needs_update(self):
        return self._needs_update