import numpy
import math
import operator

from constants import *

class Pest:
  def __init__(self, id, x, y, vx=0, vy=0):
    self.id = id
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy

  def __eq__(self, other):
    if isinstance(other, Pest):
      return self.id == other.id

  def __hash__(self):
    return hash(self.id)

  def distance(self, other):
    assert(isinstance(other,Pest))
    return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class LeaderPest(Pest):
  def __init__(self, id, x, y, vx=0, vy=0):
    Pest.__init__(self, id, x, y, vx=vx, vy=vy)

  def update_velocity(self, pests):
    self.vx = VMAX * math.sqrt(2)
    self.vy = VMAX

class FollowerPest(Pest):
  def __init__(self, id, x, y, vx=0, vy=0):
    Pest.__init__(self, id, x, y, vx=vx, vy=vy)
  
  def update_velocity(self, pests):
    # Get nearest neighbors and set velocity to their average velocity.
    # Compute distances to each other pest.
    distances = {}
    total_weight = 0
    vx_new = 0
    vy_new = 0
    for pest in pests:
      distances[pest] = self.distance(pest)
    sorted_distances = sorted(distances.iteritems(),key=operator.itemgetter(1))
    # print 'sorted distances\n', sorted_distances
    for i,(pest,dist) in enumerate(sorted_distances):
     #  print pest, dist
      if i > K_NEIGHBORS:
        break
      weight = 1
      if DIST_WEIGHTED:
        weight = math.exp(-DIST_DECAY*dist)
      # print 'vx_new = ', weight, '*', pest.vx
      # print 'vy_new = ', weight, '*', pest.vy
      vx_new += weight * pest.vx + numpy.random.normal(0,SIGMA)
      vy_new += weight * pest.vy + numpy.random.normal(0,SIGMA)
      # vx_new += weight * (pest.x - self.x)
      # vy_new += weight * (pest.y - self.y)
      total_weight += weight
    if total_weight > 0:
      vx_new /= total_weight
      vy_new /= total_weight
      self.vx = vx_new
      self.vy = vy_new
