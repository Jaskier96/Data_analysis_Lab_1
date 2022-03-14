from cmdstanpy import CmdStanModel


F=7
L=6

model_tune = CmdStanModel(stan_file='code_6.stan')

y0 = 1
data={'y_guess':[y0],
'theta':[(F+L)/2]}
tunes = model_tune.sample(data=data, fixed_param=True, iter_sampling=1,iter_warmup=0, chains = 1)
tunes.draws_pd()
