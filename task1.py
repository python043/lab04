import sys

def test(val):
    if val ==0 :
        print('ZERO')
    elif val >0:
        print('POSTIVE')
    elif val < 0:
        print('NEGATIVE')
    else:
        print('NOT A NUMBER')
def main():
    print("Main start!")
    test(1)
    print("Main  End!.")
if __name__ == "__main__":
    main()

