from typing import Text
import displays.WidgetsV2.MyInteractable

import displays.WidgetsV2.MyText


class TextBox(displays.WidgetsV2.MyInteractable.Interactable):
    def __init__(self,screen,pos,back_col,alt_col,text_scale,max_text,text_col="black",start_text="",autodraw = True,autoclick=True):
        text = " "*max(0,max_text-len(str(start_text))) + str(start_text)[:max_text]
        self._alt_col = alt_col
        self.textClass = displays.WidgetsV2.MyText.Text(screen,pos,back_col,text,text_col,text_scale)

        super().__init__(screen,pos,self.textClass.WH,back_col,autodraw=autodraw,autoclick=autoclick)

    def draw(self):
        super().draw()
        self.textClass.draw()

    def action(self):
        self.back_col, self.alt_col = self.alt_col, self.back_col
        super().action()
        self.back_col, self.alt_col = self.alt_col, self.back_col

    def additional_key_handling(self,event):
        if event.unicode == "":
            pass

        elif ord(event.unicode) == 8:
            self.textClass._text = self.textClass._text[:-1]
            self.textClass._text = " " + self.textClass._text

        elif ord(event.unicode)<127 and ord(event.unicode)>31:
            self.textClass._text = self.textClass._text[1:]
            self.textClass._text += event.unicode

    @property
    def back_col(self):
        return self.textClass._back_col
    @back_col.setter
    def back_col(self,new_back_col):
        self.textClass._back_col = new_back_col
        self._needs_update = 1


    @property
    def alt_col(self):
        return self._alt_col
    @alt_col.setter
    def alt_col(self,new_alt_col):
        self._alt_col = new_alt_col
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


    @property
    def text(self):
        return self.textClass._text


class NumTextBox(TextBox):
    def __init__(self,screen,pos,back_col,alt_col,text_scale,max_text,text_col="black",start_text = "0"):
        super().__init__(screen,pos,back_col,alt_col,text_scale,max_text,text_col,start_text)

    def additional_key_handling(self,event):
        if event.unicode == "":
            pass

        elif ord(event.unicode) == 8:  # backspace
            self.textClass._text = self.textClass._text[:-1]
            self.textClass._text = " " + self.textClass._text

        elif ord(event.unicode) == 45: # minus sign
            if self.textClass._text[-1]==" ":
                self.textClass._text = self.textClass._text[1:]
                self.textClass._text += event.unicode

        elif ord(event.unicode) == 46: # fullstop
            if "." not in self.textClass._text:
                self.textClass._text = self.textClass._text[1:]
                self.textClass._text += event.unicode

        elif ord(event.unicode)<=57 and ord(event.unicode)>=48:
            self.textClass._text = self.textClass._text[1:]
            self.textClass._text += event.unicode

    @property
    def num(self):
        numStr = self.text.lstrip(" ")
        numStr = "0" if numStr=="-" or numStr=="" or numStr=="." or numStr=="-." else numStr
        return float(numStr)
    @num.setter
    def num(self,new_num):
        self.textClass._text = str(new_num)[:len(self.text)-1]        


class NumTextBoxWithBounds(NumTextBox):
    def __init__(self,screen,pos,back_col,alt_col,text_scale,max_text,hard_bounds,text_col="black",):
        midpoint = (hard_bounds[1]+hard_bounds[0])/2
        assert hard_bounds[0]<hard_bounds[1], "just how???"
        self._bounds = hard_bounds
        self._max_text = max_text
        super().__init__(screen,pos,back_col,alt_col,text_scale,max_text,text_col,midpoint)

    def additional_key_handling(self,event):
        if event.unicode == "":
            pass

        # TODO: Errors in predicting next number for backspace and decimal points

        elif ord(event.unicode) == 8:  # backspace
            if float(str(self.num)[:-1]) >= self._bounds[0]:
                self.textClass._text = self.textClass._text[:-1]
                self.textClass._text = " " + self.textClass._text

        elif ord(event.unicode) == 45: # minus sign
            if self.textClass._text[-1]==" ":
                if self._bounds[0]<=0:
                    self.textClass._text = self.textClass._text[1:]
                    self.textClass._text += event.unicode

        elif ord(event.unicode) == 46: # fullstop
            if "." not in self.textClass._text:
                self.textClass._text = self.textClass._text[1:]
                self.textClass._text += event.unicode

        elif ord(event.unicode)<=57 and ord(event.unicode)>=48:
            if self.text.lstrip(" ") == "":
                future_num = float(event.unicode)
            elif self.text.lstrip(" ") == "-":
                future_num = -1*float(event.unicode)
            elif len(self.text.lstrip(" ")) == self._max_text:
                future_num = float(self.text.lstrip(" ")[1:] + event.unicode)
            else:
                future_num = float(self.text.lstrip(" ")+event.unicode)

            if future_num >= self._bounds[0]:
                if future_num <= self._bounds[1]:
                    self.textClass._text = self.textClass._text[1:]
                    self.textClass._text += event.unicode



class PopupTextBox(TextBox):
    def __init__(self,screen,pos,surface,surface_pos,back_col,alt_col,text_scale,max_text,text_col="black",start_text="",autodraw = True,autoclick=True,allowed_uni_ranges=[]):
        super().__init__(surface, pos, back_col, alt_col, text_scale, max_text, text_col=text_col, start_text=start_text, autodraw=autodraw, autoclick=autoclick)
        self.screen = screen
        self.surface_pos = surface_pos
        self.allowed_ranges = allowed_uni_ranges

    def additional_selected_loop(self):
        self.screen.blit(self.SCREEN,self.surface_pos)

    def additional_key_handling(self, event):
        if event.unicode!="":
            if ord(event.unicode)==8:
                super().additional_key_handling(event)
            for uni_range in self.allowed_ranges:
                if ord(event.unicode)>=uni_range[0] and ord(event.unicode)<=uni_range[1]:
                    super().additional_key_handling(event)
