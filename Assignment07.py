#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# ABruck, 2021-Feb-2, Created File
# ABruck, 2021-Mar-2, Modified File
#------------------------------------------#

import pickle
# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
# Change text file to binary file
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:

    # Need to put @staticmethod before all your method declaration for these classes.
    @staticmethod
    # def delete_inventory(table):
    # Since we should not be prompting for user input inside of DataProcessor
    #   we need to also accept as an argument the ID we with to remove.
    def delete_inventory(table, id_to_remove):

        # We do not want to make any calls to outside class methods.
        # IO.show_inventory(table)
        # 3.5.1.2 ask user which ID to remove
        # This violates SoC and should be in IO or the main while loop.
        # intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == id_to_remove:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

        # No outside class calls.
        # IO.show_inventory(table)
    
    @staticmethod
    def add_to_inventory(cd_id, cd_title, cd_artist, table):
        new_cd = {
            'ID': int(cd_id),
            'Title': cd_title,
            'Artist': cd_artist
        }
        table.append(new_cd)



class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        # Using pickle.load to read data from binary file        
        with open(file_name, 'rb') as fileobj:
            data = pickle.load(fileobj)
            
    @staticmethod
    def write_file(data, file_name):
        
        # No function calls to external class methods
        # IO.show_inventory(table)

        # No prompting for user input inside of FileProcessor
        # strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # if strYesNo == 'y':
            
            
        # Using pickle.dump to write data on binary file
            with open(file_name, 'wb') as fileobj:
                pickle.dump(data, fileobj)
        
        # else:
        #     input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice_list = ['l', 'a', 'i', 'd', 's', 'x']
        choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        try : 
            choice_list.index(choice) 
            res = "Element found"
        except ValueError : 
                res = "Element not in list !"
                print()  # Add extra space for layout
        
        # Printing result 
        print("The value after catching error : " + str(res))
        return choice 

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # We need to have @staticmethod before each of our methods
    @staticmethod
    def add_inventory():
        
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()

        return strID, strTitle, stArtist

        # intID = int(strID)
        # dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        # lstTbl.append(dicRow)
        # IO.show_inventory(lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit firstcls
    if strChoice == 'x':
        break

    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # 3.3 process add a CD
    elif strChoice == 'a':
        # The IO function call should get the data from the user and return it to here.
        # IO.add_inventory()
        # 3.3.1 Ask user for new ID, CD Title and Artist
        cd_id, cd_title, cd_artist = IO.add_inventory()
        # 3.3.2 Add item to the table
        DataProcessor.add_to_inventory(cd_id, cd_title, cd_artist, lstTbl)

    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # DataProcessor.delete_inventory(lstTbl)
        DataProcessor.delete_inventory(lstTbl, intIDDel)

    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        # First we display inventory
        IO.show_inventory(lstTbl)
        # Then prompt for verification.
        #   This could also be made into a method in the IO class or left here.
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(lstTbl, strFileName)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')

        
        continue  # start loop back at top.

    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




