#!/usr/bin/env python 
import numpy as np

def gen_dat(n_features = 100, n_observations = 500, n_relevant = 7):
  """generate some random data with a few relevant features"""
  xmax = 10
  xmin = 0
  data = 1.*np.random.randint(xmax+1, size=(n_observations, n_features)) 
  labels = np.zeros((n_observations,))
  delta = n_relevant*(xmax - xmin)/2.
  """
  for n, sample in enumerate(data.transpose()):
    if np.sum(sample[:n_relevant]) >= delta:
      labels[n] = 1.
    else:
      labels[n] = 2.
  """
  for m in range(n_observations):
    zz = 0.
    for k in range(n_relevant):
      zz += data[m,k]
    if zz > delta:
      labels[m] = 1.
    else:
      labels[m] = 2.
  return data, labels

