from displays.display import *

class Sim(Display):
    def __init__(self, SCREEN, back_col,add_info):
        super().__init__(SCREEN, back_col,add_info)

        pygame.display.set_caption("Simulation")

        self.grid = MyGrid.Grid(
            self.SCREEN,(5,5),
            (360,300),36,30,
            MyColours.displayColours["blank"]["back_col"]
        )

        self.materials_bar = MySlidingText.SlidingTexts(
            self._SCREEN,
            (5,325),489,MyColours.displayColours["blank"]["back_col"],
            ["door","wall","window","desk","student chair","teacher chair"],
            20,
            [
                "white","white","white",
                "white","white","white"
            ],
        )

        self.parameters_bar = MySlidingText.SlidingTexts(
            self._SCREEN,
            (5,350),489,MyColours.displayColours["blank"]["back_col"],
            ["Open windows","Masks","Wipe surfaces","Vaccinations"],
            20,
            [
                MyColours.stdColours["red"] for i in range(4)
            ]
        )

        self.builder_button = MyButtons.TextButton(
            self._SCREEN,(499,302),
            MyColours.stdColours["red"],
            MyColours.stdColours["red2"],
            "Exit",40,MyColours.textColours["grey"]
        )

        self.pause_button = MyButtons.TextButton(
            self._SCREEN,(499,350),
            MyColours.stdColours["green"],
            MyColours.stdColours["green2"],
            " || ",40,MyColours.textColours["grey"]
        )

        self.back_text = MyWidget.Widget(
            self.SCREEN,
            (375,5),(220,290),
            MyColours.stdColours["white"])

        self.graph = MyGraph.PositiveGraph(
            self.SCREEN,(380,10),
            (210,100),MyColours.stdColours["white"],
        )

        self.time = MyText.Text(
            self.SCREEN,
            (380,115),MyColours.stdColours["white"],
            "00:00",MyColours.textColours["grey"],
            40,border=False
        )
        self.days = MyText.Text(
            self.SCREEN,(505,115),
            MyColours.stdColours["white"],
            "days:    00",MyColours.textColours["grey"],
            12,border=False
        )
        self.lessons = MyText.Text(
            self.SCREEN,(505,130),
            MyColours.stdColours["white"],
            "lessons: 00",MyColours.textColours["grey"],
            12,border=False
        )


    def loop(self):
        if self.builder_button.selected:
            self._running = False
            self._next_display = "Rbuilder"




