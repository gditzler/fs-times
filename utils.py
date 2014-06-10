#!/usr/bin/env python 
import numpy as np

def gen_dat(n_features = 100, n_observations = 500, n_relevant = 7):
  """generate some random data with a few relevant features"""
<<<<<<< HEAD
  data_val_max = 10
  xmax = 10
  xmin = 0
  data = 1.0*np.random.randint(xmax + 1, size = (n_features, n_observations))
  delta = n_relevant * (xmax - xmin) / 2.0
  labels = np.zeros((n_observations,))
  for m in range(n_observations):
    zz = 0.0
    for k in range(n_relevant):
      zz += data[k, m]
    if zz > delta:
      labels[m] = 1
    else:
      labels[m] = 2
  data = data.transpose()
  return data, labels

