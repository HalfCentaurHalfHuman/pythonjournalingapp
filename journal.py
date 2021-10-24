import os, keyboard, time, sys
import msvcrt

# Constant variables
SAMPLE = {'QUESTION': 'Welcome. What do you want to do today?', # UI elements
          'KEY': ['write', 'read', 'help', 'quit']}
standard_length = 10 # The length of the date
path = os.getcwd() # Current working deirectory
global months
global months_number
months = [['jan', 'january'],['feb', 'febuary'],['mar', 'march'],['apr','april'],['may'],['jun', 'june'], 
              ['jul', 'july'],['aug', 'august'],['sep', 'september'],['oct', 'october'],['nov', 'november'],['dec', 'december']]
months_number = ['1','01','2','02','3','03','4','04','5','05','6','06','7','07','8','08','9','09','10','11','12']

def yes_no(question):
    '''
    Simple yes or no question.
    Parameter:
        question: string, the question
    Return:
        bool, depending on the user's answer
    '''
    choice = ''
    done = False
    while not done:
        choice = input(question + ' ')
        if choice in ['Yes', 'yes', 'Y', 'y', 'ye']:
            return True
        elif choice in ['No', 'no', 'N', 'n']:
            return False


def get_date():
    '''
    Get the date from user.
    '''
    date = ''
    # day
    done = False
    while not done:
        cont = True
        day = input('Enter day: ')
        if int (day) < 32 and int(day) > 0:
            if len(day) == 1:
                day = '0' + day
                date += day
                done = True
            elif len(day) == 2:
                date += day
                done = True
        else:
            print('Try again. Try.')
    # month
    done = False
    while not done:
        month = input('Enter month: ')
        if month.lower() in months[0]:
            month = '01'
            date += month
            done = True
        elif month.lower() in months[1]:
            month = '02'
            date += month
            done = True
        elif month.lower() in months[2]:
            month = '03'
            date += month
            done = True
        elif month.lower() in months[3]:
            month = '04'
            date += month
            done = True
        elif month.lower() in months[4]:
            month = '05'
            date += month
            done = True
        elif month.lower() in months[5]:
            month = '06'
            date += month
            done = True
        elif month.lower() in months[6]:
            month = '07'
            date += month
            done = True
        elif month.lower() in months[7]:
            month = '08'
            date += month
            done = True
        elif month.lower() in months[8]:
            month = '09'
            date += month
            done = True
        elif month.lower() in months[9]:
            month = '10'
            date += month
            done = True
        elif month.lower() in months[10]:
            month = '11'
            date += month
            done = True
        elif month.lower() in months[11]:
            month = '12'
            date += month
            done = True
        elif month in months_number:
            done = True
            if len(month) == 1:
                month = '0' + month
                date += month
            elif len(month) == 2:
                date += month
            else:
                print('No.')
                return 1
        else:
            print('Try again.')
            time.sleep(1)
    # year
    done = False
    while not done:
        year = input('Enter year: ')
        if len(year) == 4:
            date += year[2:]
            done = True
        else:
            print('Please try again.')
            time.sleep(1)
    # if everything went well
    return date

def decode_date(date_in):
    '''
    Change the six digit date format to a more conventional format
    '''
    date_out = ''
    # day
    date_out += date_in[:2] + ' '
    # month
    month = date_in[2:4]
    if month[0] == '0':
        month = months[int(month[1]) - 1][1]
        date_out += month[0].upper() + month[1:]
    else:
        month = months[int(month) - 1][1]
        date_out += month
    # year
    date_out += ', ' + '20' + date_in[4:]
    return date_out

def write_journal():
    '''
    Creates a new entry, then helps the user write into it and save afterwards. Does not support editing entries.
    '''
    #input('Press Enter to continue...')
    # Enter Date
    date = get_date()
    # check if entry already exists
    if os.path.isfile(date + '.txt'):
        if yes_no('Entry already exist. Do you want to add to it? You might want to read it first. '):
            os.system('cls')
            print('Start writing your journal. Type in "<done>" (without quotes) and hit ENTER when you are done. \n################################################')
            with open(date + '.txt', 'r') as file:# open in read mode to print out the contents of the entry
                for i in file:
                    sys.stdout.write(i)
                    sys.stdout.flush()
            file = open(date + '.txt', 'a') # now open it again in append mode
        else:
            print('Going back to menu...')
            time.sleep(1)
    else:            
        file = open(date + '.txt', 'w+')
        # Automatic time stamps
        file.write('Daily journal.\n' + decode_date(date) + '\n')
        os.system('cls')
        print('Start writing your journal. Type in "<done>" (without quotes) and hit ENTER when you are done. \n################################################')
    # Starts writing
    temp = ''
    while temp != '<done>':
        temp = input()
        if temp == '<done>': # if the user enters "<done>"
            break
        elif temp == '': # if the user hits Enter without any strings attached, this means an empty line
            file.write('\n')
        else:
            file.write(temp + '\n') # if the user hits Enter, this means he wants to go to a new line, so add "\n" to the text
    os.system('cls')
    print('DONE.')
    file.close()
    time.sleep(1)
    
def find_journal():
    '''
    The actual function that will look for an entry and display it.
    '''
    date = get_date()
    try:
        file = open(date + '.txt', 'r')
        os.system('cls')
        print('########################')
        for i in file:
            print(i)
    except:
        print('Wrong date or entry does not exist...yet.')
    time.sleep(1)
    #input('########################\npress Enter to continue...')
    print('########################')
    
def read_journal():
    '''
    Handles reading journals by prompting use to enter date an look for the entry, then asks if the user wants to read another.
    '''
    done = False
    while not done:
        date = get_date()
        try:
            file = open(date + '.txt', 'r')
            os.system('cls')
            print('################################################')
            for i in file:
                print(i)
        except:
            print('Wrong date or entry does not exist...yet.')
        time.sleep(1)
        print('################################################')
        
        if yes_no('Do you want to read another entry?'):
            done = False
        else:
            done = True
        
def hlp():
    print('''You can choose "Write" to begin writing a diary, or "Read" to read an entry you have written, or "Help" to read this message again, "quit" to quit.

You will be prompted to enter the date of the journal, which will be formatted as follow: DD/MM/YYYY. Example: 05/01/2021

The date will also be the name of the journal file. Time of day is optional, formatted as anything you like.

Have fun journaling. \n''')
    time.sleep(1)
    input('press Enter to continue...')
    
def main():
    '''
    Pretty much the main function.
    '''
    time.sleep(0.5)
    CURRENT = 0
    while True:
        os.system('cls')
        display_choice(SAMPLE['QUESTION'], SAMPLE['KEY'], CURRENT)
        msvcrt.getch()                    # pause the program from further executions until it detects a keystroke
        if keyboard.is_pressed('down'):   # to prevent constant looping and consume resources.
            if CURRENT < len(SAMPLE['KEY']) - 1:
                CURRENT += 1
                os.system('cls')
                display_choice(SAMPLE['QUESTION'], SAMPLE['KEY'], CURRENT)
                time.sleep(0.1)
        elif keyboard.is_pressed('up'):
            if CURRENT > 0:
                CURRENT -= 1
                os.system('cls')
                display_choice(SAMPLE['QUESTION'], SAMPLE['KEY'], CURRENT)
                time.sleep(0.1)
        elif keyboard.is_pressed('enter'):
            os.system('cls')
            if CURRENT == 3:
                print('Bye bye')
            else:
                print('Wise choice')
            time.sleep(1)
            os.system('cls')
            if CURRENT == 0:
                write_journal()
            elif CURRENT == 1:
                read_journal()
            elif CURRENT == 2:
                hlp()
            elif CURRENT == 3:
                quit()
                
def display_choice(question, lst, index):
    '''
    Display helper function, display the question and the current choice.
    '''
    print(question)
    order = 0
    for i in lst:
        if order == index:
            print('[x]' + i)
            order += 1
        else:
            print('[ ]' + i)
            order += 1
        
if __name__ == "__main__":
    main()
    
    
    
    
    
