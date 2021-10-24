import keyboard, os, time

def write():
    print('writing')

def read():
    print('reading')
    
def hlp():
    print('not helping')
    
def qt():
    print('not quitting')

SAMPLE = {'QUESTION': 'What do you want to do?',
          'KEY': ['write', 'read', 'help', 'die'],
          'CHOICE': {'write': write(), 'read': read(), 'help': hlp(), 'die': qt()}}

def what():
    '''
    Pretty much the main function
    '''
    os.system('cls')
    temp = []
    CURRENT = 0
    display_choice(SAMPLE['QUESTION'], SAMPLE['KEY'], CURRENT)
    while True:
        if keyboard.is_pressed('down'):
            if CURRENT < len(SAMPLE['KEY']) - 1:
                CURRENT += 1
                os.system('cls')
                display_choice(SAMPLE['QUESTION'], SAMPLE['KEY'], CURRENT)
                time.sleep(0.1)
        elif keyboard.is_pressed('up'):
            if CURRENT > 0:
                CURRENT -= 1
                os.system('cls')
                display_choice(SAMPLE['QUESTION'], SAMPLE['CHOICE'], CURRENT)
                time.sleep(0.1)
        elif keyboard.is_pressed('enter'):
            os.system('cls')
            print('Wise choice')
            time.sleep(1)
            os.system('cls')
            if CURRENT == 0:
                write()
            elif CURRENT == 1:
                read()
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
            
what()
            
            