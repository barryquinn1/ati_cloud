import math
import numpy as np
from time import process_time
S0=36.
T=1.0
r=0.06
sigma=0.2
def mcs_simulation_py(p):
  M,I = p #  M= number of time intervals for discretisation. I = number of paths to simulate. 
  dt = T/M
  S = np.zeros((M+1,I))
  S[0]=S0
  rn = np.random.standard_normal(S.shape)
  for t in range(1,M+1):
    for i in range(I):
      S[t,i] = S[t-1,i] * math.exp((r-sigma**2/2) * dt + sigma * math.sqrt(dt) * rn[t,i])
  return S

I=1000
M=100
t1_start=process_time()
S = mcs_simulation_py((M,I))
t1_stop=process_time()
print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start)


def mcs_simulation_np(p):
  M,I = p
  dt = T/M
  S = np.zeros((M+1,I))
  S[0]=S0
  rn = np.random.standard_normal(S.shape)
  for t in range(1,M+1):
    for i in range(I):
      S[t,i] = S[t-1,i] * np.exp((r-sigma**2/2) * dt + sigma * math.sqrt(dt) * rn[t,i]) 
  return S
  
t1_start=process_time()
S = mcs_simulation_np((M,I))

import numba
mcs_simulation_nb=numba.jit(mcs_simulation_np)
t_start=process_time()
S=mcs_simulation_nb((M,I))
t_end=process_time()
print("Elapsed time in seconds:",t_end-t_start)

t_start=process_time()
S=mcs_simulation_nb((M,I))
t_end=process_time()
print("Elapsed time in seconds:",t_end-t_start)

t1_stop=process_time()
