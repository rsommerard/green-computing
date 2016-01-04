average = 0.0
i = 0

with open("flv.out") as f:
  for line in f:
    power = line.split(" ")[1]
    average += float(power.split("\n")[0])
    i+=1

print average/i
