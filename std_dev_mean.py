import time
import random
import numpy as np

def find_mean_st_deviation(data):
	start_time = time.time()

	data_arr = np.array(data)

	mean = np.mean(data_arr)
	standard_dev = np.std(data_arr)
	end_time = time.time()

	execution_time = end_time - start_time

	print(f"Mean (numpy): {mean}")
	print(f"Standard deviation (numpy): {standard_dev}")
	print(f"Execution time (numpy): {execution_time}")

data = [random.random() for _ in range(1000)]
find_mean_st_deviation(data)

print("************************")
print("************************")
print("************************")


def long_route(data):
	start_time = time.time()
	total_sum = 0
	squared_sum = 0

	for i in data:
		total_sum += i
		squared_sum += i ** 2


	mean = total_sum / len(data)
	standard_deviation = (squared_sum / len(data) - mean**2) ** 0.5
	end_time = time.time()
	execution_time = end_time - start_time

	print(f"Mean_of_long route: {mean}")
	print(f"St_dev_of_long route: {standard_deviation}")
	print(f"Exec time_of_long route: {execution_time}")

# data = [random.random() for _ in range(1000)]
long_route(data)




