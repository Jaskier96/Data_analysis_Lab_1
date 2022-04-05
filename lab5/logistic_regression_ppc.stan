data{
    int<lower=1> N; //number of observ
    int<lower=1> M; //number of covariates
    matrix[N, M] X; //covariate design matrix
    real sigma; //prior standard deviation
}

transformed data {
   vector[N] ones_N = rep_vector(1, N);
   vector[M] ones_M = rep_vector(1, M);
}

generated quantities {
   vector[N] prob_ppc;
   
       real beta[M] = normal_rng(0, ones_M*sigma);
       real alpha = normal_rng(0, sigma);
       prob_ppc = inv_logit(X * to_vector(beta) + ones_N*alpha);
   
}