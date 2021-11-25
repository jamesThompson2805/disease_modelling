from displays.display import *

class Results(Display):
    def __init__(self, SCREEN, back_col,add_info):
        super().__init__(SCREEN, back_col,add_info)

        pygame.display.set_caption("Results")


        self.buttons = [
        MyButtons.TextButton(
            self._SCREEN,
            (0,0),
            "red","blue",
            "Rmenu",20),
        MyButtons.TextButton(
            self._SCREEN,
            (0,22),
            "red","blue",
            "Rbuilder",20),
        MyButtons.TextButton(
            self._SCREEN,
            (0,44),
            "red","blue",
            "Rsim",20),
        MyButtons.TextButton(
            self._SCREEN,
            (0,66),
            "red","blue",
            "Uresults",20)]



    def loop(self):
        for button in self.buttons:
            if button.selected:
                self._running = False
                self._next_display = button.text
                button.selected = 0               