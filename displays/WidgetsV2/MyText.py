import pygame.font

import displays.WidgetsV2.MyWidget

class Text(displays.WidgetsV2.MyWidget.Widget):
    def __init__(self,SCREEN,pos,back_col,text,text_col,scale,border=True,autodraw = True):
        self.border = border
        WH = (
            int(0.6*scale*len(text)),
            int(1.14 * scale)
        )

        super().__init__(SCREEN,pos,WH,back_col,autodraw=autodraw)

        self._text = text
        self._scale = scale
        self._text_col = text_col

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,new_text):
        self._text = new_text
        self.WH = (
            int(0.6*self._scale*len(self._text)),
            int(1.14 * self._scale)
        )
        self._needs_update = 1


    @property
    def scale(self):
        return self._scale
    @scale.setter
    def scale(self,new_scale):
        self._scale = new_scale
        self.WH = (
            int(0.6*self._scale*len(self._text)),
            int(1.14 * self._scale)
        )
        self._needs_update = 1


    def draw(self):
        if self.border:
            super().draw()
        else:
            pygame.draw.rect(self.SCREEN,self.back_col,self.rectPos)
        font = pygame.font.SysFont("monospace",int(self._scale))
        text = font.render(self.text, True, self._text_col)
        self._SCREEN.blit(text, self.pos)




