import math
import numpy as np


def perturb(data, n, alpha, w, theta, mu,  score_array, epsilon, epsilon_reminded, sample_result):
    p = 1-math.exp(-1*(alpha/score_array[n]+(1-alpha)*score_array[n]))
    # p = 1 - math.exp(-score_array[n])
    b = math.log(theta/score_array[n]+mu)
    epsilon_now = p*epsilon_reminded
    epsilon_reminded -= epsilon_now
    q = 0.5*epsilon_now/(1-math.exp(-epsilon_now*b))
    perturb_value = sample_function(q, b, epsilon_now)
    perturbed_result = data[sample_result[n]]+perturb_value
    # print("alpha", alpha)
    if epsilon_reminded>epsilon/2:
        alpha -= 1/((1-alpha)*(1-alpha))*0.01
    elif epsilon/w > epsilon_reminded:
        alpha += 1/((1-alpha)*(1-alpha))*0.01

    return alpha, perturbed_result, epsilon_reminded


def sample_function(a, b, epsilon):
    number = np.random.random_sample()
    if number < 0.5:
        result = math.log(number*a/epsilon+math.exp(-1*epsilon*b))/epsilon
        return result
    else:
        result = -1*math.log((0.5+a/epsilon-number)*epsilon/a)/epsilon
        return result
