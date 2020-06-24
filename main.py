# variable declaration
import sys
hid_word = 'ironman'
dashes = ['_'] * len(hid_word)
chances = 10


def display_dashes():
    global dashes
    for x in dashes:
        print(x, end=' ')


def get_move():
    global hid_word, dashes, chances
    letter = input("Enter a letter to guess : ")
    if len(letter) > 1:
        print('Please enter only letters')
    else:
        if letter in hid_word:
            print('Guesssed letter present in word')
            for x in range(len(hid_word)):
                if letter == hid_word[x]:
                    dashes[x] = letter
        else:
            print('guessed letter not in word')
        # print(dashes)
        chances-=1
        print("Chances left ",chances)
        check_win()

def check_win():
    global hid_word,dashes,chances
    if chances==0:
        print("You lost the secret word was :",hid_word)
        sys.exit(0)
    else:
        # flg=0
        # for x in dashes:
        #     if x=='_':
        #         flg=1
        # if flg==0:
        #     print('You won the game')
        #     sys.exit(0)

        str_dashes=''.join(dashes)
        # print(str_dashes)
        if str_dashes.find('_')==-1:
            print('You won')
            sys.exit(0)



print('\t\t\t Hangaman game')
print('*'*50)
display_dashes()
print('')
while(True):
    get_move()
    display_dashes()
    print('')

# check_win()




