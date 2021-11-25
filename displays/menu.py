from displays.display import *
import pygameWindow

class Menu(Display):
    def __init__(self, SCREEN, back_col,add_info):
        super().__init__(SCREEN, back_col,add_info)

        pygame.display.set_caption("Menu")

        
        self.title = MyText.Text(
            self._SCREEN,
            (156,100),
            MyColours.displayColours["menu"]["back_col"],
            "Classroom Sim",
            MyColours.textColours["grey"],
            40,border=False
        )

        self.GO = MyButtons.TextButton(
            self._SCREEN,
            (276,200),MyColours.stdColours["green"],
            MyColours.stdColours["green2"],"GO",40
        )

        self.QUIT = MyButtons.TextButton(
            self._SCREEN,
            (252,248),MyColours.stdColours["red"],
            MyColours.stdColours["red"],"QUIT",40
        )

    def loop(self):
        super().loop()
        if self.GO.selected:
            self._running = False
            self._next_display = "Lbuilder"
        elif self.QUIT.selected:
            self._running = False
            self._next_display = "quit"


