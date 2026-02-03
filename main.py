#packages
import os
import heapq
from bst_directory import BST 
from graph_explorer import GraphExplorer
from travel_dp import travel_dp

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

            elif "connections" in header:
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

                count = data["num_locations"]
                items = []

                for offset in range(count):
                    line = lines[i + 1 + offset]
                    items.append(parse_cost(line))
                # Turn list of (loc, cost) into a dict
                data["travel_costs"] = dict(items)
                i = i + 1 + count
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

def handle_menu(option, travel, explorer, bst):
    data_state = False
    match option:
        case 1: #show locations
            for name in bst.order():
                print(bst.name)

        case 2: #shortest path between 2 locations
            start = input("Start location: ")
            end = input("End location: ")
           
            result = explorer.shortest_path(start, end)
           #output shortest path
            if result is None:
                print("No path found.")
            else:
                distance, path = result
                print("Distance:", distance)
                print("Path:", " -> ".join(path))
    
        case 3: #run travel budget estimation
            print("Max locations visitable:", travel.max_locations())
        case 4: #add new location
            name = input("Location name: ")
            bst.insert(name)
            explorer.graph[name] = []
            data_state["modified"] = True
            #send to function, take info (can be manual)
        case 5: #search for new location
            name = input("Location name: ")
            found = bst.search(name)
            print("Found" if found else "Not found")
        case 6: #reload the dataset
            print("a")
            #redo dataset
        case 7: #exit
            if data_state == False:
                exit()
            else: #if data has been modified
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

graphExplorer = GraphExplorer()
tripTravel = travel_dp(0, 15) #needs travel and budget
bst = BST()

readFile(fileName, locations, connections)
print_menu()

menuType = verifyUse(1, 7)

handle_menu(menuType, tripTravel, graphExplorer, bst)
#read in data




#main menu
print_menu()