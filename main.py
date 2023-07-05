import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("URL Shortener")
root.geometry("500x250")

url = input('Enter the URL: ')

def func(url):
    shortedURL = pyshorteners.Shortener()
    entry2.insert(0, shortedURL.tinyurl.short(url))
    # print(entry2.insert(0, shortedURL.tinyurl.short(url)))

# func(url)

label1 = tkinter.Label(root, text="Enter the URL to be shortened")
entry1 = tkinter.Entry(root)
label2 = tkinter.Label(root, text="Shortened URL")
entry2 = tkinter.Entry(root)
button = tkinter.Button(root, text="Shorten URL", command=func(entry1.get()))

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()

root.mainloop()