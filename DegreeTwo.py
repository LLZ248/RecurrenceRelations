# aₙ = xa₍ₙ₋₁₎ + Ba₍ₙ₋₂₎
def degreeTwoHomo(x, B, A0, A1):
    print(f"aₙ = {x}a₍ₙ₋₁₎ + {B}a₍ₙ₋₂₎")
    d = (-x) ** 2 - 4 * 1 * (-B)
    if d >= 0:
        if d == 0:
            root = x / (2 * 1)
            print("One root, Using a\u207F = A(r)\u207F + Bn(r)\u207F ,")
            print(f"General Solution: a\u207F = A({root})\u207F + Bn({root})\u207F")
            if A0 is not None and A1 is not None:
                print(f"A0 = {A0}, A1 = {A1}")
                A = A0
                B = (A1 - A * root) / root
                print(f"A = {A}, B = {B} ,")
                print(f"General Solution: a\u207F = {A}({root})\u207F + {B}n({root})\u207F")

        else:
            root1 = (x + (d ** (1 / 2))) / (2 * 1)
            root2 = (x - (d ** (1 / 2))) / (2 * 1)
            print("Two distinct roots, Using a\u207F = A(r₁)\u207F + B(r₂)\u207F ,")
            print(f"General Solution: a\u207F = A({root1})\u207F + B({root2})\u207F")
            # ax+by=e, cx+dy=f; x = (ed-bf)/(ad-bc) y=(af-ec)/(ad-bc)
            if A0 is not None and A1 is not None:
                print(f"A0 = {A0}, A1 = {A1}")
                # A + B = A0 , root1*A + root2*B = A1
                a = 1
                b = 1
                e = A0
                c = root1
                d = root2
                f = A1
                A = (e * d - b * f) / (a * d - b * c)
                B = (a * f - e * c) / (a * d - b * c)
                print(f"A = {A}, B = {B} ,")
                print(f"General Solution: a\u207F = {A}({root1})\u207F + {B}({root2})\u207F")


# aₙ = xa₍ₙ₋₁₎ + Ba₍ₙ₋₂₎ + Yn + C
def degreeTwoNonHomo(x, B, Y, C, A0, A1):
    print(f"aₙ = {x}a₍ₙ₋₁₎ + {B}a₍ₙ₋₂₎ + {Y}n + {C}")
    # Homogenous part
    d = (-x) ** 2 - 4 * 1 * (-B)
    if d >= 0:
        if d == 0:
            root = x / (2 * 1)
            print("One root, Using a\u207F = A(r)\u207F + Bn(r)\u207F ,")
            print(f"Homogenous Solution: A({root})\u207F + Bn({root})\u207F")
            if Y != 0:
                print("Polynomial, using a\u207F = cn+d ,")
            else:
                print("Constant, using a\u207F = c ,")
            c = Y / (1 - x - B)
            d = -c * x + x * d - 2 * B * c + d * B + c
            print(f"Non-homogenous Solution: {c}n + {d}")
            print(f"General solution: A({root})\u207F + Bn({root})\u207F + {c}n + {d}")

            if A0 is not None and A1 is not None:
                print(f"A0 = {A0}, A1 = {A1}")
                A = A0 - d
                B = (A1 - A * root - c - d) / root
                print(f"A = {A}, B = {B} ,")
                print(f"General Solution: a\u207F = {A}({root})\u207F + {B}n({root})\u207F")

        else:
            root1 = (x + (d ** (1 / 2))) / (2 * 1)
            root2 = (x - (d ** (1 / 2))) / (2 * 1)
            print("Two distinct roots, Using a\u207F = A(r₁)\u207F + B(r₂)\u207F ,")
            print(f"Homogenous Solution: a\u207F = A({root1})\u207F + B({root2})\u207F")
            c = Y / (1 - x - B)
            d = ((-c * x) - (2 * B * c) + C) / (1 - x - B)
            if Y != 0:
                print("Polynomial, using a\u207F = cn+d ,")
                print(f"Non-homogenous Solution: {c}n + {d}")
                print(f"General solution: A({root1})\u207F + B({root2})\u207F + {c}n + {d}")
            else:
                print("Constant, using a\u207F = C ,")
                print(f"Non-homogenous Solution: {d}")
                print(f"General solution: A({root1})\u207F + B({root2})\u207F + {d}")

            if A0 is not None and A1 is not None:
                # ax+by=e, Cx+Dy=f; x = (eD-bf)/(aD-bC) y=(af-eC)/(aD-bC)
                print(f"A0 = {A0}, A1 = {A1}")
                # A = x, B = y
                # A + B = A0 - d , root1*A + root2*B = A1 - c - d
                a = 1
                b = 1
                e = A0 - d
                C = root1
                D = root2
                f = A1 - c - d
                A = (e * D - b * f) / (a * D - b * C)
                B = (a * f - e * C) / (a * D - b * C)
                print(f"A = {A}, B = {B} ,")
                if Y != 0:
                    print(f"General Solution: a\u207F = {A}({root1})\u207F + {B}({root2})\u207F + {c}n + {d}")
                else:
                    print(f"General Solution: a\u207F = {A}({root1})\u207F + {B}({root2})\u207F + {d}")


# degreeTwoHomo(1, 2, 2, 7)
# degreeTwoNonHomo(6, -8, 0, 3, 0, 1)
