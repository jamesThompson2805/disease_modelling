
import displays.WidgetsV2.MyWidget

class Clickable(displays.WidgetsV2.MyWidget.Widget):
    clickableObjects=[]

    def __init__(self,SCREEN,pos,WH,back_col,autodraw = True,autoclick = True):
        super().__init__(SCREEN,pos,WH,back_col,autodraw=autodraw)

        self._selected = False
        if autoclick:
            Clickable.clickableObjects.append(self)


    def action(self):
        self._needs_update = 1
        self._selected = False if self.selected else True

    @property
    def selected(self):
        return self._selected
    @selected.setter
    def selected(self,value):
        self._selected = value
