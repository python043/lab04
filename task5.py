import sys

def inBoth(arry1,arry2):
    found=0
    for n1 in arry1:
        for n2 in arry2:
            if n1==n2:
                found=1
    if found==1:
        print('TRUE')
    else:
        print('FALSE')
    
    

def main():
    inBoth([3,2,5,4,7],[9,0,1,3])
if __name__ == "__main__":
    main()

