import pygame.mouse

import displays.WidgetsV2.MyInteractable

class Slider(displays.WidgetsV2.MyInteractable.Interactable):
    def __init__(self,SCREEN,pos,WH,back_col,bounds,background_col,autodraw = True,autoclick=True):
        self.background_col = background_col
        super().__init__(SCREEN,pos,WH,back_col,autodraw=autodraw,autoclick=autoclick)
        self._bounds = bounds

        self._mouse_down = False
        self._rel_bar_loc = 0

        self._bar_val = self._bounds[0]

        self._new_rectpos = (
            self.rectPos[0]-5,
            self.rectPos[1],
            self.rectPos[2]+10,
            self.rectPos[3]
        )
        mid_y = int(self.pos[1]+0.5*self.WH[1])
        self._midLine = (
            (self.pos[0],mid_y),
            (self.pos[0]+self.WH[0],mid_y)
        )
        self.barLoc = (
            (self.pos[0]+self._rel_bar_loc-5),
            (self.pos[1]),
            (10),
            (self.WH[1])
        )



    def additional_mouse_down(self,event):
        self._mouse_down = pygame.mouse.get_pressed(3)[0]
    def additional_mouse_up(self,event):
        self._mouse_down = pygame.mouse.get_pressed(3)[0]

    def additional_selected_loop(self):
        if self._mouse_down and self.selected_mouse_pos[0]>=self.pos[0] and self.selected_mouse_pos[0]<=self.pos[0]+self.WH[0]:
            self.rel_bar_loc = self.selected_mouse_pos[0] - self.pos[0]

    def draw(self):
        self._needs_update = 0

        pygame.draw.rect(self._SCREEN,self.background_col,self._new_rectpos)
        pygame.draw.line(self._SCREEN,"black",(self.pos[0],self.pos[1]),self.counterRectCoords[0])
        pygame.draw.line(self._SCREEN,"black",self.counterRectCoords[1],self.leadingRectCoords[1])
        pygame.draw.line(self._SCREEN,"black",self._midLine[0],self._midLine[1])
        pygame.draw.rect(self._SCREEN,self.back_col,self.barLoc)
        pygame.draw.rect(self._SCREEN,"black",self.barLoc,1)

    @property
    def bar_val(self):
        val = self._bounds[0] + self._rel_bar_loc/self.WH[0]
        return val


    @property
    def rect_pos(self):
        return self._rectPos
    @rect_pos.setter
    def rect_pos(self,newRectPos):
        super().rectPos = newRectPos
        self._new_rectpos = (
            self.rectPos[0]-5,
            self.rectPos[1],
            self.rectPos[2]+10,
            self.rectPos[3]
        )

    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self,new_pos):
        super().pos = new_pos
        mid_y = int(self.pos[1]+0.5*self.WH[1])
        self._midLine = (
            (self.pos[0],mid_y),
            (self.pos[0]+self.WH[0],mid_y)
        )

    @property
    def WH(self):
        return self._WH
    @WH.setter
    def WH(self,newWH):
        super().WH = newWH
        mid_y = int(self.pos[1]+0.5*self.WH[1])
        self._midLine = (
            (self.pos[0],mid_y),
            (self.pos[0]+self.WH[0],mid_y)
        )

    @property
    def rel_bar_loc(self):
        return self._rel_bar_loc
    @rel_bar_loc.setter
    def rel_bar_loc(self,newRel_bar_loc):
        self._rel_bar_loc = newRel_bar_loc
        self.barLoc = (
            (self.pos[0]+self._rel_bar_loc-5),
            (self.pos[1]),
            (10),
            (self.WH[1])
        )
        self._needs_update = 1
