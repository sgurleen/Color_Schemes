##############################
#Program by Gurleen Kaur
#Instructor - Diana Cukierman
#
#Project - Color Schemes
#
#Main File
#############################

import cmpt120image
import cmpt120Colours

#Color Dictionary
colorDict = {}

#Function to display main menu
userInput = cmpt120Colours.dis_main_menu(colorDict)

#Repeat options
while(userInput != 0 ):
    if userInput == 1:
        numOfColors = cmpt120Colours.load_color_file(colorDict)
        print("The file has been loaded and ", numOfColors,
          " colours are added to the file.\n\n")

    elif userInput == 2:
        cmpt120Colours.print_colors(colorDict)

    elif userInput == 3:
        cmpt120Colours.select_colors(colorDict)

    elif userInput == 4:
        cmpt120Colours.find_closest_color(colorDict)

    elif userInput == 5:
        cmpt120Colours.dis_color_scheme()

    else:
        cmpt120Colours.dis_main_menu(colorDict)

    userInput  = cmpt120Colours.dis_main_menu(colorDict)


#Programs ends here....
