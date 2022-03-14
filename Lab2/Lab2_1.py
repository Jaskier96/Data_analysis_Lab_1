import matplotlib.pyplot as plt
from cmdstanpy import CmdStanModel

F=7
L=6

gen_quant = CmdStanModel( stan_file = "C:\\Users\\Jaskier-PC\\Desktop\\semestr8\\Data_analysis\\Lab2\\code_1.stan" )

samples = gen_quant.sample(data={'M':F},
                            fixed_param=True,
                            iter_sampling=1000,
                            iter_warmup=0,
                            chains=1)

df = samples.draws_pd()
df

Lambda = df['lambda']
Lambda.plot.hist(bins=30)
plt.show()

df2 = df.drop(df.columns[0:3],axis=1)
df2.plot.hist(subplots=True, bins=30)
plt.show()