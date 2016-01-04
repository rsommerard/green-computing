flvnum = 0.0
flvden = 0

with open("flv.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    flvnum += float(power.split("\n")[0])
    flvden += 1

flvaverage = flvnum/flvden
print flvaverage


mkvnum = 0.0
mkvden = 0

with open("mkv.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    mkvnum += float(power.split("\n")[0])
    mkvden += 1

mkvaverage = mkvnum/mkvden
print mkvaverage


mp4num = 0.0
mp4den = 0

with open("mp4.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    mp4num += float(power.split("\n")[0])
    mp4den += 1

mp4average = mp4num/mp4den
print mp4average


with open("average.out", "w") as f:
  f.write('flv mkv mp4')
  f.write("Average" + str(flvaverage) + " " + str(mkvaverage) + " " + str(mp4average))
