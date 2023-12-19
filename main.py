from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube


def browse():
    download_dir = filedialog.askdirectory(initialdir="YOUR DOWNLOAD PATH")
    download_path.set(download_dir)


def highest_quality():
    get = e1.get()
    get2 = lbl3.get()
    if get2 == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    if get == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    else:
        down = YouTube(get)
        vid = down.streams.get_highest_resolution()
        vid.download(get2)
        messagebox.showinfo("Download Info", "Downloaded Successfully")


def lowest_quality():
    get = e1.get()
    get2 = lbl3.get()
    if get2 == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    if get == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    else:
        down = YouTube(get)
        vid = down.streams.get_lowest_resolution()
        vid.download(get2)
        messagebox.showinfo("Download Info", "Downloaded Successfully")


def audio_only():
    get = e1.get()
    get2 = lbl3.get()
    if get2 == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    if get == "":
        messagebox.showerror("Error", "Input Box Can't Be Empty")
    else:
        down = YouTube(get)
        vid = down.streams.get_audio_only()
        vid.download(get2)
        messagebox.showinfo("Download Info", "Downloaded Successfully")


root = Tk()
root.geometry("800x370")
root.resizable(False, False)
root.title("YouTube Video Downloader")

ttl1 = Label(root, text="YouTube Video Downloader", font=("Helvetica", 25)).place(
    x=200, y=5
)
lbl1 = Label(root, text="Enter URL: ", font=("Helvetica", 18))
lbl1.place(x=200, y=100)
e1 = Entry(root, width=47)
e1.place(x=330, y=107)

btn1 = Button(
    root,
    text="Download(Highest Quality)",
    font=("Helvetica", 10),
    command=highest_quality,
)
btn1.place(x=250, y=150)
btn2 = Button(
    root,
    text="Download(Lowest Quality)",
    font=("Helvetica", 10),
    command=lowest_quality,
)
btn2.place(x=430, y=150)
btn3 = Button(
    root, text="Download(Audio Only)", font=("Helvetica", 10), command=audio_only
)
btn3.place(x=350, y=190)

lbl2 = Label(root, text="Select Download Path", font=("Helvetica", 20))
lbl2.place(x=260, y=230)

btn4 = Button(root, text="Select", font=("Helvetica", 10), command=browse)
btn4.place(x=370, y=280)

download_path = StringVar()
lbl3 = Entry(root, textvariable=download_path, font=("Helvetica", 12))
lbl3.place(x=300, y=320)

root.mainloop()
