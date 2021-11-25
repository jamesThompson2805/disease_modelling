import pygame
from pygame.locals import *
import sys

import displays.WidgetsV2.MyClickable


class Interactable(displays.WidgetsV2.MyClickable.Clickable):
    def __init__(self,SCREEN,pos,WH,back_col,autodraw = True,autoclick=True):
        super().__init__(SCREEN,pos,WH,back_col,autodraw=autodraw,autoclick=autoclick)

    def action(self):
        super().action()
        self.selected_mouse_pos = pygame.mouse.get_pos()

        while self.selected:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.selected = False
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEMOTION:
                    self.selected_mouse_pos = pygame.mouse.get_pos()

                elif event.type == MOUSEBUTTONDOWN:
                    if not self.in_bounds(self.selected_mouse_pos):
                        self.selected = False
                    self.additional_mouse_down(event)

                elif event.type == MOUSEBUTTONUP:
                    self.additional_mouse_up(event)

                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        self.selected = False
                    self.additional_key_handling(event)

            self.draw()
            self.additional_selected_loop()
            pygame.display.flip()

    def additional_selected_init(self):
        pass

    def additional_key_handling(self,event):
        pass

    def additional_mouse_down(self,event):
        pass

    def additional_mouse_up(self,event):
        pass

    def additional_selected_loop(self):
        pass