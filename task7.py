import sys

def pair(arry1,arry2,sum):
    for n1 in arry1:
        for n2 in arry2:
            if n1+n2==sum:
                print(n1,n2)
def main():
    pair([2,3,4],[5,7,9,12],9)
if __name__ == "__main__":
    main()

