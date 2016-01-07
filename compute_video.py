part14num = 0.0
part14den = 0

with open("mpeg-4_part14.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    part14num += float(power.split("\n")[0])
    part14den += 1

part14average = part14num/part14den
print part14average


h264num = 0.0
h264den = 0

with open("h-264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    h264num += float(power.split("\n")[0])
    h264den += 1

h264average = h264num/h264den
print h264average


yuvnum = 0.0
yuvden = 0

with open("yuv.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    yuvnum += float(power.split("\n")[0])
    yuvden += 1

yuvaverage = yuvnum/yuvden
print yuvaverage


vp8num = 0.0
vp8den = 0

with open("vp8.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    vp8num += float(power.split("\n")[0])
    vp8den += 1

vp8average = vp8num/vp8den
print vp8average

vp9num = 0.0
vp9den = 0

with open("vp9.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    vp9num += float(power.split("\n")[0])
    vp9den += 1

vp9average = vp9num/vp9den
print vp9average

LLvp8num = 0.0
LLvp8den = 0

with open("LLvp8.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LLvp8num += float(power.split("\n")[0])
    LLvp8den += 1

LLvp8average = LLvp8num/LLvp8den
print LLvp8average


LLvp9num = 0.0
LLvp9den = 0

with open("LLvp9.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LLvp9num += float(power.split("\n")[0])
    LLvp9den += 1

LLvp9average = LLvp9num/LLvp9den
print LLvp9average

with open("average.out", "w") as f:
  f.write('codec part14 h-264 vp8 vp9 LLvp8 LLvp9 yuv\n')
  f.write("Average " + str(part14average) + " " + str(h264average) + " " + str(vp8average)+ " " + str(vp9average)+ " " + str(LLvp8average)+ " " + str(LLvp9average)+ " " + str(yuvaverage))
