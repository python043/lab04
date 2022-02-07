import sys
import collections

def doubles(arry):
    print(arry)
    prev=0
    for n in arry:
        if prev * 2 == n:
            print(n)
        prev=n


def main():
    doubles([3,0,1,2,3,6,2,4,5,6,5])
if __name__ == "__main__":
    main()


