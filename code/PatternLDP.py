import read_file as rf
import pattern_aware_sampling as pas
import importance_characterization as ic
import importance_aware_randomization as iar
import dynamic_time_wrapping as dt
from matplotlib import pyplot as plt
import numpy as np


def pattern_ldp(file_names, delta, w, theta, mu, epsilon, k_p, k_i, k_d, pi):
    for name in file_names:
        d = []
        for loop in range(0, 10):
            print(name)
            time, data = rf.read_files(name)
            sample_points = pas.sample_points(data, time, delta)
            perturb_array = []
            error_array = [0, 0]
            score_array = [0.01, 0.01]
            alpha = 0.5
            epsilon_remaind = epsilon
            for index in range(len(sample_points)):
                if index <= 1:

                    perturb_array.append(data[sample_points[index]])
                else:
                    score_array, error_array = ic.pid_control(index, data, time, error_array, sample_points, k_p, k_i, k_d, pi, score_array)
                    alpha, perturb_result, epsilon_remind = \
                        iar.perturb(data, index, alpha, w, theta, mu,  score_array, epsilon, epsilon_remaind, sample_points)
                    perturb_array.append(perturb_result)
                    if index % w == 0:
                        alpha = 0.5
                        epsilon_remaind = epsilon
                    # if index % 100 == 0:
                    #     print("100 done")

            # process_array = []
            # start_index = sample_points[0]
            # for index in range(1, len(sample_points)):
            #     process_array.append(data[start_index])
            #     end_index = sample_points[index]
            #     k = (perturb_array[index]-perturb_array[index-1])/(time[end_index]-time[start_index])
            #     for virtual_index in range(start_index+1, end_index):
            #         process_array.append(k*(time[virtual_index]-time[start_index])+data[start_index])
            #     start_index = end_index
            # # plt.axis([0, 1500, -3, 4])
            # # # plt.scatter(time[:500], process_array[:500], c="orange")
            # # plt.plot(time[:500], process_array[:500], c="orange")
            # # plt.scatter(time[:500], data[:500], c="blue")
            # # plt.plot(time[:500], data[:500], c="blue")
            # # plt.show()
            # # plt.cla()
            # distance = dt.dtw(process_array, data)
            # d.append(distance)


            process_array = [data[index] for index in sample_points]
            # plt.axis([0, 200, -3, 4])
            # plt.scatter(time[:50], process_array[:50], c="blue")
            # plt.plot(time[:50], process_array[:50], c="blue")
            # plt.scatter(time[:50], perturb_array[:50], c="orange")
            # plt.plot(time[:50], perturb_array[:50], c="orange")
            # plt.show()
            # plt.cla()
            distance = dt.dtw(process_array, perturb_array)
            d.append(distance)

        print("distance", np.mean(d))
    return distance


if __name__ == "__main__":
    files = ["../data/heartrate_2017-01-09.csv", "../data/heartrate_2017-01-10.csv", "../data/heartrate_2017-01-11.csv",
             "../data/heartrate_2017-01-12.csv", "../data/heartrate_2017-01-14.csv", "../data/heartrate_2017-01-16.csv"]
    # files = ["../data/heartrate_2017-01-09.csv"]
    pattern_ldp(files, 0.5, 40, 10, 1, 0.5, 0.8, 0.1, 0.1, 5)