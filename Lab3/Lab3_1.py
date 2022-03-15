import matplotlib.pyplot as plt
import pandas as pd
import arviz as az
import numpy as np
import scipy.stats as stats
from cmdstanpy import CmdStanModel

model = CmdStanModel(stan_file='stan1.stan')
