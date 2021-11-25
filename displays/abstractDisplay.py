import pygame
from pygame.locals import *
import sys
from abc import ABC, abstractmethod

class AbstractDisplay(ABC): # the class is a subclass of the metaclass ABC
    def __init__(self,SCREEN):
        self._SCREEN = SCREEN
        pygame.display.set_caption("testing")

    @property # defines a getter for self.SCREEN
    def SCREEN(self):
        return self._SCREEN
    
    @property
    def backCol(self):
        return self._backCol        
    
    @abstractmethod # declares that the function below is ...
    def initialise_display(self): # ... an abstract method
        pass