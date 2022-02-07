import collections
import sys

def four_letter(arry):
    for n in arry:
        if len(n)==4:
            print(n)
def main():
    four_letter(['dog','letter','stop','door','bus','dust'])
if __name__ == "__main__":
    main()

