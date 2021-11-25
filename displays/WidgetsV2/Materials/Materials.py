from typing import Collection
import MyColours

class Mat:
    name = "blank"
    colour = MyColours.matColours["blank"]

    @classmethod
    def check_self(cls,pos,tiles):
        #checks for self if place in grid is valid
        return True

    @classmethod
    def check_and_place(cls,pos,tiles):
        if not cls.check_self(pos,tiles):
            return False
        temp = tiles[pos[1]][pos[0]]
        tiles[pos[1]][pos[0]] = Mat
        dirs=[1,0,-1,0]
        valid = True
        for i in range(4):
            if not tiles[dirs[(i+1)%4]][dirs[i]].check_self((i,(i+1)%4),tiles):
                valid = False
        tiles[pos[1]][pos[0]] = temp
        return valid


class Wall(Mat):
    name = "wall"
    colour = MyColours.matColours["wall"]

class WindowC(Wall):
    name = "windowC"
    colour = MyColours.matColours["window"]
class WindowS(Wall):
    name = "windowS"
    colour = MyColours.matColours["window"]
class WindowO(Wall):
    name = "windowO"
    colour = MyColours.matColours["window"]

class Door(Wall):
    name="door"
    colour = MyColours.matColours["door"]

class Floor(Mat):
    name="floor"
    colour = MyColours.matColours["floor"]

class OnFloor(Mat):
    @classmethod
    def check_self(cls, pos, tiles):
        if tiles[pos[1]][pos[0]].name == "floor":
            return True
        return False
    
class TeacherChairU(OnFloor):
    name="TchairU"
    colour = MyColours.matColours["Tchair"]
class TeacherChairD(OnFloor):
    name="TchairD"
    colour = MyColours.matColours["Tchair"]
class TeacherChairL(OnFloor):
    name="TchairL"
    colour = MyColours.matColours["Tchair"]
class TeacherChairR(OnFloor):
    name="TchairR"
    colour = MyColours.matColours["Tchair"]

class StudentChairU(OnFloor):
    name="SchairU"
    colour = MyColours.matColours["Schair"]
class StudentChairD(OnFloor):
    name="SchairD"
    colour = MyColours.matColours["Schair"]
class StudentChairL(OnFloor):
    name="SchairL"
    colour = MyColours.matColours["Schair"]
class StudentChairR(OnFloor):
    name="SchairR"
    colour = MyColours.matColours["Schair"]

class Desk(OnFloor):
    name="desk"
    colour = MyColours.matColours["desk"]






