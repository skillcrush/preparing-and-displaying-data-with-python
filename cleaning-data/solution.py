import re
import json

with open("data.json", "r") as text:
    data = json.load(text)

for item in data:
  item["Category"] = re.compile(" [\.(]").split(item["Category"])[0]

print(data)