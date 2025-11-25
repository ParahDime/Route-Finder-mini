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

def readFile(filepath, locations, connections):
    #open the file and read in
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    data = {
        "num_locations": None,
        "locations": [],
        "num_connections": None,
        "connections": [],
        "travel_costs": {},
        "energy_budget": None
    }


    # helper function embedded
    #items are returned to og function to be usable variables
    def read_count_and_items(start_index, cast_item=lambda x: x):

        count = int(lines[start_index])
        items = []

        for i in range(count):
            items.append(cast_item(lines[start_index + 1 + i]))

        # Return the next index for further parsing
        next_index = start_index + 1 + count
        return count, items, next_index



    i = 0  
    #for each line
    while i < len(lines):
        line = lines[i]

        if line.startswith("#"): #hashtag lines are used to tell what part the program is on
            header = line.lower()

            if "number_of_locations" in header:
                count, _, next_i = read_count_and_items(i + 1)
                data["num_locations"] = count
                i = next_i
                continue

            elif "locations" in header and "one per line" in header:
                count, items, next_i = read_count_and_items(i + 1)
                data["locations"] = items
                i = next_i
                continue

            elif "number_of_connections" in header:
                count, _, next_i = read_count_and_items(i + 1)
                data["num_connections"] = count
                i = next_i
                continue

            elif "each connection" in header:
                def parse_connection(line):
                    a, b, d = line.split()
                    return (a, b, int(d))

                count, items, next_i = read_count_and_items(
                    i + 1,
                    cast_item=parse_connection
                )
                data["connections"] = items
                i = next_i
                continue

            elif "travel_costs_per_location" in header:
                def parse_cost(line):
                    loc, cost = line.split()
                    return (loc, int(cost))

                count, items, next_i = read_count_and_items(
                    i + 1,
                    cast_item=parse_cost
                )
                # Turn list of (loc, cost) into a dict
                data["travel_costs"] = dict(items)
                i = next_i
                continue

            elif "travel_energy_budget" in header:
                # Just a single integer, not a list
                data["energy_budget"] = int(lines[i + 1])
                i += 2
                continue

        i += 1

    locations = data["locations"]
    connections = data["connections"]

def print_menu():
    print("1 | Show all locations (sorted)")
    print("2 | Find shortest path between 2 locations")
    print("3 | Run travel budget estimator")
    print("4 | Insert a new location")
    print("5 | Search for a new location")
    print("6 | Reload dataset")
    print("7 | Exit")

def handle_menu(option):
    match option:
        case 1: #show locations
            print("a")
        case 2: #shortest path between 2 locations
            print("a")
        case 3: #run travel budget estimation
            print("a")
        case 4: #add new location
            print("a")
        case 5: #search for new location
            print("a")
        case 6: #reload the dataset
            print("a")
        case 7: #exit
            exit()
        
#text menu that calls each module


#focus on output

#initialise variables
locations = []
connections = []

data = [] #holds location data

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

readFile(fileName, locations, connections)
print_menu()
menuType = verifyUse(1, 7)

handle_menu(menuType)
#read in data




#main menu
print_menu()