import dateutil.parser
import random
import matplotlib.pyplot as plt
from sys import argv

def main(filename):
    with open(filename) as file:
        lines = file.readlines()
        x = [dateutil.parser.parse(line) for line in lines]
        x = sorted(x)
        y = [i for i in range(1, len(lines) + 1)]
        assert(isSorted(x))
        assert(len(x)==len(y))
        
        plt.plot(x,y)
        plt.gcf().autofmt_xdate()

        plt.show()

def isSorted(l):
    for i in range(len(l)):
        if i < len(l) - 1 and l[i] > l[i+1]: 
            print(i, "/", len(l)-1, l[i])
            print(i+1,"/",len(l)-1, l[i+1])
            return False
    return True

    

if __name__ == '__main__':
    if(len(argv) > 1):
        main(argv[1])
    else:
        print("No argument supplied!")