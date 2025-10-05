def compound_interest(p: float, n: float, r: float) -> tuple:
    amt = p * (1 + (r / 100)) ** n
    i = amt - p
    return i, amt


def main():
    p = float(input("Please Enter principal in INR : "))
    n = float(input("Please enter number of years : "))
    r = float(input("Please enter rate of interst in %.p.a : "))
    i, a = compound_interest(p, n, r)
    print(f"Interest : {i:.2f} INR")
    print(f"Amount : {a:.2f} INR")


if __name__ == "__main__":
    main()
