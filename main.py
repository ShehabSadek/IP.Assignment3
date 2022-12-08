from ImageMasking import *
from VideoMasking import *
from termcolor import colored


while(True):
    print(colored('Orange Detection Mode','white',attrs=["reverse"]))
    print("1){}".format(colored('Image Masking', 'blue')),"\n2){}".format(colored('Video Masking', 'yellow')),"\n3){}".format(colored('Exit', 'red')))
    choice = input("Pick desired option:")
    if(choice=='1'):
        imgMasking()
        continue
    elif(choice=='2'):
        vidMasking()
        continue
    elif(choice=='3'):
        break
    else:
        print(colored("INVALID INPUT !",'red'))