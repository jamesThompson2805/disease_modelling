import pygame
from displays.display import *
import displays.menu
import displays.builder
import displays.sim
import displays.results

import displays.WidgetsV2.MyWidget

pygame.init()


import math

class Window:
    def __init__(self,wh):
        self._wh = wh
        self.__SCREEN = pygame.display.set_mode(wh)

        icon = pygame.image.load("virus_cell.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Classroom Disease Model")
        
        self.application = True
        self.display_info = {
            "menu":{
                "display":displays.menu.Menu,
                "back_col":MyColours.displayColours["menu"]["back_col"],
                "transition":MyColours.displayColours["menu"]["transition"]},
            "builder":{
                "display":displays.builder.Builder,
                "back_col":MyColours.displayColours["builder"]["back_col"],
                "transition":MyColours.displayColours["builder"]["transition"]},
            "sim":{
                "display":displays.sim.Sim,
                "back_col":MyColours.displayColours["sim"]["back_col"],
                "transition":MyColours.displayColours["sim"]["transition"]},
            "results":{
                "display":displays.results.Results,
                "back_col":MyColours.displayColours["results"]["back_col"],
                "transition":MyColours.displayColours["results"]["transition"]},
            "quit":{
                "back_col":MyColours.stdColours["red"],
                "transition":MyColours.stdColours["red2"]
            }
}
    
    def run(self):
        next_display = "menu"

        self.transition("U","menu")
        self.display = self.display_info[next_display]["display"](self.__SCREEN,self.display_info[next_display]["back_col"],"")
        next_display, info_for_next = self.display.initialise_display()
        while self.application:
            self.display = self.create_display(next_display,info_for_next)
            next_display, info_for_next = self.display.initialise_display()


    def create_display(self,next_display,info_for_next):
        if next_display == "quit":
            self.transition("D",next_display)
            pygame.quit()
            sys.exit()
        else:
            direction = next_display[0]
            next_display = next_display[1:]
            self.transition(direction,next_display)
        return self.display_info[next_display]["display"](self.__SCREEN,self.display_info[next_display]["back_col"],info_for_next)


    def transition(self,direction,next_display):
        step = 0
        steps = 2500
        while step <= math.pi/2:
            if direction == "R":
                rectTuple = (
                    self._wh[0]-self._wh[0]*math.sin(step),
                    0,
                    self._wh[0]*math.sin(step)+1,
                    self._wh[1]
                )
            elif direction == "L":
                rectTuple = (
                    0,
                    0,
                    self._wh[0]*math.sin(step),
                    self._wh[1]
                )
            elif direction == "D":
                rectTuple = (
                  0,
                  0,
                  self._wh[0],
                  self._wh[1]*math.sin(step)  
                )
            else:
                rectTuple = (
                  0,
                  self._wh[1]-self._wh[1]*math.sin(step),
                  self._wh[0],
                  self._wh[1]*math.sin(step)  
                )                
            pygame.draw.rect(self.__SCREEN,self.display_info[next_display]["transition"],rectTuple)
            pygame.display.flip()
            step+=math.pi/(steps*2)
        self.fade(self.display_info[next_display]["transition"],self.display_info[next_display]["back_col"])


    def fade(self,current_col,target_col):
        step = 0
        r_diff = target_col[0]-current_col[0]
        g_diff = target_col[1]-current_col[1]
        b_diff = target_col[2]-current_col[2]
        steps = (r_diff + g_diff + b_diff)*5
        while step<=steps:
            fade_col = (
                int(current_col[0]+r_diff*(step/steps)),
                int(current_col[1]+g_diff*(step/steps)),
                int(current_col[2]+b_diff*(step/steps))
            )
            pygame.draw.rect(self.__SCREEN,fade_col,(0,0,self._wh[0],self._wh[1]))
            pygame.display.flip()
            step+=1
            
            
