"""This program is to update, search, and display state's capital, population, and flowers"""

#imports
import sys
import os
import matplotlib.pyplot as plt


#multidimensional array of states, capitals, flower, and population
states = [["Alabama", "Montgomery", "Camellia", "5,024,279", os.path.join(sys.path[0] + "\\" +
"Camellia.jpg")],["Alaska", "Juneau", "Forget Me Not", "733,391",os.path.join(sys.path[0] +
"\\" + "Forget Me Not.jpg")], ["Arizona", "Phoenix", "Saguaro Cactus Blossom", "7,151,502",
os.path.join(sys.path[0] + "\\" + "Saguaro Cactus Blossom.jpg")], ["Arkansas", "Little Rock",
"Apple Blossom", "3,011,524", os.path.join(sys.path[0] + "\\" + "apple blossom.jpg")],
["California", "Sacramento", "California Poppy", "39,538,223", os.path.join(sys.path[0] +
"\\" + "california poppy.jpg")], ["Colorado", "Denver", "White and Lavender Columbine",
"5,773,714", os.path.join(sys.path[0] + "\\" + "white and lavender columbine.jpg")],
["Connecticut", "Hartford", "Mountain Laurel", "3,605,944", os.path.join(sys.path[0] +
"\\" + "smountaijn laurel.jpg")], ["Delaware", "Dover", "Peach Blossom", "989,948",
os.path.join(sys.path[0] + "\\" + "peach blossom.jpg")], ["Florida", "Tallahassee",
"Orange Blossom", "21,538,187", os.path.join(sys.path[0] + "\\" + "sorange blossom.jpg")],
["Georgia", "Atlanta", "Cherokee Rose", "10,711,908", os.path.join(sys.path[0] + "\\" +
"cherokee rose.jpg")], ["Hawaii", "Honolulu", "Hibiscus", "1,455,271", os.path.join(sys.path[0]
+ "\\" + "hibiscus.jpg")], ["Idaho", "Boise", "Syringa", "1,839,106", os.path.join(sys.path[0] +
"\\" + "syringa.jpg")], ["Illinois", "Springfield", "Purple Violet", "12,812,508",
os.path.join(sys.path[0] + "\\" + "purple violet.jpg")], ["Indiana", "Indianapolis", "Peony",
"6,785,528", os.path.join(sys.path[0] + "\\" + "peony.jpg")], ["Iowa", "Des Moines",
"Wild Prairie Rose", "3,190,369", os.path.join(sys.path[0] + "\\" + "wild prairie rose.jpg")],
["Kansas", "Topeka", "Sunflower", "2,937,880"], ["Kentucky", "Frankfort", "Goldenrod", "4,505,836"],
["Louisiana", "Baton Rouge", "Magnolia", "4,657,757"], ["Maine", "Augusta",
"White Pine Cone and Tassel", "1,362,359"], ["Maryland", "Annapolis", "Black-Eyed Susan",
"6,177,224", os.path.join(sys.path[0] + "\\" + "black eyed susan.jpg")],
["Massachusetts", "Boston", "Mayflower", "7,029,917", os.path.join(sys.path[0] +
    "\\" + "mayflower.jpg")], ["Michigan", "Lansing", "Apple Blossom", "10,077,331",
os.path.join(sys.path[0] + "\\" + "apple blossom.jpg")], ["Minnesota", "Saint Paul",
"Pink and White Lady Slipper", "5,706,494", os.path.join(sys.path[0] + "\\" +
"Pink and White Lady Slipper.jpg")], ["Mississippi", "Jackson", "Magnolia", "2,961,279",
os.path.join(sys.path[0] + "\\" + "magnolia.jpg")], ["Missouri", "Kefferson City",
"White Hawthorn Blossom", "6,154,913", os.path.join(sys.path[0] + "\\" +
"white hawthorn blossom.jpg")], ["Montana", "Helena", "Bitterroot", "1,084,225",
os.path.join(sys.path[0] + "\\" + "bitterroot.jpg")], ["Nebraska", "Lincoln", "Goldenrod",
"1,961,504", os.path.join(sys.path[0] + "\\" + "goldenrod.jpg")], ["Nevada", "Carson City",
"Sagebrush", "3,104,614", os.path.join(sys.path[0] + "\\" + "sagebrush.jpg")], ["New Hampshire",
"Concord", "Purple Lilac", "1,377,529", os.path.join(sys.path[0] + "\\" + "purple lilac.jpg")],
["New Jersey", "Trenton", "Violet", "9,288,994", os.path.join(sys.path[0] + "\\" + "violet.jpg")],
["New Mexico", "Santa Fe", "Yucca Flower", "2,117,522", os.path.join(sys.path[0] + "\\" +
"yucca flower.jpg")], ["New York", "Albany", "Rose", "20,201,249", os.path.join(sys.path[0] + "\\" +
"rose.jpg")], ["North Carolina", "Raleigh", "Dogwood", "10,439,388", os.path.join(sys.path[0] + "\\"
+ "dogwood.jpg")], ["North Dakota", "Bismarck", "Wild Prarie Rose", "779,094",
os.path.join(sys.path[0] + "\\" + "wild prairie rose.jpg")], ["Ohio", "Columbus",
"Scarlet Carnation", "11,799,448", os.path.join(sys.path[0] + "\\" + "scarlet carnation.jpg")],
["Oklahoma", "Oklahoma City", "Mistletoe", "3,959,353", os.path.join(sys.path[0] + "\\" +
    "mistletoe.jpg")], ["Oregon", "Salem", "Oregon Grape", "4,237,256", os.path.join(sys.path[0] +
    "\\" + "oregon grape.jpg")], ["Pennsylvania", "Harrisburg", "Mountain Laurel", "13,002,700",
    os.path.join(sys.path[0] + "\\" + "mountain laurel.jpg")], ["Rhode Island", "Providence",
    "Violet", "1,097,379", os.path.join(sys.path[0] + "\\" + "violet.jpg")], ["South Carolina",
    "Columbia", "Yellow Jessamine", "5,118,425", os.path.join(sys.path[0] + "\\" +
"yellow jessamine.jpg")], ["South Dakota", "Pierre", "Pasque Flower", "886,667",
os.path.join(sys.path[0] + "\\" + "spasque flower.jpg")], ["Tennessee", "Nashville", "Iris",
"6,910,840", os.path.join(sys.path[0] + "\\" + "iris.jpg")], ["Texas", "Austin", "Bluebonnet",
"29,145,505", os.path.join(sys.path[0] + "\\" + "bluebonnet.jpg")], ["Utah", "Salt Lake City",
"Sego Lily", "3,271,616", os.path.join(sys.path[0] + "\\" + "sego lily.jpg")], ["Vermont",
"Montpelier", "Red Clover", "643,077", os.path.join(sys.path[0] + "\\" + "red clover.jpg")],
["Virginia", "Richmond", "Dogwood", "8,631,393", os.path.join(sys.path[0] + "\\" + "dogwood.jpg")],
["Washington", "Olympia", "Pink Rhododendron", "7,705,281", os.path.join(sys.path[0] + "\\" +
    "pink rhododendron.jpg")], ["West Virginia", "Charleston", "Rhododendron", "1,793,716",
os.path.join(sys.path[0] + "\\" + "rhododendron.jpg")], ["Wisconsin", "Madison", "Wood Violet",
"5,893,718", os.path.join(sys.path[0] + "\\" + "wood violet.jpg")], ["Wyoming", "Cheyenne",
"Indian Paintbrush", "576,851", os.path.join(sys.path[0] + "\\" + "indian paintbrush.jpg")]]


#function to display all states in alphabetical order as well as capital, population, and flower

def display_all():
    """this function displays all of the states in alphabetical order, the capital, population,
    and state flower"""
    var_x = 0
    while var_x <= 49:
        print("State: " + states[var_x][0])
        print("Capital: " + states[var_x][1])
        print("State Flower: " + states[var_x][2])
        print("State Population: " + states[var_x][3] + "\n")
        var_x += 1


#function to search for specific state and display appropriate information
def find_state():
    """This function is to find a specific state and display the needed information"""
    search = input("What State Information would you like to find?: ")
    for state_info in states:
        if state_info[0].upper() == search.upper():
            print("State: " + state_info[0])
            print("Capital:" + state_info[1])
            print("State Flower: " + state_info[2])
            print("State Population: " + state_info[3])
            print(state_info[4])
            return
    print("State Not Found")


#function to provide a bar braph of the top 5 populated states that shows overall population
def bar_graph():
    """This function provides a bar graph of the top 5 states and their overall population"""
    states.sort(key=lambda state_info: int(state_info[3].replace(',', '')))
    states_five = states[-5:]
    print(states_five)
    axis_x = []
    axis_y = []
    for state_info in states_five:
        axis_x.append(state_info[0])
        axis_y.append(state_info[3])
    plt.bar(axis_x, axis_y)

    plt.title('Top 5 States By Population')
    plt.xlabel('State')
    plt.ylabel('Population')
    plt.show()


#function to update the overall state population for specific state
def overall_population():
    """This function is to update the population on specific states"""
    search = input("What state population would you like to update?: ")
    new_population = str(input("What is the new population of the state?: "))
    for state_info in states:
        if state_info[0].upper() == search.upper():
            state_info[3] = new_population
            print("State: " + state_info[0])
            print("Capital:" + state_info[1])
            print("State Flower: " + state_info[2])
            print("State Population: " + state_info[3])



#function to exit the program
def exit_program():
    """This function is to exit the program"""
    print("Thank you for using our program!")
    sys.exit(0)


#function to display the menu and the running options
def menu():
    """This function is to display the menu associated with the functions to run"""
    print("Option 1: Display all of the states in alphabetical order with the capitals, "
    	"population, and state flower.")
    print("Option 2: Find and display a specific state's information")
    print("Option 3: Display the top five state populations using a bar graph.")
    print("Option 4: Show the overall population for a specific state")
    print("Option 0: Exit")



CHOICE = None
while CHOICE != 0:
    menu()

    CHOICE = input("Please select a menu choice: \n")

    if CHOICE == "1":
        display_all()
    elif CHOICE == "2":
        find_state()
    elif CHOICE == "3":
        bar_graph()
    elif CHOICE == "4":
        overall_population()
    elif CHOICE == "0":
        exit_program()
    else:
        print("Please make a valid choice")
