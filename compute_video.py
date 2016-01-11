
yuvnum = 0.0
yuvden = 0

with open("yuv.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    yuvnum += float(power.split("\n")[0])
    yuvden += 1

yuvaverage = yuvnum/yuvden
print yuvaverage


UFH264num = 0.0
UFH264den = 0

with open("UFH264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    UFH264num += float(power.split("\n")[0])
    UFH264den += 1

UFH264average = UFH264num/UFH264den
print UFH264average


FH264num = 0.0
FH264den = 0

with open("FH264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    FH264num += float(power.split("\n")[0])
    FH264den += 1

FH264average = FH264num/FH264den
print FH264average


MH264num = 0.0
MH264den = 0

with open("MH264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    MH264num += float(power.split("\n")[0])
    MH264den += 1

MH264average = MH264num/MH264den
print MH264average


SH264num = 0.0
SH264den = 0

with open("SH264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    SH264num += float(power.split("\n")[0])
    SH264den += 1

SH264average = SH264num/SH264den
print SH264average


PH264num = 0.0
PH264den = 0

with open("PH264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    PH264num += float(power.split("\n")[0])
    PH264den += 1

PH264average = PH264num/PH264den
print PH264average



with open("average.out", "w") as f:
  f.write('codec UFH264 FH264 MH264 SH264 PH264 YUV\n')
  f.write("Average " + str(UFH264average) + " " + str(FH264average) + " " + str(MH264average) + " "  + str(SH264average) + " " + str(PH264average) + " " + str(yuvaverage))
