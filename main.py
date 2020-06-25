# variable declaration
import sys

hid_word = 'ironman'
dashes = ['_'] * len(hid_word)
chances = 6
cur_cnt=1

def display_dashes():
    global dashes
    for x in dashes:
        print(x, end=' ')


def get_move():
    global hid_word, dashes, chances , letter_input
    global chance_label,present_label,dash_label,cur_cnt,hang_man_img , img
    letter = letter_input.get()
    if len(letter) > 1:
        # print('Please enter only letters')
        present_label['text']='Please enter only letters'
        present_label.pack()
    else:
        ans=''
        if letter in hid_word:
            ans='Guesssed letter present in word'
            for x in range(len(hid_word)):
                if letter == hid_word[x]:
                    dashes[x] = letter
        else:
            ans='guessed letter not in word'
            img=PhotoImage(file=f'hangman_pics/hangman_step{cur_cnt}.png')
            hang_man_img['image']=img
            hang_man_img.pack()
            cur_cnt+=1
        # print(dashes)
        chances-=1
        present_label['text']=ans
        present_label.pack()
        dash_label['text']=''.join([x+' ' for x in dashes])
        dash_label.pack()
        chance_label['text']="chances left : "+str(chances)
        chance_label.pack()
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



# print('\t\t\t Hangaman game')
# print('*'*50)
# display_dashes()
# print('')
# while(True):
#     get_move()
#     display_dashes()
#     print('')

# check_win()

##################################

from tkinter import Tk
from tkinter import *
from tkinter import font
root=Tk()

def print_letter():
    global letter_input
    print(letter_input.get())

ff=font.Font(size='25')
heading=Label(root,text="Hangman Game")
heading.pack()
heading['font']=ff
f1=Frame(root)
f2=Frame(root)
f1.pack()
f2.pack()
img=PhotoImage(file='C:\\Users\\Balarubinan\\PycharmProjects\\Hangman_game\\hangman_pics\\hangman_step5.png')
hang_man_img=Label(f1,image=img)
hang_man_img.pack()
hang_man_img['font']=ff
dash_label=Label(f1,text='_ '*7)
dash_label.pack()
dash_label['font']=ff
chance_label=Label(f1,text='present')
chance_label.pack()
chance_label['font']=ff

present_label=Label(f1,text='chances left is : 10')
present_label.pack()
present_label['font']=ff

letter_input=Entry(f2)
letter_input.grid(row=0,column=0)
letter_input['font']=ff
btn=Button(f2,text='Guess',command=get_move)
btn.grid(row=0,column=1)
btn['font']=ff
root.mainloop()


