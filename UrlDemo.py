import bitly_api
from tkinter import *
import tkinter.messagebox

def copy_text ():
    txt = E2.get()
    print (txt)
    root.clipboard_clear()
    root.clipboard_append (txt) # This is the process of copying to the clipboard
def getShortUrl():
    BITLY_ACCESS_TOKEN ="e2a4e09da6a8d0ca85277f17fefc5392c05becad"   
    b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN) 
    url = E1.get()
    if url.strip():
        #print("STR")
        response = b.shorten(url) 
        shorturl = response['url']
        print(shorturl)
        #print(response)
        E2.delete ( 0, last=tkinter.END )
        E2.insert (tkinter.END, shorturl)
    else : 
        #print("NOT")
        tkinter.messagebox.showinfo(title="Error", message="Enter the Url First",)
root = Tk()
root.bind('<Escape>', lambda e: root.quit()) 
L1 = Label(root, text="Enter Long Url")
L1.grid(row=0,column=0)
E1 = Entry(root, bd =5)
E1.grid(row=0,column=1)
E2 = Entry(root, text="Shorten Url")
#E2["state"]=DISABLED
E2.grid(row=1,column=0,padx=30,pady=10,columnspan=2)
B1 = Button(root, text="Shorten Url",command=getShortUrl)
B1.grid(row=2,column=0,padx=30,pady=10)
B2 = Button(root, text="Copy",command=copy_text)
B2.grid(row=2,column=1,padx=30,pady=10)
root.mainloop()
