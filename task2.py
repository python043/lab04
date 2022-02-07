import sys

def multi3(arry):
    print(arry)
    for n in arry:
        if n % 3 == 0:
            print(n)

def main():
    multi3([3,1,6,2,3,9,7,9,5,4,5])
if __name__ == "__main__":
    main()

