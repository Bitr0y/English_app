from tkinter import *
import tkinter.ttk as ttk
import random

dictionary_Eng_words = {}
with open("English_words3.txt", encoding = 'utf-8') as file:
    for line in file:
        key, *value = line.split()
        dictionary_Eng_words[key] = value



class English:
    """Menu"""
    def main_menu(self):
        """Place Main Window"""
        self.button_learn.place(x = 205, y = 175)
        self.button_settings.place(x = 205, y = 255)
        self.button_exit.place(x = 205, y = 335)
        """Remove other widgets"""
        self.button_new_words.place_forget()
        self.button_repeat.place_forget()
        self.button_back.place_forget()
        self.buttton_color_grey.place_forget()
        self.buttton_color_white.place_forget()
        self.l1.place_forget()
        self.l2.place_forget()
        self.button_next.place_forget()
    """Setting"""
    def grey_theme(self):
        self.root['bg'] = "#21252b"

    def white_theme(self):
        self.root['bg'] = "white"
    """Learn"""
    def new_words(self):
        pass

    def repeate_words(self):
        pass

    def learn(self):
        """Show Learn Window"""
        self.button_back.configure(text = '←', width = 4)
        self.button_new_words.place(x = 205, y = 220)
        self.button_repeat.place(x = 205, y = 305)
        self.button_back.place(x = 0, y = 0)
        """Remove other widgets"""
        self.button_learn.place_forget()
        self.button_settings.place_forget()
        self.button_exit.place_forget()

    def settings(self):
        """Show Setting Window"""
        self.button_back.place(x = 0, y = 0)
        self.buttton_color_grey.place(x = 100, y = 50)
        self.buttton_color_white.place(x = 150, y = 50)
        """Remove other widgets"""
        self.button_learn.place_forget()
        self.button_settings.place_forget()
        self.button_exit.place_forget()



    def __init__(self, root):
        """Initialization variables"""
        self.var = IntVar()
        self.var.set(0)
        self.root = root
        """Main window Initialization
        учить(новые слова / повторение)
        настройки
        выход """
        self.button_learn = Button(text = 'Изучение', font = ("roboto", 14), command = self.learn, height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        self.button_settings = Button(text = 'Настройки', font = ("roboto", 14), command = self.settings, height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        self.button_exit = Button(text = 'Выход', font = ("roboto", 14), command = exit, height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        """Button BACK Initialization"""
        self.button_back = Button(text = '←', font = ("roboto", 14), command = self.main_menu, height = 2, width = 4, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        """Initialization Learn Window"""
        """new words"""
        self.button_new_words = Button(text = 'Новые слова', font = ("roboto", 14), command = self.see, height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        self.l1 = Label( width = 35, height = 3, font = ("roboto", 20), bg ='#21252b', foreground = '#61afef', justify = CENTER)
        self.l2 = Label( width = 35, height = 3, font = ("roboto", 20), bg ='#21252b', foreground = '#c49262')
        self.button_next = Button(text = "Дальше", font = ("roboto", 14), command = self.see, height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        self.button_repeat = Button(text = 'Повторение', font = ("roboto", 14), height = 2, width = 15, bg = '#202020', foreground = '#98c379', activebackground = '#202020')
        """Initialization Setting Window"""
        self.buttton_color_grey = Radiobutton(text = 'grey', width = 3, height = 2, bg = '#21252b', activebackground = 'red', variable = self.var, value = 0, indicatoron=0, command = self.grey_theme)
        self.buttton_color_white = Radiobutton(text = 'white', width = 3, height = 2, bg = 'white', variable = self.var, value = 1, indicatoron=0, command = self.white_theme)

        """Show Main Window"""
        self.main_menu()


    def see(self):
        """Initialization"""
        eng, rus = random.choice(list(dictionary_Eng_words.items()))
        self.l1['text'] = eng
        self.l2['text'] = rus
        self.l1.place(x = 0, y = 100)
        self.l2.place(x = 0, y = 200)
        self.button_back.configure(text = 'В меню', width = 15)
        self.button_back.place(x = 90, y = 520)
        self.button_next.place(x = 280, y = 520)
        """Remove other widgets"""
        self.button_new_words.place_forget()
        self.button_repeat.place_forget()



def main():
    root = Tk()
    root.geometry('560x600+710+240')
    root.title('Easy English')
    root['bg'] = "#21252b" #'#282c34'
    root.overrideredirect(1)
    #root.attributes('-zoomed', True)
    app = English(root)
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
