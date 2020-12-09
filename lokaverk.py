import re
import math

def heilda(fall):
    formerki = []
    if fall[0] != "-":
        fall = "+" + fall
    lidir = re.split("[+-]", fall)
    lidir.remove("")

    for x in fall:
        if x == "+" or x == "-":
            formerki.append(x)

    lidur = []
    strengur = ""
    for x in lidir:
        if "x" in x:
            i = ""
            ind = x.index("x")
            if ind == 0 and len(x) > 1:
                i = i + str(1 / (int(x[ind + 1:]) + 1)) + "*x**" + str(int(x[ind + 1:]) + 1)
                lidur.append(i)
            elif ind == 0 and len(x) == 1:
                lidur.append("0.5*x**2")
            elif len(x) > 2:
                i = i + str(int(x[:ind]) / (int(x[ind + 1:]) + 1)) + "*x**" + str(int(x[ind + 1:]) + 1)
                lidur.append(i)
            else:
                i = i + str(int(x[:ind]) / 2) + "*x**" + "2"
                lidur.append(i)
        else:
            lidur.append(x + "*x")
    for x in range(len(lidur)):
        strengur = strengur + formerki[x] + lidur[x]

    return strengur

def flatarmal(fall, efri, nedri):
    nytt_fall = heilda(fall)
    m_a = nytt_fall.replace("x", efri)
    m_b = nytt_fall.replace("x", nedri)
    flatarmal = abs(eval(m_a)-eval(m_b))

    return flatarmal


def rummalSnuda(fall):
    nytt_fall = heilda(fall)
    m_a = nytt_fall.replace("x", efri)
    m_b = nytt_fall.replace("x", nedri)
    rummal = float(math.pi * ((heilda(fall))**2))
    return rummal

on=True
while on:
    print("1. Flatarmál milli x-ás og f(x)")
    print("2. Flatarmál milli f(x) og g(x)")
    print("3. Rúmmál snúða")
    print("4. Hætta")
    val = int(input("Veldu hvað þú vilt reikna:"))

    if val==1:

        fall = input("Sláðu inn fallið: f(x)= ")
        efri = input("Sláðu inn x fyrir efri mörk: ")
        nedri = input("Sláðu inn x fyrir neðri mörk: ")

        print("Flatarmálið milli x-ás og f(x) =", fall, "er:", flatarmal(fall,efri,nedri))

    elif val==2:
        fall = input("Sláðu inn fallið: f(x)= ")
        fall2 = input("Sláðu inn fallið: g(x)= ")
        efri = input("Sláðu inn x fyrir efri mörk: ")
        nedri = input("Sláðu inn x fyrir neðri mörk: ")

        flat = flatarmal(fall,efri,nedri)
        flat2 = flatarmal(fall2,efri,nedri)

        print("Flatarmálið milli f(x)=", fall,", og g(x) =", fall2, "er:", abs(round(flat - flat2, 5)))

    elif val==3:
        fall = input("Sláðu inn fallið: f(x)= ")
        print("Rúmmmál Snúða f(x) =", fall, "er:", rummalSnuda(fall))

    elif val==4:
        on=False

    else:
        print()
        print("Ekki hægt veldu aftur!")
        print()
