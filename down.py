from tkinter import *
from tkinter import messagebox
import pytube
import requests
import youtube_dl
import os
from PIL import ImageTk, Image

def show_message():
    z=tekst.get()
    if(z[0:5]!="https"):
        messagebox.showinfo("Уведомление","Не правильная ссылка")
    else:
        URL=tekst.get()
        youtube = pytube.YouTube(URL)
        video = youtube.streams.first()
        video.download("./YOUTUBE_VIDEOS")
        messagebox.showinfo("Уведомление","Видео скачано")


def show_message2():
    z=tekst2.get()
    if(z[0:5]!="https"):
        messagebox.showinfo("Уведомление","Не правильная ссылка")
    else:
        ydl_opts = {
            'format':'best',
            'outtmpl':'./INSTAGRAM_VIDEOS/%(title)s.%(ext)s',
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([z])
        messagebox.showinfo("Уведомление","Файл скачан")


def show_message3():
    z=tekst3.get()
    if(z[0:5]!="https"):
        messagebox.showinfo("Уведомление","Не правильная ссылка")
    else:
        ydl_opts = {
            'format':'best',
            'outtmpl':'./FACEBOOK_VIDEOS/%(title)s.%(ext)s',
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([z])
        messagebox.showinfo("Уведомление","Файл скачан")



root=Tk()
root.call('wm', 'iconphoto', Tk._w, ImageTk.PhotoImage(Image.open('dnw2.ico')))
root.title("Видео загрузчик")
root.geometry("300x300")
root.resizable(width=False, height=False)
tekst = StringVar()
tekst2 = StringVar()
tekst3 = StringVar()
root["bg"]="black"


lbl=Label(text="Вставьте ссылку YouTube",background="red",font=12)
lbl.pack(side=TOP)


val = Entry(textvariable=tekst,width=50,bd =5)
val.config(state=NORMAL)
val.pack(side=TOP)


btn = Button(text="Скачать", command=show_message,
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
    font=5
    )
btn.pack(side=TOP)



lbl2=Label(text="Вставьте ссылку instagram",background="red",font=12)
lbl2.pack(side=TOP)


val2= Entry(textvariable=tekst2,width=50,bd =5)
val2.config(state=NORMAL)
val2.pack(side=TOP)


btn3 = Button(text="Скачать", command=show_message2,
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
    font=5
    )
btn3.pack(side=TOP)


lbl2=Label(text="Вставьте ссылку Facebook",background="red",font=12)
lbl2.pack(side=TOP)


val3= Entry(textvariable=tekst3,width=50,bd =5)
val3.config(state=NORMAL)
val3.pack(side=TOP)


btn4 = Button(text="Скачать", command=show_message3,
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
    font=5
    )
btn4.pack(side=TOP)


root.mainloop()