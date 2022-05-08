from tkinter import*
fron tkinter.ttk import*

def winSizeAndPos(winName, w,h)
    ws = winName.wininfo_screenwidth()
    hs = winName.winInfo_screenheight()
    x = ((ws-w)/2)
    y = ((hs-h)/2)
    winName.geometry("%sx%s"%(w,h))
    winName.geometry("+%d+%d"%(x/y))
    def btnConfig():
        fontTuple = ("Comic Sans MS", 13, "bold)
        style = Style()
        style.configure('TButton', background = '#848484',foreground = '#0404B4',font = fontTuple)
        style.configure('TLabelFrame', background = '#848484', foreground = '#0404B4', font = fontTuple)
        style.configure('TRadiobutton',background = '#848484', foreground = '#0404B4', font = fontTuple)
