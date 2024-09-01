import csv
import numpy as np

with open("titanic.csv", "r") as file:
  data = csv.reader(file, delimiter=",")
  headers = next(data)
  data = list(data)
  data = np.array(data)
  

survived = np.array
fare = np.array

#empty lists to hold data from  the for loop
fare_survived = []
fare_not_survived = []

#ADD CODE: for loop and if/else statements

#ADD CODE: print lists
