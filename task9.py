import sys
def lastfirst(lst):
    
    firstArry=[]
    secondArry=[]
    for name in lst:
        namearray = name.split(",")
        for idx, val in enumerate(namearray):
            if(idx ==0):
                firstArry.append(val)
            elif(idx==1):
                secondArry.append(val)
    print(secondArry)
    print(firstArry)
def main():
    lastfirst(['Gerber,Len','Fox,Kate','Dunn,Bob'])
if __name__ == "__main__":
    main()

