def pid_control(n, time, error_array, sample_result, k_p, k_i, k_d, pi, score_array):
    score = k_p*error_array[n]
    for i in range(n-pi-1, n+1):
        score += k_i/pi*error_array[i]
    score += k_d*(error_array[n]-error_array[n-1])/(time[sample_result[n]]-time[sample_result[n-1]])
    score_array.append(score)
    return score_array