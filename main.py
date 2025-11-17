#packages

#used to verify if the file is read or exit (loop)
def verifyUse(min, max):
    while True: #will loop infinitely until the condition is met
        num = input()
        try:
            num = int(num)
        except ValueError:
            print("Not a valid value. Please try again")
            
        if min <= num and max >= num:
            return num
        else:
            print("Not a valid input. Please try again")


def selectFile():
    pass

def verifyFIle(name):
    pass



def readFile():
    a = 1




#text menu that calls each module


#focus on output

#initialise variables

#ask for type of file read in
print("Route explorer")
print("===========\n")
print("1 | Load Dataset")
print("0 | Exit")

if(verifyUse(0, 1) == 1):
    print("Please choose a file type:")
    print("1 | Small\n2 | Medium\n3 | Large\n\n0 | Quit")
    fileType = verifyUse(0, 3)

    fileName = "map_" + " " + ".txt"
    verifyFIle(fileName)
    pass
else:
    quit()
#read in files

