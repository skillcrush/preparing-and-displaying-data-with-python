import matplotlib.pyplot as plt

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [28,32,31,40,45,55,60,65,54,43,34,30]

plt.plot(month,temp,color="purple")
plt.xlabel("Month", fontsize=16)
plt.ylabel("Temp in Fahrenheit", fontsize=16)
plt.title("Avg Temperatures for 2018 in North Pole, Alaska")

plt.savefig("north_pole_temps.png")