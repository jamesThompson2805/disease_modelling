from pygame.image import load
from displays.WidgetsV2 import MyPopup
from displays.display import *
from displays.WidgetsV2.Materials.Materials import *


class Builder(Display):
    def __init__(self, SCREEN, back_col,add_info):
        super().__init__(SCREEN, back_col,add_info)


        pygame.display.set_caption("Builder")
        
        self.grid = MyGrid.Grid(
            self.SCREEN,(5,5),
            (360,300),36,30,
            MyColours.displayColours["blank"]["back_col"]
        )

        self.materials_bar = MySlidingText.SlidingButtons(
            self._SCREEN,
            (5,325),489,MyColours.displayColours["blank"]["back_col"],
            ["Eraser","Wall","Window","Door","Floor","Desk","Student chair","Teacher chair"],
            20,
            [
                MyColours.displayColours["blank"]["back_col"] for i in range(8)
            ],
            [
                MyColours.matColours["eraser"],
                MyColours.matColours["wall"],
                MyColours.matColours["window"],
                MyColours.matColours["door"],
                MyColours.matColours["floor"],
                MyColours.matColours["desk"],
                MyColours.matColours["Schair"],
                MyColours.matColours["Tchair"],
            ]
        )

        self.conditions_bar = MySlidingText.SlidingButtons(
            self._SCREEN,
            (5,350),489,MyColours.displayColours["blank"]["back_col"],
            ["Masks","Wipe surfaces","Vaccinations"],
            20,
            [
                MyColours.stdColours["red"] for i in range(3)
            ],
            [
                MyColours.stdColours["green"] for i in range(3)
            ],only_one=False
        )


        self.menu_button = MyButtons.TextButton(
            self._SCREEN,(499,302),
            MyColours.stdColours["red"],
            MyColours.stdColours["red2"],
            "Exit",40,MyColours.textColours["grey"]
        )

        self.sim_button = MyButtons.TextButton(
            self._SCREEN,(499,350),
            MyColours.stdColours["green"],
            MyColours.stdColours["green2"],
            "Run!",40,MyColours.textColours["grey"]
        )

        self.back_text = MyWidget.Widget(
            self.SCREEN,
            (375,5),(220,290),
            MyColours.stdColours["white"])

        self.cough_chance = [
            MyText.Text(
                self.SCREEN,(380,10),
                MyColours.stdColours["white"],
                "Cough chance",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,10),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,1),MyColours.textColours["grey"]
            )
        ]

        self.trace_chance = [
            MyText.Text(
                self.SCREEN,(380,35),
                MyColours.stdColours["white"],
                "Trace chance",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,35),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,1),MyColours.textColours["grey"]
            )
        ]

        self.student_inf_start = [
            MyText.Text(
                self.SCREEN,(380,60),
                MyColours.stdColours["white"],
                "Student inf.",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,60),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,1),MyColours.textColours["grey"]
            )
        ]

        self.teacher_inf_start = [
            MyText.Text(
                self.SCREEN,(380,85),
                MyColours.stdColours["white"],
                "Teacher inf.",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,85),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,1),MyColours.textColours["grey"]
            )
        ]

        self.ceiling_height = [
            MyText.Text(
                self.SCREEN,(380,110),
                MyColours.stdColours["white"],
                "Ceiling ht. ",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,110),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,7),MyColours.textColours["grey"]
            )
        ]
        self.vacc_perc = [
            MyText.Text(
                self.SCREEN,(380,135),
                MyColours.stdColours["white"],
                "Vaccinated %",
                MyColours.textColours["grey"],20
            ),
            MyTextBoxes.NumTextBoxWithBounds(
                self.SCREEN,(530,135),
                MyColours.displayColours["builder"]["back_col"],
                MyColours.stdColours["white"],
                20,5,(0,100),MyColours.textColours["grey"]
            )
        ]



        self.undo = MyButtons.TextButton(
            self.SCREEN,
            (380,220),MyColours.displayColours["builder"]["back_col"]
            ,MyColours.displayColours["builder"]["back_col"],"Undo",20,
            MyColours.textColours["grey"]
        )
        self.redo = MyButtons.TextButton(
            self.SCREEN,
            (495,220),MyColours.displayColours["builder"]["back_col"]
            ,MyColours.displayColours["builder"]["back_col"],"Redo",20,
            MyColours.textColours["grey"]
        )        
        self.clear = MyButtons.TextButton(
            self.SCREEN,
            (380,245),MyColours.displayColours["builder"]["back_col"]
            ,MyColours.displayColours["builder"]["back_col"],"Clear",20,
            MyColours.textColours["grey"]
        )
        self.save = MyButtons.TextButton(
            self.SCREEN,
            (380,270),MyColours.displayColours["builder"]["back_col"]
            ,MyColours.displayColours["builder"]["back_col"],"Save",20,
            MyColours.textColours["grey"]
        )
        self.load = MyButtons.TextButton(
            self.SCREEN,
            (495,270),MyColours.displayColours["builder"]["back_col"]
            ,MyColours.displayColours["builder"]["back_col"],"Load",20,
            MyColours.textColours["grey"]
        )
        self.savepopup = MyPopup.SavePopup(
            self.SCREEN,
             "white",
             MyColours.displayColours["builder"]["back_col"]
        )
        self.loadpopup = MyPopup.LoadPopup(
            self.SCREEN,
             "white",
             MyColours.displayColours["builder"]["back_col"]
        )
        self.errorpopup = MyPopup.ErrorPopup(
            self.SCREEN, "white",
            MyColours.displayColours["builder"]["back_col"],
        )





    def loop(self):
        if self.menu_button.selected:
            self._running = False
            self._next_display = "Rmenu"
        elif self.sim_button.selected:
            self._running = False
            self._next_display = "Lsim"
        elif self.clear.selected:
            self.clear_grid()
        elif self.save.selected:
            self.save_all()
            self.savepopup.selected = 1
            self.save.selected = 0
        elif self.load.selected:
            self.loadpopup.selected = 1
            self.load.selected = 0
        elif self.undo.selected:
            self.grid.undo()
            self.undo.selected = 0
        elif self.redo.selected:
            self.grid.redo()
            self.redo.selected = 0

    def manual_render(self):
        if self.savepopup.selected:
            saveFileName = self.savepopup.while_selected()
            if len(saveFileName)==0:
                pass
            else:
                savefile = open("saves/"+saveFileName+".txt", "w")
                savefile.write(self.save_string)
                savefile.close()

        elif self.loadpopup.selected:
            loadFileName=self.loadpopup.while_selected()
            print(loadFileName)
            if len(loadFileName)==0:
                pass
            else:
                loadfile = open("saves/"+loadFileName+".txt", "r")
                loadtext = loadfile.read()
                if loadtext == "":
                    self.errorpopup.errormessage="Invalid file"
                    self.errorpopup.selected=1
                else:
                    self.load_all(loadtext)
                loadfile.close()
        elif self.errorpopup.selected:
            self.errorpopup.while_selected()


    def events(self):
        super().events()
        if self.materials_bar.in_bounds(self._mouse_pos):
            if self.materials_bar.button_states[0]:
                self.grid.selected_mat = Mat
            elif self.materials_bar.button_states[1]:
                self.grid.selected_mat = Wall
            elif self.materials_bar.button_states[2]:
                self.grid.selected_mat = WindowC
            elif self.materials_bar.button_states[3]:
                self.grid.selected_mat = Door
            elif self.materials_bar.button_states[4]:
                self.grid.selected_mat = Floor
            elif self.materials_bar.button_states[5]:
                self.grid.selected_mat = Desk
            elif self.materials_bar.button_states[6]:
                self.grid.selected_mat = StudentChairU
            elif self.materials_bar.button_states[7]:
                self.grid.selected_mat = TeacherChairU



    def clear_grid(self):
        self.clear.selected = 0
        self.grid.tiles = [[Mat for i in range(self.grid._CR[0])] for j in range(self.grid._CR[1])]
        self.grid.desks = []
        self.grid.student_chairs = []
        self.grid.teacher_chairs = []
        self.grid.doors = []
        

    def save_all(self):
        self.save_string=""
        list_to_string=lambda x: "|".join([str(i) for i in x])
        self.save_string+=list_to_string(self.conditions_bar.button_states)+"\n"
        parameters = [
            self.cough_chance[1].num,
            self.trace_chance[1].num,
            self.student_inf_start[1].num,
            self.teacher_inf_start[1].num,
            self.ceiling_height[1].num,
            self.vacc_perc[1].num
        ]
        self.save_string+=list_to_string(parameters)+"\n"
        self.save_string += self.grid.save_state()
        
    def load_all(self,load_string):
        save_sections = load_string.split("\n")
        self.conditions_bar.button_states = [int(i) for i in save_sections.pop(0).split("|")]
        self.conditions_bar._needs_update = True
        parameters = [float(i) for i in save_sections.pop(0).split("|")]
        self.cough_chance[1].num = parameters.pop(0)
        self.trace_chance[1].num = parameters.pop(0)
        self.student_inf_start[1].num = parameters.pop(0)
        self.teacher_inf_start[1].num = parameters.pop(0)
        self.ceiling_height[1].num = parameters.pop(0)
        self.vacc_perc[1].num = parameters.pop(0)
        grid_string = "\n".join(save_sections)
        self.grid.load_state(grid_string)
        
        
        
    def cleanup(self):
        super().cleanup()
        self.save_all()
        self._info_for_next_display = self.save_string
