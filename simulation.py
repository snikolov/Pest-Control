import numpy
import random
import matplotlib.pyplot as plt

from constants import *
from pest import *

class Simulation:

  def __init__(self,n_leader_pests,n_follower_pests,xmax,ymax):
    self.n_leader_pests = n_follower_pests
    self.xmax = xmax
    self.ymax = ymax
    (self.leader_pests, self.follower_pests) = \
        self._init_pests(n_leader_pests,n_follower_pests,xmax,ymax)

  def _init_pests(self,n_leader_pests,n_follower_pests,xmax,ymax):
    # Initialize n_pests pests at random positions and velocities
    follower_pests = []
    for pid in xrange(n_follower_pests):
      theta = random.random() * math.pi * 2
      dirx = math.cos(theta)
      diry = math.sin(theta)
      follower_pests.append(FollowerPest(pid, 
                                numpy.random.normal(0,.1) * self.xmax,
                                numpy.random.normal(0,.1) * self.ymax,
                                vx = VMAX * numpy.random.normal(0,1) * dirx,
                                vy = VMAX * numpy.random.normal(0,1) * diry))
    leader_pests = []
    for pid in xrange(n_leader_pests):
      theta = random.random() * math.pi * 2
      dirx = math.cos(theta)
      diry = math.sin(theta)
      leader_pests.append(LeaderPest(pid, 
                              numpy.random.normal(0,.1) * self.xmax,
                              numpy.random.normal(0,.1) * self.ymax,
                              vx = VMAX * numpy.random.normal(0,1) * dirx,
                              vy = VMAX * numpy.random.normal(0,1) * diry))
    return (leader_pests, follower_pests)

  def run(self):
    plt.figure()
    plt.hold(False)
    pests = []
    pests.extend(self.leader_pests)
    pests.extend(self.follower_pests)
    for t in xrange(NUM_TIMESTEPS):
      # Pick a random pest and update it's position and velocity
      for n in xrange(len(pests)):
        # pid = random.randint(0,self.n_pests-1)
        pid = n
        pest = pests[pid]
        # print 'velocity pid', pid, ':', pest.vx, pest.vy
        pest.x += TIME_PER_STEP * pest.vx
        pest.x = pest.x % self.xmax
        pest.y += TIME_PER_STEP * pest.vy
        pest.y = pest.y % self.ymax
        pest.update_velocity(pests)
      plt.scatter([p.x for p in self.leader_pests], [p.y for p in self.leader_pests], c='r', marker='o')
      plt.hold(True)
      plt.scatter([p.x for p in self.follower_pests], [p.y for p in self.follower_pests], c='b', marker='o')
      plt.hold(False)
      plt.axis([0,self.xmax,0,self.ymax])
      plt.draw()
      plt.pause(0.0001)
      
