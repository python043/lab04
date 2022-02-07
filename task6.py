import sys


def intersect(arry1,arry2):
    for n1 in arry1:
        for n2 in arry2:
            if n1==n2:
                print(n1)
def main():
    print("Main start!")
    intersect([3,5,1,7,9],[4,2,6,3,9])
    print("Main  End!.")
if __name__ == "__main__":
    main()

