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

# Transform your merged dataset back into a regular list and then a string
listify = combined_data.tolist()

titanic_lists_to_string = []
for titanic_lists in listify:
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)
complete_titanic = ("\n").join(titanic_lists_to_string)

# Write your fresh string to a new .csv file
with open("titanic.csv", "w") as file:
  file.write("Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n")
  file.write(complete_titanic)
