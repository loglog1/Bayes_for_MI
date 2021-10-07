import GPy
import GPyOpt
import numpy as np

def target_func(x):
    # TODO: describe your code
    return 

# optization boundaries
bounds = [{'name': 'x0', 'type': 'continuous', 'domain': (0,10)},
          {'name': 'x1', 'type': 'discrete', 'domain': (0,1)}]
myBopt = GPyOpt.methods.BayesianOptimization(f=target_func, domain=bounds)

myBopt.run_optimization(max_iter=30)
print(myBopt.x_opt)
print(myBopt.fx_opt)
