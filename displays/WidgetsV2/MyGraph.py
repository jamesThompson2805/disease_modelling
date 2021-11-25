from pygame.constants import APPINPUTFOCUS
import pygame.draw

import displays.WidgetsV2.MyWidget
import displays.WidgetsV2.MyText

class PositiveGraph(displays.WidgetsV2.MyWidget.Widget):
    def __init__(self,SCREEN,pos,WH,back_col,autodraw = True):
        super().__init__(SCREEN,pos,WH,back_col,autodraw = autodraw)

        self._lines = []

        self._axis_coords = self.determine_axis()
        self._scales = [0,0,1,1]

    def add_line(self,line):
        self._needs_update = 1
        self._lines.append(line)
        self._scales = self.determine_scale()

    def determine_scale(self):
        minX = min([min(self._lines[i]._XY[0]) for i  in range(len(self._lines))])
        minY = min([min(self._lines[i]._XY[1]) for i  in range(len(self._lines))])
        maxX = max([max(self._lines[i]._XY[0]) for i  in range(len(self._lines))])
        maxY = max([max(self._lines[i]._XY[1]) for i  in range(len(self._lines))])
        return (minX,minY,maxX,maxY)

    def determine_axis(self):
        x_axis_coords = (
            (
                self.counterRectCoords[0][0]+10,
                self.counterRectCoords[0][1]-10
            ),
            (
                self.leadingRectCoords[1][0]-10,
                self.leadingRectCoords[1][1]-10
            )
        )
        y_axis_coords = (
            (
                self.counterRectCoords[0][0]+10,
                self.counterRectCoords[0][1]-10
            ),
            (
                self.leadingRectCoords[0][0]+10,
                self.leadingRectCoords[0][1]+10
            )
        )
        return (x_axis_coords,y_axis_coords)


    def draw(self):
        super().draw()

        pygame.draw.line(self._SCREEN,"red",self._axis_coords[0][0],self._axis_coords[0][1])
        pygame.draw.line(self._SCREEN,"green",self._axis_coords[1][0],self._axis_coords[1][1])

        for line in self._lines:
            pos1 = self.xy_to_pos((line.XY[0][0],line.XY[1][0]))
            for index in range(len(line.XY[0])-1):
                pos2 = self.xy_to_pos((line.XY[0][index+1],line.XY[1][index+1]))
                pygame.draw.line(self._SCREEN,line.line_col,pos1,pos2)
                pos1=pos2

    def xy_to_pos(self,xy):

        x_scalingFactor=(self._axis_coords[0][1][0]-self._axis_coords[0][0][0])/(self._scales[2]-self._scales[0])
        y_scalingFactor=(self._axis_coords[1][0][1]-self._axis_coords[1][1][1])/(self._scales[3]-self._scales[1])

        x = self._axis_coords[0][0][0] + (xy[0]-self._scales[0])*x_scalingFactor
        y = self._axis_coords[1][0][1] - (xy[1]-self._scales[1])*y_scalingFactor


        return (int(x),int(y))

    def add_line_points(self,lineThing,XY):
        self._needs_update = 1
        line = self._lines[self._lines.index(lineThing)]
        line._XY[0] = line._XY[0] + XY[0]
        line._XY[1] = line._XY[1] + XY[1]


        self.determine_scale()
        self.determine_axis()






class Line:
    def __init__(self,XY,line_col):
        self._XY = [XY[0],XY[1]]
        assert len(XY[0]) == len(XY[1]), "your points have undefined coords"
        self.line_col = line_col


    @property
    def XY(self):
        return self._XY

    def sort_line(self):
        ### MERGE SORT!!!
        pass



