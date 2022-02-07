import sys

def evenrow(arr1):
    sum=0
    for x in arr1:
      for y in x:
        sum=sum+y
    if sum %2 ==0:
        print('TRUE')
    else:
        print('FALSE')
def main():
    evenrow([[1,3],[2,4]])
if __name__ == "__main__":
    main()

