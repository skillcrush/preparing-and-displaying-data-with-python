import csv
import numpy as np

with open("titanic1.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data1 = np.array(data_list)

with open("titanic2.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data2 = np.array(data_list)

combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

print(combined_data.shape)
print(combined_data.ndim)