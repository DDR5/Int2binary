#This program will convert interger values to their binary counter part
import time, sys
con = True
while con == True:
    x = input('Input a interger value to convert to binary. ')
    print('Now converting \n')
    print (bin(x) + ' - Ignore the 0b infront of the binary values, its not important for what you want')
    time.sleep(3)
    y = raw_input('Would you like to input another number? [Y/N]').lower()
    if y == "y":
     con = con   
    else:
        con = False


    

