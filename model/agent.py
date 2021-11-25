

from numpy.core.fromnumeric import trace
import random


class Agent:
    def __init__(self, pos, vacc, inf, cough_chance, trace_chance, grid, seat, door, cough_grid, trace_grid):
        self._pos = pos
        self._vacc_state = vacc
        self._inf_state = inf
        self.to_seat = self.calc_seat_path(grid, seat, door)
        self._movement_state = ("RS", len(self.to_seat)) # RS : reaching seat, SS : sit seat, LR: leaving room, OC : Out Classroom
        
        self.cough_grid = cough_grid
        self.trace_grid = trace_grid
        self.cough_chance = cough_chance
        self.trace_chance = trace_chance
        
    def calc_seat_path(self,grid,seat,door):
        pathing = AStar(door,seat,grid)
        return pathing.get_moves()[:]
    
    ### All beyond this point handled every tick
    def one_action(self):
        self.move()
        if self._inf_state:
            self.symptoms()
        else:
            self.calc_inf()
        
    def move(self):
        if self._movement_state[0] == "RS":
            self._movement_state[1]-=1
            self._pos = self.to_seat[self._movement_state[1]]
            if self._movement_state[1]==0:
                self._movement_state = ("SS",100)
    
    def symptoms(self):
        cough = random.random()
        trace = random.random()
        if cough < self.cough_chance:
            self.cough_grid.plus_one(self.pos)
        if trace < self.trace_chance:
            self.trace_grid[self._pos[1]][self._pos[0]] = 1
        
    def calc_inf(self):
        cough = random.random()
        trace = random.random()
        if cough < self.cough_grid[self._pos[1],self._pos[0]] and not self._vacc_state:
            self._inf_state = 1
        if trace < self.trace_grid[self._pos[1]][self._pos[0]] and not self._vacc_state:
            self._inf_state = 1

            
class AStar:
    def __init__(self,initial_pos,target_pos,grid):
        self.start = initial_pos
        self.target_pos = target_pos
        
        self.frontier = [initial_pos]
        self.came_from = {initial_pos:None}
        self.costs = {initial_pos:0}
        
        self.moves = []
        
        self.grid = grid
        
        self.current_pos = initial_pos
        
    def calc_dist(self,pos1,pos2):
        return ( (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2 )**0.5
        
    def calc_score(self,was_from,pos):
        return self.costs[was_from] + self.calc_dist(pos,was_from)
    
    def front_pri_push(self,cell,priority):
        inserted = False
        for i,el in enumerate(self.frontier):
            if priority <= self.costs[el]+self.calc_dist(el,self.target_pos):
                self.frontier.insert(i,cell)
                inserted = True
                break
        if not inserted:
            self.frontier.append(cell)
        

    def astar(self):
        while len(self.frontier)!=0:
            curr = self.frontier.pop(0)
            
            if curr == self.target_pos:
                break
            
            dirs = [1,0,-1,0]
            for i in range(4):
                next_pos = (curr[0]+dirs[i], curr[1]+dirs[(i+1)%4])
                if self.grid.in_bounds(next_pos):
                    score = self.calc_score(curr, next_pos)
                    if next_pos not in self.costs or score < self.costs[next_pos]:
                        self.came_from[next_pos] = curr
                        self.costs[next_pos] = score
                        priority = score + self.calc_dist(next_pos,self.target_pos)
                        self.front_pri_push(next_pos,priority)
                        
    def backtrack(self,target_pos):
        self.moves.append(target_pos)
        if self.came_from[target_pos] == None:
            return None
        else:
            self.backtrack(self.came_from[target_pos])
            
    def get_moves(self):
        self.astar()
        self.backtrack()
        
