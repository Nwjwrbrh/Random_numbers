import math
with open("uni.dat","r") as f1:
    with open("3.1/V.dat","w") as f2:
        for n in f1:
            if(1-float(n)>0):
                f2.write(f"{-2*math.log(1-float(n))}\n")