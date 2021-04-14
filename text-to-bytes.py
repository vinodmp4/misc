from tkinter import *
from tkinter.scrolledtext import ScrolledText

class GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("Insider")
        self.root.geometry('1165x675')
        self.root.minsize(width=1165,height=675)
        self.root.maxsize(width=1165,height=675)
        self.inputentry = ScrolledText(self.root,bg='black',fg='lime',height=20)
        self.byteentry = ScrolledText(self.root,bg='black',fg='lime',height=20)
        self.intentry = ScrolledText(self.root,bg='black',fg='cyan')
        self.inputentry.grid(row=0,column=0)
        self.byteentry.grid(row=0,column=1,sticky='e')
        self.intentry.grid(row=1,column=0,columnspan=2,sticky='news')
        self.byteentry.config(state=DISABLED)
        self.intentry.config(state=DISABLED)
        self.intentry.grid_columnconfigure(0, weight=1)
        self.inputentry.bind('<KeyRelease>',self.doalg)
    def doalg(self,*arg):
        self.intentry.config(state='normal')
        self.byteentry.config(state='normal')
        self.intentry.delete(1.0,END)
        self.byteentry.delete(1.0,END)
        self.intentry.insert(INSERT,self.texttoint(self.inputentry.get(1.0,END)))
        self.byteentry.insert(INSERT,self.texttobin(self.inputentry.get(1.0,END)))
        self.intentry.config(state='disabled')
        self.byteentry.config(state='disabled')

    def texttoint(self,text):
        num = 0
        OUTPUT = ""
        for x in text:
            if num<8:
                num+=1
                OUTPUT += str(ord(x))+', '
            else:
                num =0
                OUTPUT += "\n"+str(ord(x))+', '
        return OUTPUT

    def texttobin(self,text):
        num = 0
        OUTPUT = ""
        for x in text:
            txt = str(bin(ord(x))[2:])
            if len(txt)<8:txt=str('0'*(8-len(txt)))+txt
            if num<5:
                num+=1
                OUTPUT += " "+txt
            else:
                num = 0
                OUTPUT += " "+txt+"\n"
        return OUTPUT

application = Tk()
GUI(application)
if __name__ == "__main__":application.mainloop()
