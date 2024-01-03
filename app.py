import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from ttkthemes import themed_tk as tk
from tkinter import *
from tkinter import filedialog


root = tk.ThemedTk()
root.get_themes()
root.title('Music Player')# Returns a list of all themes that can be set
root.set_theme("radiance")


root.minsize(500,500)
root.iconbitmap(r'D:\\Media\\Downloads\\songs')
root.resizable(0, 0)

listbox=Listbox(root,selectmode=ACTIVE,width=100,height=20,bg="black",fg="white")
listbox.pack(fill=X)

sb =Scrollbar(root,orient = 'vertical')
sb.configure(command = listbox.yview)
sb.pack(side="right", fill="y")

listbox.configure(yscrollcommand=sb.set)

listofsongs=[]
realnames = []

v =StringVar()
songlabel =Label(root,textvariable=v,width=80)
index=0
count=0
ctr=0


def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])

def pausesong(event):
    global ctr
    ctr += 1
    if (ctr%2!=0):
        pygame.mixer.music.pause()
        statusbar['text'] = "Music Pause"
    if(ctr%2==0):
        try:
            pygame.mixer.music.unpause()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[item])
        except Exception as e:
            print(e)
            pass



def playsong(event):
    pygame.mixer.music.play()


def nextsong(event):
    global index
    index += 1
    if (index < count):
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])
        audio = MP3(listofsongs[index])
        x = audio.info.length
        mins, secs = divmod(x, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat2 = '{:02d}:{:02d}'.format(mins, secs)
        length['text'] = "Total Length" + ' - ' + timeformat2
        listbox.itemconfig(index, bg='orange',fg = 'black')
        import threading
        global t2
    else:
        index = 0
        pygame.mixer.music.load(listofsongs[index])
        statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])
        pygame.mixer.music.play()
        listbox.itemconfig(index, bg='orange',fg = 'black')
        # listbox.selection_set(first=index)
    try:
      updatelabel()
    except NameError:
        print("")

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[index])

    audio = MP3(listofsongs[index])
    x = audio.info.length
    mins, secs = divmod(x, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
    length['text'] = "Total Length" + ' - ' + timeformat1
    pygame.mixer.music.play()
    listbox.itemconfig(index, bg='orange',fg = 'black')
    try:
        updatelabel()
    except NameError:
        print("")

directory = filedialog.askdirectory() ##Enter your music Directory path
os.chdir(directory)
root.title(directory)
for  files in os.listdir(directory):
    try:
         if files.endswith(".mp3"):

              realdir = os.path.realpath(files)
              audio = ID3(realdir)
              realnames.append(audio['TIT2'].text[0])
              listofsongs.append(files)
    except:
         print(files+" is not a song")

listbox.delete(0, END)
realnames.reverse()
for items in realnames:
            listbox.insert(0, items)
for i in listofsongs:
            count = count + 1
pygame.mixer.init()
pygame.mixer.music.load(listofsongs[index])
pygame.mixer.music.play()
listbox.itemconfig(index, bg='orange',fg = 'black')

from mutagen.mp3 import MP3
audio = MP3(listofsongs[index])
x = audio.info.length
print(x)
mins, secs = divmod(x, 60)
mins = round(mins)
secs = round(secs)
timeformat = '{:02d}:{:02d}'.format(mins, secs)

def del_music(self):
    items = map(int, listbox.curselection())
    for item in items:
        listbox.delete(item)
        listofsongs.pop(item)
        print(item)
        print(listofsongs)

def play_music(self):
    items = map(int, listbox.curselection())
    global item
    for item in items:
        item = int(item)
        pygame.mixer.music.load(listofsongs[item])
        statusbar['text'] = "Playing music" + ' - ' + os.path.basename(listofsongs[item])
        audio = MP3(listofsongs[item])
        x = audio.info.length
        mins, secs = divmod(x, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat1 = '{:02d}:{:02d}'.format(mins, secs)
        length['text'] = "Total Length" + ' - ' + timeformat1
        pygame.mixer.music.play()
        listbox.itemconfig(item, bg='orange',fg = 'black')


def add_music(self):
    import tkinter as tk
    from tkinter import filedialog
    rt = tk.Tk()
    rt.withdraw()
    global  filename
    filename = filedialog.askopenfilename()
    print(filename)
    listofsongs.insert(index,filename)
    print(listofsongs)
    listbox.insert(index,filename)
    rt.mainloop()


def show_value(val):
    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)

length = Label(root, text="Welcome to Melody", font='Times 13 bold')
length.pack(side=BOTTOM, fill=X)
length.place(x =10,y=445 )
length['text'] = "Total Length" + ' - ' + timeformat


le = Label(root, text="Welcome to Melody", font='Times 13 bold')
le.pack(side=BOTTOM, fill=X)
le.place(x =270,y=445 )

def mute(self):
    vol.set(0)
    if vol.set(0):
        vol.set(10)


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                pygame.mixer.music.stop()
                root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

vol = Scale(root,from_ = 0,to = 100,orient = HORIZONTAL ,relief =SUNKEN,resolution = 10,command = show_value,activebackground='cyan')
vol.set(80)
pygame.mixer.music.set_volume(0.8)
vol.place(x=910, y = 436)

volume = Label(root, text="Volume", font='Times 13 bold')
volume.place(x=840, y = 450)

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=W,background='black',fg='white',font='Times 13 bold italic')
statusbar.pack(side=BOTTOM, fill=X)

statusbar['text'] = "Playing Music" + ' - ' + os.path.basename(listofsongs[index])

framemiddle =Frame(root,width=250,height=30)
framemiddle.pack()


framedown =Frame(root,width=400,height=300)
framedown.pack()

previousbutton = Button(framedown,text="◄◄",bg='black',fg='white',activebackground = "Red",width=15  ,height=2)
previousbutton.pack(side=LEFT)

playbutton = Button(framedown,text="►",activebackground = "Red",width=15  ,height=2)
playbutton.pack(side=LEFT)

mutebtn = Button(framedown,text="Play",activebackground = "Red",width=15  ,height=2)
mutebtn.pack(side=LEFT)

pausebutton = Button(framedown,bg='black',fg='white',text="►/║║",activebackground = "white",width=15  ,height=2)
pausebutton.pack(side=LEFT)

del_button = Button(framedown,text="Del Song",activebackground = "Red",width=15  ,height=2)
del_button.pack(side=LEFT)

add_button = Button(framedown,text="Add Song",activebackground = "Red",width=15  ,height=2)
add_button.pack(side=LEFT)

nextbutton = Button(framedown,text="►►",bg='black',fg='white',activebackground = "Red",width=15  ,height=2)
nextbutton.pack(side=LEFT)


playbutton.bind("<Button-1>",playsong)
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
mutebtn.bind("<Button-1>",play_music)
pausebutton.bind("<Button-1>",pausesong)
del_button.bind("<Button-1>",del_music)
add_button.bind("<Button-1>",add_music)
root.mainloop()
