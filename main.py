#packages
import os
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


def selectFile(fileSize):
    labels = {
        1: "small",
        2: "medium",
        3: "large"
    }
    return labels.get(fileSize, "invalid") #converts fileSize to a string with the size

def verifyFile(name): #verify the file exists
    return os.path.isfile(name)



def readFile(): #read the contents of the file
    a = 1

def print_menu():
    print("1 | Show all locations (sorted)")
    print("2 | Find shortest path between 2 locations")
    print("3 | Run travel budget estimator")
    print("4 | Insert a new location")
    print("5 | Search for a new location")
    print("6 | Reload dataset")
    print("7 | Exit")


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
else:
    quit()

#read in files
fileType = verifyUse(0, 3)
fileType = selectFile(fileType)
fileName = "map_" + fileType + ".txt"
if(verifyFile(fileName)):
    print("File located")
else:
    print("File not found")
    quit()

#read in data



#main menu
print_menu()