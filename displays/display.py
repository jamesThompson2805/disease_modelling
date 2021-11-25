
from displays import WidgetsV2
import displays
from displays.abstractDisplay import *
import MyColours


from displays.WidgetsV2 import MyButtons, MyClickable, MyWidget
from displays.WidgetsV2 import MyGraph
from displays.WidgetsV2 import MyGrid
from displays.WidgetsV2 import MySlider
from displays.WidgetsV2 import MySlidingText
from displays.WidgetsV2 import MyText
from displays.WidgetsV2 import MyTextBoxes
from displays.WidgetsV2 import MyPopup


class Display(AbstractDisplay):
    def __init__(self,SCREEN,back_col,additional_info):
        super().__init__(SCREEN)
        self._back_col = back_col

        pygame.display.set_caption("testing")

        self.buttons=[]

        self._next_display = None

    def initialise_display(self):
        self._info_for_next_display = ""
        self._running = True
        self._mouse_pos = [0,0]
        self.SCREEN.fill(self._back_col)
        while self._running:
            self.events()
            self.loop()
            self.render()
        self.cleanup()
        return self._next_display, self._info_for_next_display


    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self._mouse_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONDOWN:
                for clickable in MyClickable.Clickable.clickableObjects:
                    if clickable.in_bounds(self._mouse_pos):
                        clickable.action()

    def loop(self):
        pass
    def render(self):
        for widget in MyWidget.Widget.widgets:
            if widget.needs_update:
                widget.draw()
        self.manual_render()
        pygame.display.flip()
        
    def cleanup(self):
        MyClickable.Clickable.clickableObjects.clear()      
        MyWidget.Widget.widgets.clear()      

    def manual_render(self):
        pass
        


    @property
    def back_col(self):
        return self._back_col
    @back_col.setter
    def back_col(self,value):
        self._back_col = value
        self._SCREEN.fill(value)
        for widget in MyWidget.Widget.widgets:
            self._needs_update = 1


