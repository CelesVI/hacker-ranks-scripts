def print_formatted(number):
    # your code goes here
    width= len("{0:b}".format(number))
    for i in range(1, number+1):
        #print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=width))
        print("{0:d}".format(i).rjust(width)+" "+"{0:o}".format(i).rjust(width)+" "+"{0:x}".format(i).rjust(width).upper()+" "+"{0:b}".format(i).rjust(width))

        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
