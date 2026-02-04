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
            continue
            
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

def readFile(filepath, data):
    #open the file and read in
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]


    # helper function embedded
    #items are returned to og function to be usable variables
    i = 0  
    #for each line
    while i < len(lines):
        line = lines[i]

        if line.startswith("#"): #hashtag lines are used to tell what part the program is on
            header = line.lower()

            if "number_of_locations" in header:
                data["num_locations"] = int(lines[i + 1])
                i += 2
                continue

            elif "available_locations" in header:
                count = data["num_locations"]
                #items, next_i = read_count_and_items(i + 1)
                data["locations"] = lines[i + 1 : i + 1 + count]
                i = i + 1 + count
                continue

            elif "number_of_connections" in header:
                #count, _, next_i = read_count_and_items(i + 1)
                data["num_connections"] = int(lines[i + 1])
                i += 2
                continue

            elif "connections" in header:
                def parse_connection(line):
                    a, b, d = line.split()
                    return (a, b, int(d))

                count = data["num_connections"]
                connections = []

                for j in range(count):
                    a, b, d = lines[i + 1 + j].split()
                    connections.append((a, b, int(d)))

                data["connections"] = connections
                i = i + 1 + count
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

    #locations = data["locations"]
    #connections = data["connections"]

def print_menu():
    print("1 | Show all locations (sorted)")
    print("2 | Find shortest path between 2 locations")
    print("3 | Run travel budget estimator")
    print("4 | Insert a new location")
    print("5 | Search for a location")
    print("6 | Reload dataset")
    print("7 | Exit")

def handle_menu(option, travel, explorer, bst, data_modified):

        match option:
            case 1: #show locations
                locations = bst.inorder()
                for location in locations:
                    print(location)

            case 2: #shortest path between 2 locations
                start = input("Start location: ")
                end = input("End location: ")
            

                result = explorer.shortest_path(start, end)
            #output shortest path
                if result is None:
                    print("No path found.")
                else:
                    distance, path = result
                    print("Path:", distance)
                    print("Distance:", path)
        
            case 3: #run travel budget estimation
                #TOFIX
                if not data["travel_costs"] or data["energy_budget"] is None:
                    print("Travel data not loaded.")
                    return

                max_locations = travel.max_visitable_locations()

                print(f"With an energy budget of {data['energy_budget']},")
                print(f"you can visit at most {max_locations} locations.")
            case 4: #add new location               
                #Name
                name = input("Enter new location name: ").strip()
                if name in data["locations"]:
                    print("Location already exists")
                    return False

                #Travel amount
                try:
                    cost = int(input("Enter travel cost for this location: "))
                except ValueError:
                    print("Invalid cost.")
                    return False

                #Add to data
                data["locations"].append(name)
                data["travel_costs"][name] = cost
                data["num_locations"] += 1

                #Insert to BST
                bst.insert(name)

                #add to graph
                graphExplorer.graph[name] = []

                
                connected = False
                #Add a connection
                while connected == False:
                    other = input("Enter existing location name: ").strip()

                    if other not in data["locations"]:
                        print("That location does not exist. Skipping connection.")
                    else:
                        try:
                            distance = int(input("Enter distance between locations: "))
                        except ValueError:
                            print("Invalid distance. Skipping connection.")
                        else:
                            data["connections"].append((name, other, distance))
                            data["num_connections"] += 1

                            graphExplorer.graph[name].append((other, distance))
                            graphExplorer.graph[other].append((name, distance))

                    connected = True
                print(f"Location '{name}' added successfully.")
                data_modified = True
            case 5: #search for a location
                name = input("Location name: ")
                found = bst.search(name)
                print("Found" if found else "Not found")
            case 6: #reload the dataset
                #TOFIX
                print("a")
                #redo dataset
            case 7: #exit
                #TOFIX
                run = False
                if data_modified == False:
                    exit()
                else: #if data has been modified
                    return

        

#initialise variables
data = {
        "num_locations": None,
        "locations": [],
        "num_connections": None,
        "connections": [],
        "travel_costs": {},
        "energy_budget": None
    } #holds location data

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
 #needs travel and budget
bst = BST()

readFile(fileName, data)

#populate BST
for location in data["locations"]:
    bst.insert(location)

#build graph for graphexplorer
graphExplorer.build_graph(data["locations"], data["connections"])
tripTravel = travel_dp(data["travel_costs"], data["energy_budget"])

data_modified = False
run = True
while run:
    print_menu()
    menuType = verifyUse(1, 7)
    handle_menu(menuType, tripTravel, graphExplorer, bst, data_modified)

if data_modified == True:
    pass