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


LCh265num = 0.0
LCh265den = 0

with open("LCh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LCh265num += float(power.split("\n")[0])
    LCh265den += 1

LCh265average = LCh265num/LCh265den
print LCh265average


HCh265num = 0.0
HCh265den = 0

with open("HCh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    HCh265num += float(power.split("\n")[0])
    HCh265den += 1

HCh265average = HCh265num/HCh265den
print HCh265average


LCFLh264num = 0.0
LCFLh264den = 0

with open("LCFLh-264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LCFLh264num += float(power.split("\n")[0])
    LCFLh264den += 1

LCFLh264average = LCFLh264num/LCFLh264den
print LCFLh264average

LCFLh265num = 0.0
LCFLh265den = 0

with open("LCFLh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LCFLh265num += float(power.split("\n")[0])
    LCFLh265den += 1

LCFLh265average = LCFLh265num/LCFLh265den
print LCFLh265average

HCFLh264num = 0.0
HCFLh264den = 0

with open("HCFLh-264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    HCFLh264num += float(power.split("\n")[0])
    HCFLh264den += 1

HCFLh264average = HCFLh264num/HCFLh264den
print HCFLh264average

HCFLh265num = 0.0
HCFLh265den = 0

with open("HCFLh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    HCFLh265num += float(power.split("\n")[0])
    HCFLh265den += 1

HCFLh265average = HCFLh265num/HCFLh265den
print HCFLh265average

LCLLh264num = 0.0
LCLLh264den = 0

with open("LCLLh-264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LCLLh264num += float(power.split("\n")[0])
    LCLLh264den += 1

LCLLh264average = LCLLh264num/LCLLh264den
print LCLLh264average

LCLLh265num = 0.0
LCLLh265den = 0

with open("LCLLh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    LCLLh265num += float(power.split("\n")[0])
    LCLLh265den += 1

LCLLh265average = LCLLh265num/LCLLh265den
print LCLLh265average

HCLLh264num = 0.0
HCLLh264den = 0

with open("HCLLh-264.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    HCLLh264num += float(power.split("\n")[0])
    HCLLh264den += 1

HCLLh264average = HCLLh264num/HCLLh264den
print HCLLh264average

HCLLh265num = 0.0
HCLLh265den = 0

with open("HCLLh-265.out", "r") as f:
  for line in f:
    power = line.split(" ")[1]
    HCLLh265num += float(power.split("\n")[0])
    HCLLh265den += 1

HCLLh265average = HCLLh265num/HCLLh265den
print HCLLh265average
with open("average.out", "w") as f:
  f.write('codec part14 h-264 vp8 vp9 LLvp8 LLvp9 LCh-265 HCh-265 LCFLh-264 LCFLh-265 HCFLh-264 HCFLh-265 LCLLh-264 LCLLh-265 HCLLh-264 HCLLh-265 yuv\n')
  f.write("Average " + str(part14average) + " " + str(h264average) + " " + str(vp8average)+ " " + str(vp9average)+ " " + str(LLvp8average)+ " " + str(LLvp9average)+ " " + str(LCh265average)+" " + str(HCh265average)+ " " + str(LCFLh264average)+ " " + str(LCFLh265average)+ " " + str(HCFLh264average)+ " " + str(HCFLh265average)+ " " + str(LCLLh264average)+ " " + str(LCLLh265average)+ " " + str(HCLLh264average)+ " " + str(HCLLh265average)+ " " + str(yuvaverage))
