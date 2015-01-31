#attempting to add in solved animation
#does not delete inputs if time error
import tkinter as tk
from tkinter import *
import controller as ctrl
import webbrowser
import time
#if not complete puzzle, while loop will keep running
#trying to move getent from button
#trying url
#entry boxes
#comment example of insert to an entry box
#creates dictionary of entrys with zero for no entries
class gui:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root = tk.Tk()
        self.root2.title("Welcome")
        self.root.title("Sudoku Solver")
        self.entries = {}
        

        self.info = tk.Label(self.root2,text = "Welcome to the (Easy Level) Sudoku Solver!")
        self.info.grid(row=0,column=0)

        self.info2 = tk.Label(self.root2,text = "Instructions: Enter the given numbers in")
        self.info2.grid(row=1,column=0)

        self.info3 = tk.Label(self.root2,text = "their respective boxes.  Hit Solve and")
        self.info3.grid(row=2,column=0)

        self.info4 = tk.Label(self.root2,text = "wait for the puzzle to be solved!")
        self.info4.grid(row=3,column=0)

        self.info5 = tk.Label(self.root2,text = "You can close this window and begin.")
        self.info5.grid(row=4,column=0)

        self.button = tk.Button(self.root2,text="Close Window",command=lambda: self.root2.destroy())
        self.button.grid(row=6,column=0)



        self.a1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a1.grid(row=0,column=0)

        self.a2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a2.grid(row=0,column=1)

        self.a3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a3.grid(row=0,column=2,padx=(0,5))

        self.a4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a4.grid(row=0,column=3)

        self.a5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a5.grid(row=0,column=4)

        self.a6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a6.grid(row=0,column=5,padx=(0,5))

        self.a7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a7.grid(row=0,column=6)

        self.a8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a8.grid(row=0,column=7)

        self.a9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.a9.grid(row=0,column=8)

        self.b1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b1.grid(row=1,column=0)

        self.b2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b2.grid(row=1,column=1)

        self.b3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b3.grid(row=1,column=2,padx=(0,5))

        self.b4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b4.grid(row=1,column=3)

        self.b5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b5.grid(row=1,column=4)

        self.b6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b6.grid(row=1,column=5,padx=(0,5))

        self.b7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b7.grid(row=1,column=6)

        self.b8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b8.grid(row=1,column=7)

        self.b9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.b9.grid(row=1,column=8)

        self.c1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c1.grid(row=2,column=0,pady=(0,5))

        self.c2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c2.grid(row=2,column=1,pady=(0,5))

        self.c3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c3.grid(row=2,column=2,padx=(0,5),pady=(0,5))

        self.c4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c4.grid(row=2,column=3,pady=(0,5))

        self.c5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c5.grid(row=2,column=4,pady=(0,5))

        self.c6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c6.grid(row=2,column=5,padx=(0,5),pady=(0,5))

        self.c7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c7.grid(row=2,column=6,pady=(0,5))

        self.c8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c8.grid(row=2,column=7,pady=(0,5))

        self.c9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.c9.grid(row=2,column=8,pady=(0,5))

        self.d1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d1.grid(row=3,column=0)

        self.d2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d2.grid(row=3,column=1)

        self.d3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d3.grid(row=3,column=2,padx=(0,5))

        self.d4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d4.grid(row=3,column=3)

        self.d5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d5.grid(row=3,column=4)

        self.d6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d6.grid(row=3,column=5,padx=(0,5))

        self.d7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d7.grid(row=3,column=6)

        self.d8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d8.grid(row=3,column=7)

        self.d9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.d9.grid(row=3,column=8)

        self.e1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e1.grid(row=4,column=0)

        self.e2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e2.grid(row=4,column=1)

        self.e3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e3.grid(row=4,column=2,padx=(0,5))

        self.e4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e4.grid(row=4,column=3)

        self.e5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e5.grid(row=4,column=4)

        self.e6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e6.grid(row=4,column=5,padx=(0,5))

        self.e7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e7.grid(row=4,column=6)

        self.e8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e8.grid(row=4,column=7)

        self.e9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.e9.grid(row=4,column=8)

        self.f1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f1.grid(row=5,column=0,pady=(0,5))

        self.f2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f2.grid(row=5,column=1,pady=(0,5))

        self.f3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f3.grid(row=5,column=2,padx=(0,5),pady=(0,5))

        self.f4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f4.grid(row=5,column=3,pady=(0,5))

        self.f5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f5.grid(row=5,column=4,pady=(0,5))

        self.f6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f6.grid(row=5,column=5,padx=(0,5),pady=(0,5))

        self.f7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f7.grid(row=5,column=6,pady=(0,5))

        self.f8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f8.grid(row=5,column=7,pady=(0,5))

        self.f9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.f9.grid(row=5,column=8,pady=(0,5))

        self.g1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g1.grid(row=6,column=0)

        self.g2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g2.grid(row=6,column=1)

        self.g3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g3.grid(row=6,column=2,padx=(0,5))

        self.g4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g4.grid(row=6,column=3)

        self.g5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g5.grid(row=6,column=4)

        self.g6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g6.grid(row=6,column=5,padx=(0,5))

        self.g7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g7.grid(row=6,column=6)

        self.g8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g8.grid(row=6,column=7)

        self.g9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.g9.grid(row=6,column=8)

        self.h1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h1.grid(row=7,column=0)

        self.h2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h2.grid(row=7,column=1)

        self.h3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h3.grid(row=7,column=2,padx=(0,5))

        self.h4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h4.grid(row=7,column=3)

        self.h5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h5.grid(row=7,column=4)

        self.h6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h6.grid(row=7,column=5,padx=(0,5))

        self.h7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h7.grid(row=7,column=6)

        self.h8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h8.grid(row=7,column=7)

        self.h9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.h9.grid(row=7,column=8)

        self.i1 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i1.grid(row=8,column=0)

        self.i2 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i2.grid(row=8,column=1)
        
        self.i3 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i3.grid(row=8,column=2,padx=(0,5))

        self.i4 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i4.grid(row=8,column=3)

        self.i5 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i5.grid(row=8,column=4)

        self.i6 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i6.grid(row=8,column=5,padx=(0,5))

        self.i7 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i7.grid(row=8,column=6)

        self.i8 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i8.grid(row=8,column=7)

        self.i9 = tk.Entry(self.root,width=2,font=25,highlightbackground="black")
        self.i9.grid(row=8,column=8)

        self.button = tk.Button(self.root,text="Solve",command=lambda: (self.test()))
        self.button.grid(row=3,column=10)

        self.button3 = tk.Button(self.root,text="Clear Entries",command=lambda: (self.deleteEnts()))
        self.button3.grid(row=5,column=10)

        

    def getent(self):
        self.entries["a1"] = self.a1.get()
        self.entries["a2"] = self.a2.get()
        self.entries["a3"] = self.a3.get()
        self.entries["a4"] = self.a4.get()
        self.entries["a5"] = self.a5.get()
        self.entries["a6"] = self.a6.get()
        self.entries["a7"] = self.a7.get()
        self.entries["a8"] = self.a8.get()
        self.entries["a9"] = self.a9.get()
        self.entries["b1"] = self.b1.get()
        self.entries["b2"] = self.b2.get()
        self.entries["b3"] = self.b3.get()
        self.entries["b4"] = self.b4.get()
        self.entries["b5"] = self.b5.get()
        self.entries["b6"] = self.b6.get()
        self.entries["b7"] = self.b7.get()
        self.entries["b8"] = self.b8.get()
        self.entries["b9"] = self.b9.get()
        self.entries["c1"] = self.c1.get()
        self.entries["c2"] = self.c2.get()
        self.entries["c3"] = self.c3.get()
        self.entries["c4"] = self.c4.get()
        self.entries["c5"] = self.c5.get()
        self.entries["c6"] = self.c6.get()
        self.entries["c7"] = self.c7.get()
        self.entries["c8"] = self.c8.get()
        self.entries["c9"] = self.c9.get()
        self.entries["d1"] = self.d1.get()
        self.entries["d2"] = self.d2.get()
        self.entries["d3"] = self.d3.get()
        self.entries["d4"] = self.d4.get()
        self.entries["d5"] = self.d5.get()
        self.entries["d6"] = self.d6.get()
        self.entries["d7"] = self.d7.get()
        self.entries["d8"] = self.d8.get()
        self.entries["d9"] = self.d9.get()
        self.entries["e1"] = self.e1.get()
        self.entries["e2"] = self.e2.get()
        self.entries["e3"] = self.e3.get()
        self.entries["e4"] = self.e4.get()
        self.entries["e5"] = self.e5.get()
        self.entries["e6"] = self.e6.get()
        self.entries["e7"] = self.e7.get()
        self.entries["e8"] = self.e8.get()
        self.entries["e9"] = self.e9.get()
        self.entries["f1"] = self.f1.get()
        self.entries["f2"] = self.f2.get()
        self.entries["f3"] = self.f3.get()
        self.entries["f4"] = self.f4.get()
        self.entries["f5"] = self.f5.get()
        self.entries["f6"] = self.f6.get()
        self.entries["f7"] = self.f7.get()
        self.entries["f8"] = self.f8.get()
        self.entries["f9"] = self.f9.get()
        self.entries["g1"] = self.g1.get()
        self.entries["g2"] = self.g2.get()
        self.entries["g3"] = self.g3.get()
        self.entries["g4"] = self.g4.get()
        self.entries["g5"] = self.g5.get()
        self.entries["g6"] = self.g6.get()
        self.entries["g7"] = self.g7.get()
        self.entries["g8"] = self.g8.get()
        self.entries["g9"] = self.g9.get()
        self.entries["h1"] = self.h1.get()
        self.entries["h2"] = self.h2.get()
        self.entries["h3"] = self.h3.get()
        self.entries["h4"] = self.h4.get()
        self.entries["h5"] = self.h5.get()
        self.entries["h6"] = self.h6.get()
        self.entries["h7"] = self.h7.get()
        self.entries["h8"] = self.h8.get()
        self.entries["h9"] = self.h9.get()
        self.entries["i1"] = self.i1.get()
        self.entries["i2"] = self.i2.get()
        self.entries["i3"] = self.i3.get()
        self.entries["i4"] = self.i4.get()
        self.entries["i5"] = self.i5.get()
        self.entries["i6"] = self.i6.get()
        self.entries["i7"] = self.i7.get()
        self.entries["i8"] = self.i8.get()
        self.entries["i9"] = self.i9.get()
        for key in self.entries:
            if(self.entries[key] == ""):
                self.entries[key] = 0
        return self.entries


    def deleteEnts(self):
        if(2 > 1):
            if(2 > 1):
                if(2 > 1):
                    if(2 > 1):
                        self.a1.delete(0,tk.END)
                        self.a2.delete(0,tk.END)
                        self.a3.delete(0,tk.END)
                        self.a4.delete(0,tk.END)
                        self.a5.delete(0,tk.END)
                        self.a6.delete(0,tk.END)
                        self.a7.delete(0,tk.END)
                        self.a8.delete(0,tk.END)
                        self.a9.delete(0,tk.END)
                        self.b1.delete(0,tk.END)
                        self.b2.delete(0,tk.END)
                        self.b3.delete(0,tk.END)
                        self.b4.delete(0,tk.END)
                        self.b5.delete(0,tk.END)
                        self.b6.delete(0,tk.END)
                        self.b7.delete(0,tk.END)
                        self.b8.delete(0,tk.END)
                        self.b9.delete(0,tk.END)
                        self.c1.delete(0,tk.END)
                        self.c2.delete(0,tk.END)
                        self.c3.delete(0,tk.END)
                        self.c4.delete(0,tk.END)
                        self.c5.delete(0,tk.END)
                        self.c6.delete(0,tk.END)
                        self.c7.delete(0,tk.END)
                        self.c8.delete(0,tk.END)
                        self.c9.delete(0,tk.END)
                        self.d1.delete(0,tk.END)
                        self.d2.delete(0,tk.END)
                        self.d3.delete(0,tk.END)
                        self.d4.delete(0,tk.END)
                        self.d5.delete(0,tk.END)
                        self.d6.delete(0,tk.END)
                        self.d7.delete(0,tk.END)
                        self.d8.delete(0,tk.END)
                        self.d9.delete(0,tk.END)
                        self.e1.delete(0,tk.END)
                        self.e2.delete(0,tk.END)
                        self.e3.delete(0,tk.END)
                        self.e4.delete(0,tk.END)
                        self.e5.delete(0,tk.END)
                        self.e6.delete(0,tk.END)
                        self.e7.delete(0,tk.END)
                        self.e8.delete(0,tk.END)
                        self.e9.delete(0,tk.END)
                        self.f1.delete(0,tk.END)
                        self.f2.delete(0,tk.END)
                        self.f3.delete(0,tk.END)
                        self.f4.delete(0,tk.END)
                        self.f5.delete(0,tk.END)
                        self.f6.delete(0,tk.END)
                        self.f7.delete(0,tk.END)
                        self.f8.delete(0,tk.END)
                        self.f9.delete(0,tk.END)
                        self.g1.delete(0,tk.END)
                        self.g2.delete(0,tk.END)
                        self.g3.delete(0,tk.END)
                        self.g4.delete(0,tk.END)
                        self.g5.delete(0,tk.END)
                        self.g6.delete(0,tk.END)
                        self.g7.delete(0,tk.END)
                        self.g8.delete(0,tk.END)
                        self.g9.delete(0,tk.END)
                        self.h1.delete(0,tk.END)
                        self.h2.delete(0,tk.END)
                        self.h3.delete(0,tk.END)
                        self.h4.delete(0,tk.END)
                        self.h5.delete(0,tk.END)
                        self.h6.delete(0,tk.END)
                        self.h7.delete(0,tk.END)
                        self.h8.delete(0,tk.END)
                        self.h9.delete(0,tk.END)
                        self.i1.delete(0,tk.END)
                        self.i2.delete(0,tk.END)
                        self.i3.delete(0,tk.END)
                        self.i4.delete(0,tk.END)
                        self.i5.delete(0,tk.END)
                        self.i6.delete(0,tk.END)
                        self.i7.delete(0,tk.END)
                        self.i8.delete(0,tk.END)
                        self.i9.delete(0,tk.END)
                        
    def checkError(self):
        for (key, value) in self.entries.items():
            if(str(value).isdigit() == False or len(str(value)) > 1):
                self.root3 = tk.Tk()
                self.root3.title("Input Error")
                #errMessage = "Input error in box: " + str(key)
                errMessage = "There appears to be an error with your inputs."
                self.error1 = tk.Label(self.root3, text = errMessage)
                self.error1.grid(row=0, column=0)
                self.error2 = tk.Label(self.root3, text = "Please make sure to only input numbers from 1 to 9.")
                self.error2.grid(row=1, column=0)
                self.errButton = tk.Button(self.root3, text = "Close", command=lambda:self.root3.destroy())
                self.errButton.grid(row=2, column=1)
                return False
        return True
    
    def test(self):
        cooridinates = ["a1","a2","a3","a4","a5","a6","a7","a8","a9",
                        "b1","b2","b3","b4","b5","b6","b7","b8","b9",
                        "c1","c2","c3","c4","c5","c6","c7","c8","c9",
                        "d1","d2","d3","d4","d5","d6","d7","d8","d9",
                        "e1","e2","e3","e4","e5","e6","e7","e8","e9",                        
                        "f1","f2","f3","f4","f5","f6","f7","f8","f9",
                        "g1","g2","g3","g4","g5","g6","g7","g8","g9",
                        "h1", "h2","h3","h4","h5","h6","h7","h8","h9",                        
                        "i1","i2","i3","i4","i5","i6","i7","i8","i9"]
        timeout = time.time() + 10
        while(cooridinates):
            self.getent()
            if(time.time() > timeout):
                self.root4 = tk.Tk()
                self.root4.title("Time Error")
                errMessage = "The given time has elapsed."
                self.error1 = tk.Label(self.root4, text = errMessage)
                self.error1.grid(row=0, column=0)
                self.error2 = tk.Label(self.root4, text = "Re-enter your inputs.\n Please make sure you have entered inputs of a solvable puzzle.\n If there are no errors with your inputs,\n enter an easier puzzle to solve.")
                self.error2.grid(row=1, column=0)
                self.errButton = tk.Button(self.root4, text = "Close", command=lambda:self.root4.destroy())
                self.errButton.grid(row=2, column=0)
                break
            if(self.checkError() == False):
                break
            for item in cooridinates:
                if(self.entries[item] == 0):
                    self.ctrl = ctrl.controller(item,self.entries)
                    if(self.ctrl.getCommon()[0] != 0 and len(self.ctrl.getCommon()) == 1):
                        if(item == "a1"):
                            self.a1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a2"):
                            self.a2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a3"):
                            self.a3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a4"):
                            self.a4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a5"):
                            self.a5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a6"):
                            self.a6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a7"):
                            self.a7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a8"):
                            self.a8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "a9"):
                            self.a9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b1"):
                            self.b1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b2"):
                            self.b2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b3"):
                            self.b3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b4"):
                            self.b4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b5"):
                            self.b5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b6"):
                            self.b6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b7"):
                            self.b7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b8"):
                            self.b8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "b9"):
                            self.b9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c1"):
                            self.c1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c2"):
                            self.c2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c3"):
                            self.c3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c4"):
                            self.c4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c5"):
                            self.c5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c6"):
                            self.c6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c7"):
                            self.c7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c8"):
                            self.c8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "c9"):
                            self.c9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d1"):
                            self.d1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d2"):
                            self.d2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d3"):
                            self.d3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d4"):
                            self.d4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d5"):
                            self.d5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d6"):
                            self.d6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d7"):
                            self.d7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d8"):
                            self.d8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "d9"):
                            self.d9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e1"):
                            self.e1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e2"):
                            self.e2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e3"):
                            self.e3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e4"):
                            self.e4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e5"):
                            self.e5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e6"):
                            self.e6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e7"):
                            self.e7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e8"):
                            self.e8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "e9"):
                            self.e9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f1"):
                            self.f1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f2"):
                            self.f2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f3"):
                            self.f3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f4"):
                            self.f4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f5"):
                            self.f5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f6"):
                            self.f6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f7"):
                            self.f7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f8"):
                            self.f8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "f9"):
                            self.f9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g1"):
                            self.g1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g2"):
                            self.g2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g3"):
                            self.g3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g4"):
                            self.g4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g5"):
                            self.g5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g6"):
                            self.g6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g7"):
                            self.g7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g8"):
                            self.g8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "g9"):
                            self.g9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h1"):
                            self.h1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h2"):
                            self.h2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h3"):
                            self.h3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h4"):
                            self.h4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h5"):
                            self.h5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h6"):
                            self.h6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h7"):
                            self.h7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h8"):
                            self.h8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "h9"):
                            self.h9.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i1"):
                            self.i1.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i2"):
                            self.i2.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i3"):
                            self.i3.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i4"):
                            self.i4.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i5"):
                            self.i5.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i6"):
                            self.i6.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i7"):
                            self.i7.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i8"):
                            self.i8.insert(0,self.ctrl.getCommon()[0])
                        if(item == "i9"):
                            self.i9.insert(0,self.ctrl.getCommon()[0])
                        self.entries[item] == self.ctrl.getCommon()[0]
                        cooridinates.remove(item)
                else:
                    cooridinates.remove(item)
        boxes = 0
        for key in self.entries:
            if(self.entries[key] == 0 or self.entries[key] == "0"):
                boxes = boxes + 1
        if(boxes == 0):
            self.root5 = tk.Tk()
            self.root5.title("Why?")
            self.message = tk.Label(self.root5, text = "What are you doing?\n Why would you enter something in every box?\n Do you even understand what this program is?\n")
            self.message.grid(row=0, column=0)
        if(len(cooridinates) == 0 and boxes != 0):
            var = []
            window = Tk()
            canvas = Canvas(window, width = 370, height = 270)
            window.title("Solved")
            canvas.pack()
            x0 = 10
            y0 = 50
            x1 = 60
            y1 = 100
            a0 = 10
            b0 = 50
            a1 = 60
            b1 = 100
            c0 = 10
            d0 = 50
            c1 = 60
            d1 = 100

            i = 0
            deltax = 2
            deltay = 3
            deltaa = 3
            deltab = 2
            deltac = 2
            deltad = 3

            w1 = canvas.create_text(x0,y0,text ="SOLVED!",fill="red", tag='red')
            w2 = canvas.create_text(a0,b0,text ="SOLVED!",fill="blue", tag='blue')
            w3 = canvas.create_text(c0,d0,text ="SOLVED!",fill="green", tag='green')
            try:
                while(True):
                    canvas.move('red', deltax, deltay)
                    canvas.move('blue', deltaa, deltab)
                    canvas.move('green', deltac, deltad)
                    canvas.after(20)
                    canvas.update()
                    if x1 >= 380:
                        deltax = -2
                    if x0 < 50:
                        deltax = 2
                    if y1 > 280:
                        deltay = -3
                    if y0 < 20:
                        deltay = 2
                    if a1 >= 280:
                        deltaa = -3
                    if a0 < 50:
                        deltaa = 3
                    if b1 > 280:
                        deltab = -2
                    if b0 < 20:
                        deltab = 3
                    if c1 >= 380:
                        deltac = -3
                    if c0 < 50:
                        deltac = 3
                    if d1 > 280:
                        deltad = -2
                    if d0 < 20:
                        deltad = 3
                    x0 += deltax
                    x1 += deltax
                    y0 += deltay
                    y1 += deltay
                    a0 += deltaa
                    a1 += deltaa
                    b0 += deltab
                    b1 += deltab
                    c0 += deltac
                    c1 += deltac
                    d0 += deltad
                    d1 += deltad
            except:
                canvas.mainloop()
                window.mainloop()
                
    def MainLoop(self):
        self.root.mainloop()
