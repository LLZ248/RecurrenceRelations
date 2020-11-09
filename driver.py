import DegreeTwo as D2
import DegreeOne as D1


def menu():
    print("Welcome to Recurrence Relations Solution Program.")
    degree = input("Is the relation degree one or degree two?[1/2] Other character to quit: ")
    if degree == "1":
        choice = input("Homogeneous[H] or Non-homogenous[N] : ").upper()
        if choice == "H":
            print("aₙ = xa₍ₙ₋₁₎")
            x = input("x: ")
            A0 = input("Your a₀ Type NULL if no a₀ : ").upper()
            if A0 != "NULL":
                D1.degreeOneHomo(float(x), float(A0))
            else:
                D1.degreeOneHomo(float(x), None)
        else:
            print("aₙ = xa₍ₙ₋₁₎ + Yn + Z")
            x = input("x : ")
            Y = input("Y : ")
            Z = input("Z : ")
            A0 = input("Your a₀ Type NULL if no a₀ : ").upper()
            if Y != "0":
                if A0 != "NULL":
                    D1.degreeOneNonHomoPoly(float(x), float(Y), float(Z), float(A0))
                else:
                    D1.degreeOneNonHomoPoly(float(x), float(Y), float(Z), None)
            else:
                if A0 != "NULL":
                    D1.degreeOneNonHomoConstant(float(x), float(Z), float(A0))
                else:
                    D1.degreeOneNonHomoConstant(float(x), float(Z), None)
        return True

    elif degree == "2":
        choice = input("Homogeneous[H] or Non-homogenous[N] : ").upper()
        if choice == "H":
            print("aₙ = xa₍ₙ₋₁₎ + Ba₍ₙ₋₂₎")
            x = input("x: ")
            B = input("B: ")
            A0 = input("Your a₀ Type NULL if no a₀ : ").upper()
            A1 = input("Your a₁ Type NULL if no a₁ : ").upper()
            if A0 == "NULL" or A1 == "NULL":
                D2.degreeTwoHomo(float(x), float(B), None, None)
            else:
                D2.degreeTwoHomo(float(x), float(B), float(A0), float(A1))
        else:
            print("aₙ = xa₍ₙ₋₁₎ + Ba₍ₙ₋₂₎ + Yn + C")
            x = input("x: ")
            B = input("B: ")
            Y = input("Y: ")
            C = input("C: ")
            A0 = input("Your a₀ Type NULL if no a₀ : ").upper()
            A1 = input("Your a₁ Type NULL if no a₁ : ").upper()
            if A0 == "NULL" or A1 == "NULL":
                D2.degreeTwoNonHomo(float(x), float(B), float(Y), float(C), None, None)
            else:
                D2.degreeTwoNonHomo(float(x), float(B), float(Y), float(C), float(A0), float(A1))
        return True
    else:
        input("Enter to quit")
        return False


def main():
    while menu():
        print()
        print("---------------------------------------------------------")
        print()


main()
