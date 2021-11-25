from pygame import mouse
import pygame.draw

from displays.WidgetsV2.MyClickable import *
from displays.WidgetsV2.MyText import *

class SlidingText(Clickable):
    def __init__(self,SCREEN,pos,width,back_col,text_array,scale,autodraw = True,autoclick=True):
        self._text_array = text_array
        self._left_button = Text(SCREEN,pos,"white","<","black",scale)
        WH = (width,self._left_button.rectPos[3])
        right_pos = (pos[0]+width-self._left_button.rectPos[2],pos[1])
        self._right_button = Text(SCREEN,right_pos,"white",">","black",scale)

        super().__init__(SCREEN,pos,WH,back_col,autodraw=autodraw,autoclick=autoclick)

        self._max_text = round(width/(0.6*scale))
        self._max_text -= 2

        self._start = 0
        self._text = self.format_text_array(text_array)[self._start:self._max_text+self._start-1]
        text_pos = (
            self._left_button.rectPos[2]+self.pos[0],
            self.pos[1]
        )
        self._textBox = Text(SCREEN,
                             text_pos,
                             back_col,
                             self._text,
                             "black",
                             self._left_button.scale,
                             border=False,autodraw=False)


    def draw(self):
        super().draw()
        self._left_button.draw()
        self._right_button.draw()
        self._textBox.draw()


    def format_text_array(self,text_array):
        string = "|"
        for i in text_array:
            string = string + i + "|"
        while len(string)<self._max_text:
            string = string + " "
        return string

    @property
    def start(self):
        return self._start
    @start.setter
    def start(self,new_start):
        self._start = new_start
        self._text = self.format_text_array(self._text_array)[self._start:self._max_text+self._start-1]
        self._textBox.text = self._text
        self._needs_update = 1

    @property
    def text_array(self):
        return self._text_array
    @text_array.setter
    def text_array(self, value):
        self._text_array = value
        self._text = self.format_text_array(self._text_array)[self._start:self._max_text+self._start-1]
        self._textBox.text = self._text
        self._max_text = round(self.WH[0]/(0.6*self._textBox.scale))
        self._max_text -= 2*3
        self._needs_update = 1



    def action(self):
        super().action()
        mouse_pos = pygame.mouse.get_pos()
        if self._left_button.in_bounds(mouse_pos):
            if self.start > 0:
                self.start = self._start - 1
        elif self._right_button.in_bounds(mouse_pos):
            if self.start<len(self.format_text_array(self._text_array))-self._max_text+1:
                self.start = self._start + 1



class SlidingTexts(SlidingText):
    def __init__(self,SCREEN,pos,width,back_col,text_array,scale,colour_array, autodraw = True,autoclick=True):
        super().__init__(SCREEN,pos,width,back_col,text_array,scale,autodraw=autodraw,autoclick=autoclick)
        self._textBoxes = {text:0 for text in text_array}
        self._colour_array = colour_array
        self._textBox = Text(self.SCREEN,pos,back_col,"","black",self._left_button.scale,False,False)
        self.format_text_boxes(text_array)



    def format_text_boxes(self,text_array):
        self._textBoxes = {text:0 for text in text_array}
        text_array_lengths = [len(i) for i in text_array]
        last_pos = (self.pos[0]+self._left_button.rectPos[2],self.pos[1])
        for word_index in range(len(text_array)):
            list_sum = sum([text_array_lengths[i] for i in range(word_index)])
            list_sum_and_one = sum([text_array_lengths[i] for i in range(word_index+1)])
            if list_sum_and_one >= self.start:
                if list_sum-self.start <= self._max_text:
                    word_start = max(self.start - list_sum,0)
                    word_end = self._max_text-list_sum+self.start
                    text_to_add = text_array[word_index][word_start:word_end]
                    newText = Text(self.SCREEN,
                                   last_pos,
                                   self._colour_array[word_index],
                                   text_to_add,
                                   "black",
                                   self._left_button.scale,
                                   border=True,autodraw=False)
                    last_pos = (
                        last_pos[0]+newText.rectPos[2],
                        last_pos[1]
                    )
                    self._textBoxes[text_array[word_index]]=(newText)

    def draw(self):
        super().draw()
        for text in list(self._textBoxes.values()):
            if text:
                text.draw()


    @property
    def start(self):
        return self._start
    @start.setter
    def start(self,new_start):
        self._start = new_start
        self.format_text_boxes(self._text_array)
        self._needs_update = 1

    @property
    def text_array(self):
        return self._text_array
    @text_array.setter
    def text_array(self, value):
        self._text_array = value
        self._max_text = round(self.WH[0]/(0.6*self._textBox.scale))
        self._max_text -= 2*1
        self.format_text_boxes(value)
        self._needs_update = 1




    def action(self,offset=(0,0)):
        self._needs_update = 1
        self.selected = False if self.selected else True
        mouse_pos_act = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos_act[0]-offset[0],mouse_pos_act[1]-offset[1])
        if self._left_button.in_bounds(mouse_pos):
            if self.start > 0:
                self.start = self._start - 1
        elif self._right_button.in_bounds(mouse_pos):
            if self.start< sum([len(i) for i in self._text_array])-self._max_text:
                self.start = self._start + 1


class SlidingButtons(SlidingTexts):
    def __init__(self,SCREEN,pos,width,back_col,text_array,scale,colour_array,alt_colour_array, autodraw = True, only_one=True):
        super().__init__(SCREEN,pos,width,back_col,text_array,scale,colour_array,autodraw=autodraw)
        self.button_states = [0 for i in range(len(text_array))]
        self.alt_colours = alt_colour_array
        self.only_one = only_one

    def action(self):
        self._needs_update = 1
        self.selected = False if self.selected else True
        mouse_pos = pygame.mouse.get_pos()
        if self._left_button.in_bounds(mouse_pos):
            if self.start > 0:
                self.start = self._start - 1
        elif self._right_button.in_bounds(mouse_pos):
            if self.start<sum([len(i) for i in self._text_array])-self._max_text:
                self.start = self._start + 1
        else:
            for textIndex in range(len(self._textBoxes)):
                text = self._textBoxes[self._text_array[textIndex]]
                if text:
                    if text.in_bounds(mouse_pos):
                        self.button_states[textIndex] = 0 if self.button_states[textIndex] else 1
                    elif self.only_one:
                        self.button_states[textIndex]=0

    def draw(self):
        for textIndex in range(len(self.button_states)):
            if self.button_states[textIndex]:
                if self._textBoxes[self._text_array[textIndex]]:
                    self._textBoxes[self._text_array[textIndex]].back_col = self.alt_colours[textIndex]
            else:
                if self._textBoxes[self._text_array[textIndex]]:
                    self._textBoxes[self._text_array[textIndex]].back_col = self._colour_array[textIndex]
        super().draw()
