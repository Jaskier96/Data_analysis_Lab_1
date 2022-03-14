import pandas as pd
import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

F=7
L=6

bern1 = CmdStanModel(stan_file='C:\\Users\\Jaskier-PC\\Desktop\\semestr8\\Data_analysis\\Lab2\\code_2.stan')
samp_bern1 = bern1.sample(data={'N':2, 'y':[0,1]})

bern2 = CmdStanModel(stan_file='C:\\Users\\Jaskier-PC\\Desktop\\semestr8\\Data_analysis\\Lab2\\code_3.stan')

samp_bern2 = bern2.sample(data={'N':2, 'y':[0,1]})

theta1 = samp_bern1.stan_variable(name='theta')
theta2 = samp_bern2.stan_variable(name='theta')
df = pd.DataFrame({'theta1': theta1, 'theta2': theta2})
df.plot.hist(subplots=True, bins=30)
plt.show()
