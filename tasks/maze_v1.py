
#Every state is a potential terminal state
import math
import numpy as np
from numpy.random import random_integers as rnd
import matplotlib.pyplot as plt

class MazeMDP(object):
    #True are obstacles
    def make_maze(self, width=21, height=21, complexity=.05, density =.1): 
        # Only odd shapes
        shape = ((height//2)*2+1, (width//2)*2+1)
        # Adjust complexity and density relative to maze size
        complexity = int(complexity*(5*(shape[0]+shape[1])))
        density    = int(density*(shape[0]//2*shape[1]//2))
        # Build actual maze
        Z = np.zeros(shape, dtype=bool)
        # Fill borders
        Z[0,:] = Z[-1,:] = 1
        Z[:,0] = Z[:,-1] = 1
        # Make isles
        for i in range(density):
            x, y = rnd(0,shape[1]//2)*2, rnd(0,shape[0]//2)*2
            Z[y,x] = 1
            for j in range(complexity):
                neighbours = []
                if x > 1:           neighbours.append( (y,x-2) )
                if x < shape[1]-2:  neighbours.append( (y,x+2) )
                if y > 1:           neighbours.append( (y-2,x) )
                if y < shape[0]-2:  neighbours.append( (y+2,x) )
                if len(neighbours):
                    y_,x_ = neighbours[rnd(0,len(neighbours)-1)]
                    if Z[y_,x_] == 0:
                        Z[y_,x_] = 1
                        Z[y_+(y-y_)//2, x_+(x-x_)//2] = 1
                        x, y = x_, y_
        return Z, width, height

    def __init__(self):
        self.maze, self.width, self.height = self.make_maze()
        self.start_loc = np.array([0,0])
        x,y = np.where(self.maze == True)
        non_term_vars = np.zeros_like(x)
        self.obstacles = np.squeeze(np.array([[x],[y],[non_term_vars]])).T
        x,y = np.where(self.maze == False)
        non_term_vars = np.zeros_like(x)
        self.valid_points = np.squeeze(np.array([[x],[y],[non_term_vars]])).T

        #self.show_path(self.valid_points)
        #point = np.array([20,25])
        #plt.imshow(self.maze, cmap=plt.cm.binary,interpolation='nearest')
        #plt.scatter(point[1], point[0], s=7, c='g')
        #plt.savefig('maze_point.png')
        #self.maze[point[0],point[1]] = True
        #self.maze[point[0]-1,point[1]] = True
        #valid_point = self.get_valid_loc_near(point)
        ##plt.imshow(self.maze, cmap=plt.cm.binary,interpolation='nearest')
        #plt.scatter(valid_point[1], valid_point[0], s=7, c='b')
        #plt.savefig('maze_point.png')
        #self.goal_loc = self.maxRanges
        ##plt.show()
        

    def show_path(self, points, color = 'r', name = 'curr', stayAwake = False):
        plt.imshow(self.maze, cmap=plt.cm.binary,interpolation='nearest')
        plt.scatter(points[:,1], points[:,0], s=7, c=color)
        plt.savefig(name + '_maze_path.png')

        if not stayAwake:
            plt.close()

    def get_next_states(self, state):
        x,y,term = state
        states = np.array([(nx, ny, 0) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.height and 0 <= ny < self.width and self.maze[nx][ny] == False] + [[x,y,1]])
        return states

    def get_valid_loc_near(self, state):
        #This will search manhattan for a free location i.e., with a value of False
        x,y = state
        ret = state
        #check index ordering
        if self.maze[x][y] == True:
            states = np.array([(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.height and 0 <= ny < self.width and self.maze[nx][ny] == False])
            ret = states[0,:]
        return ret

    def reset(self):
        self.start_loc = np.array([0,0])
        return self.start_loc
            

    def step(self, action):
        #print(action)
        if action == 0:
            self.start_loc[0] -= 1
        if action == 1:
            self.start_loc[0] += 1
        if action == 2:
            self.start_loc[1] -= 1
        if action == 3:
            self.start_loc[1] += 1
        return self.start_loc
            

    def goal_Reached(self, state):
        return state[2] == 1

    def action_space(self):
        return [0,1,2,3]


    # Function to plot the maze and path
    def render(self, path):
        plt.imshow(self.maze, cmap=plt.cm.binary,interpolation='nearest')
        plt.scatter(path[:,1], path[:,0], s=7, c='g')
        plt.show()


# 