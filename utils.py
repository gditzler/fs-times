#!/usr/bin/env python 
import numpy as np

def gen_dat(n_features = 100, n_observations = 500, n_relevant = 7):
  """generate some random data with a few relevant features"""
  data_val_max = 10

  data = 1.*np.random.randint(data_val_max, size=(n_observations, n_features)) 
  labels = np.zeros((n_observations,))
  for n, sample in enumerate(data):
    if np.sum(sample[:n_relevant]) >= data_val_max*1.0/2*n_relevant:
      labels[n] = 1.
    else:
      labels[n] = 0.
  return data, labels

