##############################
#Program by Gurleen Kaur
#Instructor - Diana Cukierman
#
#Project - Color Schemes
#
#Utilities File
#############################

import cmpt120image


#Function to find Complementary
def complement(rgbList):
    comp = [0,0,0]
    for i in range(len(rgbList)):
        comp[i] = 255 - rgbList[i]

    return comp


#Function to get the hexadecimal value of RGB values
def hex_value(rgbList):
    r = hex(int(rgbList[0])).lstrip('0x').rstrip("L")
    g = hex(int(rgbList[1])).lstrip('0x').rstrip("L")
    b = hex(int(rgbList[2])).lstrip("0x").rstrip("L")

    if r == "":
        rval = "00"
    else:
        rval = r
    if g == "":
        gval = "00"
    else:
        gval = g
    if b == "":
        bval = "00"
    else:
        bval = b

    finalval  = "#" + rval + gval + bval

    return finalval


#Function to make a colored square
def color_square(rgbList, height, width):
    square = [[rgbList for i in range(width)] for j in range(height)]

    return square


#Function to Lighten the pixels
def lighten_pixels(rgbList, per):
    lightList = [0,0,0]
    for i in range(len(rgbList)):
        lightList[i] = int(rgbList[i] + (255-rgbList[i])*per)

    return lightList


#Function to darken the pixels
def darken_pixels(rgbList, per):
    darkList = [0,0,0]
    for i in range(len(rgbList)):
        darkList[i] = int(rgbList[i]*per)

    return darkList

#Function to create a monochromatic scheme
def monochrom_scheme(rgbList):

    monoImg = color_square([0,0,0],240,240)
    baseSquare = color_square(rgbList,240,240)
    lenbSquare = len(baseSquare)
    smallSquare = int(lenbSquare/3)
    for i in range(lenbSquare):
        for j in range(lenbSquare):
            if i>=0 and i<smallSquare and j>=0 and j <smallSquare:
                monoImg[i][j] = lighten_pixels(baseSquare[i][j], 0.8)

            elif i>=0 and i<smallSquare and j>=smallSquare*2 and j<lenbSquare:
                monoImg[i][j] = lighten_pixels(baseSquare[i][j], 0.5)

            elif i>=smallSquare*2 and i<lenbSquare and j>=0 and j<smallSquare:
                monoImg[i][j] = darken_pixels(baseSquare[i][j], 0.5)

            elif i>=smallSquare*2 and i<lenbSquare and j>=smallSquare*2 \
                and j<lenbSquare:
                monoImg[i][j] = darken_pixels(baseSquare[i][j], 0.8)

            else:
                monoImg[i][j] = baseSquare[i][j]

    return monoImg

#Function to create complementary scheme
def compl_scheme(rgbList):
    complImg = color_square([0,0,0], 240, 480)
    base = monochrom_scheme(rgbList)
    compl = monochrom_scheme(complement(rgbList))

    for i in range(len(complImg)):
        complImg[i] = base[i]+compl[i]

    return complImg



#Function to load file
def load_color_file(loadcolDict):

    #Loading the colors file
    file  = open("colours.csv")

    #Adding values of the file to dictionary
    for line in file:
        lineList = line.strip("\n").split(",")
        hexVal = hex_value([lineList[1],lineList[2],lineList[3]])
        if tuple([lineList[1],lineList[2],lineList[3]]) not in loadcolDict.keys():
            loadcolDict[(lineList[1],lineList[2],lineList[3])] = \
                                        [lineList[0], hexVal]

    return len(loadcolDict)


#Function to display Main Menu
def dis_main_menu(menucolDict):
    print(" 1. Load the Color File\n",
      "2. Print All Colours\n",
      "3. Select Colour\n",
      "4. Find the Closest Colour\n",
      "5. Display(Save) Colour Scheme\n",
      "0. Quit\n")

    #User Input for the given options
    userIn = input("Select an Option: ")

    return int(userIn)


#Function to print Colour Table
def print_colors(printcolDict):

    load_color_file(printcolDict)

    #Print Header
    print("{:<16}{:>10}{:>10}{:>10}{:>15}".format("Color Name",
                                    "Red", "Green", "Blue", "Hex"))

    print("---------------------------------------------------------")
    #Print data lines
    for k,v in printcolDict.items():
        print("{:<16}{:>10}{:>10}{:>10}{:>15}".format(v[0].capitalize(),
         k[0],k[1],k[2],v[1].upper()))

    print("\n\n------------------------------------------------------")
    print("------------------------------------------------------\n\n")


#Function search and add Colours
def select_colors(selectcolDict):

    load_color_file(selectcolDict)

    #User input for RGB values
    print("Enter the RGB values of your colour.")
    colCode = "RGB"
    colList = []
    for c in colCode:
        print(c, end = ':')
        usrCol = input()
        while int(usrCol)<0 or int(usrCol)>255:
            print("Please enter a value between 0 and 255")
            print(c, end = ':')
            usrCol = input()
        colList.append(usrCol)

    found = False
    for k,v in selectcolDict.items():
        if k == tuple(colList):
            found = True
            print("Colour", colList, "is", v[0], "and has hex code ",
                  v[1].upper())

    if found == False:
        print("Colour", colList, "not found.",
                "Would you like to:\n\n",
                "1. Enter a name for this Colour: \n",
                "2. Return to the main menu")

        usrOp = input("Select an Option: ")

        if int(usrOp) == 1:
            colName  = input("\nWhat is the name of Colour? ")
            selectcolDict[tuple(colList)] = [colName, hex_value(colList)]

            print(colName, "(", hex_value(colList).upper(), ")",
                  "has been added to the file.")

    print("\n\n------------------------------------------------------")
    print("------------------------------------------------------\n\n")


#Function to find the closest colour
def find_closest_color(colDict):
    load_color_file(colDict)

    #Dictionary to store rgb  as keys
    #abs differences as values
    absSumDict = {}

    #User input for RGB
    print("Enter the RGB values of your colour.")
    colCode = "RGB"
    colList = []
    for c in colCode:
        print(c, end = ':')
        usrCol = input()
        while int(usrCol)<0 or int(usrCol)>255:
            print("Please enter a value between 0 and 255")
            print(c, end = ':')
            usrCol = input()
        colList.append(usrCol)

    #Conditions if the color is in the dictionary
    found = False
    for k,v in colDict.items():
        if k == tuple(colList):
            found = True
            print("Colour", colList, "is", v[0], "and has hex code ",
                  v[1].upper())

    #If the color is not in dictionary
    if found == False:

        for k,v in colDict.items():
            print(k,k[0])
            absSumDict[k] = abs(int(colList[0]) - int(k[0]))+ \
                            abs(int(colList[1]) - int(k[1]))+ \
                            abs(int(colList[2]) - int(k[2]))

        sumList =  list(absSumDict.values())

        #return index of min number in the list of differences
        minDiffIndex = sumList.index(min(sumList)) #returns index of

        #Returns key of the minimum difference
        closestKey = list(absSumDict.keys())[minDiffIndex]

        print("The closest colour to ", colList,
          "is ", closestKey, colDict[closestKey][0].capitalize(),
          "with hex code ", colDict[closestKey][1].upper(),
          "\nThe absolute difference is ",min(sumList))

    print("\n\n------------------------------------------------------")
    print("------------------------------------------------------\n\n")


#Function to display Color Scheme
def dis_color_scheme():
    print("Enter the RGB values of your base colour.\n")
    colCode = "RGB"
    colList = []
    #Loop to take user input for rgb values
    for c in colCode:
        print(c, end = ':')
        usrCol = input()
        while int(usrCol)<0 or int(usrCol)>255:
            print("Please enter a value between 0 and 255")
            print(c, end = ':')
            usrCol = input()
        colList.append(int(usrCol))
    print("Which colour scheme do you wish to display?\n",
          "Enter M or C\n",
          "M. Monochrome\n C. Complementary\n\n")
    userIn = input("Select an option: ")

    #Condition to display color scheme
    if userIn.upper() == "M":
        monoScheme = monochrom_scheme(colList)
        cmpt120image.showImage(monoScheme)
        cmpt120image.saveImage(monoScheme, "mscheme.png")

    elif userIn.upper() == "C":
        compScheme = compl_scheme(colList)
        cmpt120image.showImage(compScheme)
        cmpt120image.saveImage(compScheme, "cscheme.png")

    else:
        print("\n\nThat is not a valid input.\n\n")


#Programs ends here....
