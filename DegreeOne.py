# aₙ = xa₍ₙ₋₁₎ + Yn + Z
# A0 = aₙ, n = 0
def degreeOneNonHomoPoly(x, Y, Z, A0):
    print("a\u2099 = " + str(x) + "a\u208D\u2099\u208B\u2081\u208E + " + str(Y) + "n + " + str(Z))
    print("Homogeneous solution: A(" + str(x) + ")\u207f")
    c = Y / (1 - x)
    d = (-x * c + Z) / (1 - x)
    print("Non-homogeneous solution: " + str(c) + "n + " + str(d))
    print("General solution: " + "A(" + str(x) + ")\u207f " + str(c) + "n + " + str(d))
    if A0 is not None:
        A = A0 - d
        print("General solution: " + str(A) + "(" + str(x) + ")\u207f + " + str(c) + "n + " + str(d))


# aₙ = xa₍ₙ₋₁₎ + C
# A0 = aₙ, n = 0
def degreeOneNonHomoConstant(x, C, A0):
    print("a\u2099 = " + str(x) + "a\u208D\u2099\u208B\u2081\u208E +", C)
    print("Homogeneous solution: A(" + str(x) + ")\u207f")
    c = C / (1 - x)
    print("Non-homogeneous solution: " + str(c))
    print("General solution: " + "A(" + str(x) + ")\u207f + " + str(c))
    if A0 is not None:
        A = A0 - c
        print("General solution: " + str(A) + "(" + str(x) + ")\u207f + " + str(c))


def degreeOneHomo(x, A0):
    print("a\u2099 = " + str(x) + "a\u208D\u2099\u208B\u2081\u208E ")
    print("Homogeneous solution: A(" + str(x) + ")\u207f")
    if A0 is not None:
        A = A0
        print("General solution: " + str(A) + "(" + str(x) + ")\u207f")


# If no A0, then give None
# degreeOneNonHomoPoly(2, 3, 1, None)
# degreeOneNonHomoConstant(0.4, 12, 8)
# degreeOneHomo(2, 3)
