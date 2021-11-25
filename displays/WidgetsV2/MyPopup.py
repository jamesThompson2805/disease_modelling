import pygame
from pygame.image import save
from pygame.locals import *
import sys

from displays.WidgetsV2 import MyButtons,MyText,MySlidingText,MyTextBoxes,MyWidget


class Popup:
    def __init__(self, SCREEN, pos, WH, back_col, screen_col, title="A popup"):
        self._SCREEN = SCREEN
        self.widget_screen = pygame.Surface(WH,pygame.SRCALPHA,32)
        self.widget_screen.fill(back_col)

        self._pos = pos
        self._WH = WH
        self._rectPos = (self._pos[0],self._pos[1],self._WH[0],self._WH[1])

        self._back_col = back_col
        self._screen_col = screen_col
        self.popup_widgets = []
        self.popup_clickables = []

        white_bar = MyWidget.Widget(
            self.widget_screen, (0,0),
            (WH[0],1.16*10),"white",autodraw=False
        )
        self.popup_widgets.append(white_bar)
        titleBox = MyText.Text(
            self.widget_screen,(0,0),"white",title,
            "black",10,border=False,autodraw=False
        )
        self.popup_widgets.append(titleBox)

        self.X = MyButtons.TextButton(
            self.widget_screen,
            (WH[0]-0.6*3*10,0),
            "red","red"," X ",10,autodraw=False,autoclick=False
        )


        self.selected = False


    def draw(self):
        for widget in self.popup_widgets:
            if widget.needs_update:
                widget.draw()
        if self.X.needs_update:
            self.X.draw()
        self._SCREEN.blit(self.widget_screen,self._pos)
        pygame.draw.rect(self._SCREEN, "black", self._rectPos,1)
    
    def while_selected(self):
        self.mouse_pos = [0,0]
        while self.selected:
            self.events()
            self.loop()
            self.render()
        self.cleanup()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mouse_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONDOWN:
                relative_mouse = (self.mouse_pos[0]-self._pos[0], self.mouse_pos[1]-self._pos[1])
                if not self.in_bounds(self.mouse_pos):
                    self.selected = False
                elif self.X.in_bounds(relative_mouse):
                    self.selected = False
                    self.X.selected = False
                for clickable in self.popup_clickables:
                    if clickable.in_bounds(relative_mouse):
                        if type(clickable) == MySlidingText.SlidingTexts:
                            clickable.action(self._pos)
                        else:
                            clickable.action()

    def in_bounds(self,mouse_pos):
        if mouse_pos[0]>self._rectPos[0] and mouse_pos[1]>self._rectPos[1]:
            if mouse_pos[0]<self._rectPos[0]+self._rectPos[2]:
                if mouse_pos[1]<self._rectPos[1]+self._rectPos[3]:
                    return True
        return False

    def loop(self):
        pass
    def render(self):
        self.draw()
        pygame.display.flip()

    def cleanup(self):
        for widget in MyWidget.Widget.widgets:
            widget._needs_update = True
        self._SCREEN.fill(self._screen_col)


class SavePopup(Popup):
    def __init__(self, SCREEN, back_col, screen_col):
        WH = (200,100)
        pos = ((SCREEN.get_width()-200)/2,(SCREEN.get_height()-100)/2)
        super().__init__(SCREEN, pos, WH, back_col, screen_col,title="Save")

        savetext = MySlidingText.SlidingTexts(
            self.widget_screen,(10,30),180,self._back_col,
            ["Enter filename of save (+ .txt)"],20,[self._back_col],
            autodraw=False,
        autoclick=False
        )
        self.popup_widgets.append(savetext)
        self.popup_clickables.append(savetext)

        self.filebox = MyTextBoxes.PopupTextBox(
            self._SCREEN, (10,55),
            self.widget_screen, self._pos,self._screen_col,
            self._back_col,15,20,autodraw=False,autoclick=False,
            allowed_uni_ranges=[(48,57),(65,90),(97,122)]
        )
        self.popup_widgets.append(self.filebox)
        self.popup_clickables.append(self.filebox)

        self.exit_button = MyButtons.TextButton(
            self.widget_screen, (80,75),self._screen_col,
            self._back_col,"Save",20,autodraw=False,autoclick=False
        )
        self.popup_widgets.append(self.exit_button)
        self.popup_clickables.append(self.exit_button)

    def loop(self):
        super().loop()
        if self.exit_button.selected:
            self.selected = False
            self.exit_button.selected = False
    
    def while_selected(self):
        super().while_selected()
        return self.filebox.text.strip(" ")


class LoadPopup(Popup):
    def __init__(self, SCREEN, back_col, screen_col, ):
        WH = (200,100)
        pos = ((SCREEN.get_width()-200)/2,(SCREEN.get_height()-100)/2)

        super().__init__(SCREEN, pos, WH, back_col, screen_col, title="Load")
        loadtext = MySlidingText.SlidingTexts(
            self.widget_screen,(10,30),180,self._back_col,
            ["Enter filename to load (+ .txt)"],20,[self._back_col],
            autodraw=False,autoclick=False
        )
        self.popup_widgets.append(loadtext)
        self.popup_clickables.append(loadtext)

        self.filebox = MyTextBoxes.PopupTextBox(
            self._SCREEN, (10,55),
            self.widget_screen, self._pos,self._screen_col,
            self._back_col,15,20,autodraw=False,autoclick=False,
            allowed_uni_ranges=[(48,57),(65,90),(97,122)]
        )
        self.popup_widgets.append(self.filebox)
        self.popup_clickables.append(self.filebox)

        self.exit_button = MyButtons.TextButton(
            self.widget_screen, (80,75),self._screen_col,
            self._back_col,"Load",20,autodraw=False,autoclick=False
        )
        self.popup_widgets.append(self.exit_button)
        self.popup_clickables.append(self.exit_button)

    def loop(self):
        super().loop()
        if self.exit_button.selected:
            self.selected = False
            self.exit_button.selected = False
    
    def while_selected(self):
        super().while_selected()
        return self.filebox.text.strip(" ")

class ErrorPopup(Popup):
    def __init__(self, SCREEN, back_col, screen_col,error_message = "Unspecified error"):
        WH = (200,100)
        pos = ((SCREEN.get_width()-200)/2,(SCREEN.get_height()-100)/2)
        super().__init__(SCREEN, pos, WH, back_col, screen_col, title="Error")

        self.errortext = MySlidingText.SlidingTexts(
            self.widget_screen,(10,30),180,self._back_col,
            [error_message],20,["pink"],
            autodraw=False,autoclick=False
        )
        self.popup_widgets.append(self.errortext)
        self.popup_clickables.append(self.errortext)

        self._errormessage = error_message

        self.exit_button = MyButtons.TextButton(
            self.widget_screen, (80,75),self._screen_col,
            self._back_col,"Exit",20,autodraw=False,autoclick=False
        )
        self.popup_widgets.append(self.exit_button)
        self.popup_clickables.append(self.exit_button)

    def loop(self):
        super().loop()
        if self.exit_button.selected:
            self.selected = False
            self.exit_button.selected = False

    @property
    def errormessage(self):
        return self._errormessage

    @errormessage.setter
    def errormessage(self,new):
        self._errormessage = new
        self.errortext.text_array = [new]