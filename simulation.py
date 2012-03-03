import random
import matplotlib.pyplot as plt

from constants import *
from pest import *

class Simulation:

  def __init__(self,n_pests,xmax,ymax):
    self.n_pests = n_pests
    self.xmax = xmax
    self.ymax = ymax
    self.pests = self._init_pests(n_pests,xmax,ymax)

  def _init_pests(self,n_pests,xmax,ymax):
    # Initialize n_pests pests at random positions and velocities
    pests = []
    for pid in xrange(n_pests):
      theta = random.random() * math.pi * 2
      dirx = math.cos(theta)
      diry = math.sin(theta)
      pests.append(Pest(pid, 
                        random.random() * self.xmax,
                        random.random() * self.ymax,
                        vx = VMAX * random.random() * dirx,
                        vy = VMAX * random.random() * diry))
    return pests

  def run(self):
    plt.figure()
    plt.hold(False)
    for t in xrange(NUM_TIMESTEPS):
      # Pick a random pest and update it's position and velocity
      for n in xrange(self.n_pests):
        # pid = random.randint(0,self.n_pests-1)
        pid = n
        pest = self.pests[pid]
        # print 'velocity pid', pid, ':', pest.vx, pest.vy
        pest.x += TIME_PER_STEP * pest.vx
        pest.x = pest.x % self.xmax
        pest.y += TIME_PER_STEP * pest.vy
        pest.y = pest.y % self.ymax
        pest.set_velocity(self.pests)
      plt.scatter([p.x for p in self.pests], [p.y for p in self.pests])
      plt.axis([0,self.xmax,0,self.ymax])
      plt.draw()
      plt.pause(0.0001)
      
