from tkinter import *
import tkinter.ttk as ttk
import random

dictionary_Eng_words = {}
with open("English_words3.txt", encoding = 'utf-8') as file:
    for line in file:
        key, *value = line.split()
        dictionary_Eng_words[key] = value




class English:

    def main_menu(self):
        self.button_learn.place_forget()
        self.button_settings.place_forget()
        self.button_exit.place_forget()
        button_new_words = ttk.Button(text = 'Новые слова')
        button_new_words.place(x = 265, y = 220)
        button_repeat = ttk.Button(text = 'Повторение')
        button_repeat.place(x = 265, y = 250)



    def __init__(self):
        """Main window
        учить(новые слова / повторение)
        настройки
        выход """
        self.button_learn = ttk.Button(text = 'Учить', command = self.main_menu)
        self.button_settings = ttk.Button(text = 'Настройки')
        self.button_exit = ttk.Button(text = 'Выход', command = exit)
        """Button BACK Инициализация и местоположение"""
        self.button_back = ttk.Button(text = '<-')
        self.button_back.place(x = 0, y = 0)
        """Place Main Window"""
        self.button_learn.place(x = 265, y = 220)
        self.button_settings.place(x = 265, y = 250)
        self.button_exit.place(x = 265, y = 280)



    #def exit():
        #exit()






    def see():
        eng, rus = random.choice(list(dictionary_Eng_words.items()))
        l1 = Label(text = eng, font = ("roboto", 20), bg ='#282c34', foreground = '#61afef')
        l1.place(x = 100, y = 100)
        l2 = Label(text = rus, font = ("roboto", 20), bg ='#282c34', foreground = '#c49262')
        l2.place(x = 200, y = 200)




def main():
    root = Tk()
    root.geometry('600x600+690+240')
    root.title('Easy English')
    root['bg'] = "#21252b" #'#282c34'
    root.overrideredirect(1)
    #root.attributes('-zoomed', True)
    app = English()
    root.mainloop()


if __name__ == '__main__':
    main()































'''
words = []
wordsru = []

t = open('English_words2.txt', 'w', encoding = 'utf-8')

with open('transcr.txt', 'rt', encoding = 'utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        words.append(line)


for index in range(len(words)):
    column = words[index].split(']')
    t.write(column[1]+'\n')



t.close()

f.close()





















words = []
wordsru = []

t = open('English_words3.txt', 'w', encoding = 'utf-8')

with open('English_words.txt', 'rt', encoding = 'utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        words.append(line)

with open('English_words2.txt', 'rt', encoding = 'utf-8') as k:
    for line in k.readlines():
        line = line.strip()
        wordsru.append(line)

for index in range(len(words)):
    column = words[index].split('[')
    t.write(column[0] +' '+ wordsru[index]+'\n')


k.close()

t.close()

f.close()
'''
