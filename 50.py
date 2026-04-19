import csv
with open("fake.csv", 'r') as f:
  ans = csv.reader(f)

  for i in ans:
    print(i)