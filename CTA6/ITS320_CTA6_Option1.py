from complex import Complex

def main():

    C = map(float, input().split())
    D = map(float, input().split())
    x = Complex(*C)
    y = Complex(*D)
    print('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))

if __name__ == "__main__":
    main()