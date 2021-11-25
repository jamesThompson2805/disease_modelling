import pygame.draw

import displays.WidgetsV2.MyClickable
import displays.WidgetsV2.MyText

class Button(displays.WidgetsV2.MyClickable.Clickable):
    def __init__(self,SCREEN,pos,WH,back_col,alt_col,autodraw = True,autoclick=True):
        super().__init__(SCREEN,pos,WH,back_col,autodraw = autodraw, autoclick=autoclick)
        self._alt_col = alt_col

    def action(self):
        super().action()
        self.back_col, self._alt_col = self._alt_col, self.back_col


    @property
    def alt_col(self):
        if self.selected:
            return self._back_col
        else:
            return self._alt_col
    @alt_col.setter
    def alt_col(self,new_alt_col):
        if self.selected:
            self._back_col = new_alt_col
        else:
            self._alt_col = new_alt_col
        self._needs_update = 1
    
    @property
    def selected(self):
        return super().selected
    @selected.setter
    def selected(self,value):
        if self._selected != value:
            self.back_col, self._alt_col = self._alt_col, self.back_col
        self._selected = value


class TextButton(Button):
    def __init__(self,SCREEN,pos,back_col,alt_col,text,scale,text_col="black",autodraw = True, autoclick=True):
        self.textClass = displays.WidgetsV2.MyText.Text(SCREEN,pos,back_col,text,text_col,scale)
        super().__init__(SCREEN,pos,self.textClass.WH,back_col,alt_col,autodraw=autodraw, autoclick=autoclick)


    @property
    def back_col(self):
        return self.textClass._back_col
    @back_col.setter
    def back_col(self,new_back_col):
        self.textClass._back_col = new_back_col
        self._needs_update = 1

    @property
    def text(self):
        return self.textClass.text
    @text.setter
    def text(self,new_text):
        self.textClass.text = new_text
        self._needs_update = 1

    @property
    def scale(self):
        return self.textClass.scale
    @scale.setter
    def scale(self,new_scale):
        self.textClass.scale = new_scale
        self._needs_update = 1

    @property
    def text_col(self):
        return self.textClass._text_col
    @text_col.setter
    def text_col(self,new_text_col):
        self.textClass._text_col = new_text_col
        self._needs_update = 1



    def draw(self):
        self.textClass.draw()


class CheckBox(Button):
    def __init__(self,SCREEN,pos,WH,back_col,cross_col, autodraw=True, autoclick=True):
        super().__init__(SCREEN,pos,WH,back_col,back_col,autodraw=autodraw,autoclick=autoclick)
        self.cross_col = cross_col

    def draw(self):
        super().draw()
        if self.selected:
            pygame.draw.line(self._SCREEN,self.cross_col,self.leadingRectCoords[0],self.leadingRectCoords[1])
            pygame.draw.line(self._SCREEN,self.cross_col,self.counterRectCoords[0],self.counterRectCoords[1])

