
import numpy as np
import matplotlib.pylab as plt 
import feast
import utils
import time 
from sklearn.feature_selection import chi2 
from sklearn.linear_model import ElasticNet, Lasso
from npfs import npfs


n_features = 500
steps = 250
n_begin = 500
n_end =5000
n_relevant = 100
n_select = int(np.floor(n_features/5))

mrmr_times = []
mim_times = []
jmi_times = []
chi2_times = []
enet_times = []
lasso_times = []
npfs_times = []

for n_observations in range(n_begin, n_end, steps):
    print "Running with " + str(n_observations)
    data, labels = utils.gen_dat(n_features=n_features, 
                                 n_observations=n_observations, 
                                 n_relevant=n_relevant)
    # run mrmr 
    t_start = time.time()
    sel_feat = feast.mRMR(data=data, labels=labels, n_select=int(np.floor(n_features/5)))
    mrmr_times.append(time.time() - t_start)
    
    # run mim 
    t_start = time.time()
    sel_feat = feast.MIM(data=data, labels=labels, n_select=int(np.floor(n_features/5)))
    mim_times.append(time.time() - t_start)
    
    # run jmi
    t_start = time.time()
    sel_feat = feast.JMI(data=data, labels=labels, n_select=int(np.floor(n_features/5)))
    jmi_times.append(time.time() - t_start)
    
    # run chi2
    t_start = time.time()
    sel_feat = chi2(X=data, y=labels)  
    chi2_times.append(time.time() - t_start)
    
    # run lasso
    mdl = Lasso(alpha=1.0, fit_intercept=True, normalize=False, precompute='auto', 
                copy_X=False, max_iter=5000, tol=0.0001, warm_start=False, positive=False)
    t_start = time.time()
    w = mdl.fit(X=data, y=labels)
    lasso_times.append(time.time() - t_start)
    
    # run elastic net
    mdl = ElasticNet(alpha=1.0, l1_ratio=0.5, fit_intercept=True, normalize=False, 
                     precompute='auto', max_iter=5000, copy_X=False, tol=0.0001, warm_start=False, 
                     positive=False, rho=None) 
    t_start = time.time() 
    w = mdl.fit(X=data, y=labels)
    enet_times.append(time.time() - t_start)
    
    mdl = npfs(fs_method="MIM", n_select=5, n_bootstraps=50, alpha=.01, beta=0.0, parallel=50)
    t_start = time.time()
    s = mdl.fit(data,labels)
    npfs_times.append(time.time() - t_start)
    


data = {"n_observations":n_observations, "mrmr_times":mrmr_times,"jmi_times":jmi_times,"chi2_times":chi2_times,"lasso_times":lasso_times,"enet_times":enet_times,"npfs_times":npfs_times}

import pickle
pickle.dump(data, open("output.pkl","wb"))

