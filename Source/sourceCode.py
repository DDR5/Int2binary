#This program will convert interger values to their binary counter part
import time, sys
def main():
    x = input('Input a interger value to convert to binary. ')
    print('Now converting')
    print('')
    print (bin(x) + ' - Ignore the 0b infront of the binary values, its not important for what you want')
    time.sleep(3)
    y = raw_input('Would you like to input another number? [Y/N]').lower()
    if y == "y":
        main()
    else:
        sys.exit()



main()
    

