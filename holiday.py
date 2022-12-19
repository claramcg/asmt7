import datetime as dt 
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from config import save_to_jsonloc
from config import read_jsonloc



# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: dt.date
    
    def __str__ (self):
        return '%s %s' % (self.name, self.date) #string output
          
               
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
    
    def addHoliday(self, holidayObj):     #function for adding holiday OBJECT that is stored in inner holidays
    
           
        # Make sure holidayObj is an Holiday Object by checking the type
        type(holidayObj)
        if type(holidayObj) != Holiday:
            print("Please enter a valid holiday.")
            return
        # Use innerHolidays.append(holidayObj) to add holiday
        self.innerHolidays.append(holidayObj)
        
        # print to the user that you added a holiday
        print(f'{holidayObj} has been added!')

    def findHoliday(self, HolidayName, Date):   # function to find holiday by name, date
        for i in self.innerHolidays:
            if i.name == HolidayName and i.date == Date:
                return Holiday
            else:
                print('Please enter a valid holiday.')

    def removeHoliday(self, HolidayName, Date):   # function search for holiday, remove it
        # Find Holiday in innerHolidays by searching the name and date combination.
        for i in self.innerHolidays:
            if i.name == HolidayName and i.date == Date:
                self.innerHolidays.remove(i)
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
                print(f'{i} has been removed.')
            else:
                print('Please enter a valid holiday.')

    def read_json(self, read_jsonloc):
        with open(read_jsonloc, 'r') as f:
            jsonlist = json.load(f)
            for i in jsonlist['holidays']:
                self.addHoliday(Holiday(i['name'], i['date']))
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    def save_to_json(self, save_jsonloc):
        with open(save_jsonloc, 'j') as c:
            outHolidayList = []
            for i in self.innerHolidays:
                holiday = {'name':i.name, 'date':i.date}
                outHolidayList.append(holiday)
            json.dump(outHolidayList,c str(lst))
            

        # Write out json file to selected file.
        
    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years 2020, current year, and 2  years into the future 2024. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        holidays = []
        for year in range(2020,2025):
            h_url = f"https://www.timeanddate.com/holidays/us/{year}"
            h_r = requests.get(h_url)
            h = h_r.json()

            # inspect website for table name -> holidays-table

            soup = BeautifulSoup(h_r.text, 'html.parser')
            holidayTable = soup.find('table', attrs = {'id':'holidays-table'})
            tableData = holidayTable.find('tbody')


            for row in tableData.find_all('tr'):
                holiday_dict = {}
                date = row.find('th')
                name = row.find('a')
        # Check to see if name and date of holiday is in innerHolidays array
    
                if date is not None and name is not None:
                    date = 
                    date =
        # Add non-duplicates to innerHolidays
                holidays = [holiday_dict(t) for t in {tuple(d.items()) for d in holidays}]

        for i in holidays:
            hday = (Holiday(i['Name'], i['Date']))
            if hday not in self.innerHolidays:
                self.innerHolidays.append(hday)     

        # Handle any exceptions.

        except:





    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(self, year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

       ## SKIP  # def getWeather(weekNum):
                #     # Convert weekNum to range between two days
                #     # Use Try / Except to catch problems
                #     # Query API for weather in that week range
                #     # Format weather information and return weather string.

    def viewCurrentWeek(self):
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        currentWeek = datetime.today()isocalendar().week
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    initList = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    initList.scrapeHolidays()
    # 3. Create while loop for user to keep adding or working with the Calendar
         ## save holiday list = option -> saved = false

    saved = False
    runMenu = True

    # 4. Display User Menu (Print the menu)
    while runMenu:
        print('Holiday Menu\n' \
            '====================\n' \
            '1. Add a Holiday\n' \
            '2. Remove a Holiday\n' \
            '3. Save Holiday List\n' \
            '4. View Holidays\n' \
            '5. Exit\n')
        # 5. Take user input for their action based on Menu and check the user input for errors

        menuOpt = int(input('Please type the number for your desired menu option: '))
        if menuOpt == 1:
            print('Add a Holiday\n' \
                '====================')
            holidayIn = str(input('Holiday: '))
            dateIn = input('Date (use YYYY-MM-DD format): ')
            initList.addHoliday(Holiday(holidayIn, dateIn))
            print('Success:\n' \
                f'{holidayIn} has been added to the holiday list.')
        elif menuOpt == 2:
            print('Remove a Holiday\n' \
                '====================')
            holidayInR = str(input('Name of Holiday: '))
            initList.removeHoliday(holidayInR)
            print('Success:\n' \
                f'{holidayInR} has been removed from the holiday list.')
        elif menuOpt == 3:
            print('Save Holiday List\n' \
                '====================')
            askSave = input('Are you sure you want to save your changes? [y/n]: ')
            if askSave.lower() == 'y':
                initList.save_to_json()
                print('Success:\n' \
                    'Your changes have been saved.')
                saved = True
            else:
                print('Canceled:\n' \
                    'Holiday list file save canceled')
        elif menuOpt == 4:
            print('View Holidays\n' \
                '====================')
            yearIn = input('Which year?: ')
            weekIn = input('Which week? #[1-52, Leave blank for the current week]: ')
            if weekIn == '':
                initList.viewCurrentWeek()
            else:
                print(f'These are the holidays for {yearIn} week #{weekIn}')
                initList.displayHolidaysInWeek(initList.filter_holidays_by_week(yearIn, weekIn))
        elif menuOpt == 5:
            print('Exit\n' \
                '====================')
            if saved == True:
                askExit = input('Are you sure you want to exit? [y/n]: ')
                if askExit.lower() == 'y':
                    print('Goodbye!')
                    break
                elif askExit.lower() == 'n':
                    continue
            elif saved == False:
                askUnsavedExit = input('Are you sure you want to exit?\n' \
                    'Your changes will be lost.\n' \
                    '[y/n]: ')
                if askUnsavedExit.lower == 'y':
                    print('Goodbye!')
                    break
                elif askUnsavedExit.lower() == 'n':
                    continue


    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





