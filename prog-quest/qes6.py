import json
import csv
name = input("Enter your name:")
z = 0
with open("qes_ans.json", '+r') as file:
    zy = json.load(file)
    for i in range(1, 3):
        answers = input(f"{i}: {zy[str(i)][0]}")
        if answers == zy[str(i)][1]:
            z += 1

print("your result is ", z)

with open("results.csv",'+w') as f:
    z1 = csv.writer(f)
    z1.writerow([name + "," + str(z)])