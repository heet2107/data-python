# Part - 2
# Problem 2
open_file = open("CupcakeInvoices.csv")

# Problem 3
for row in open_file:
  print(row)

# Problem 4
for row in open_file:
  values = row.split(',')
  print(values[2])

# Problem 5
for row in open_file:
  values = row.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

# Problem 6
total = 0

for row in open_file:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)

# Problem 7
open_file.close()


