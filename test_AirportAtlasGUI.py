from tkinter import *
from tkinter.messagebox import *
from AirportAtlas import AirportAtlas

class DistanceCalculator(Frame):
    def __init__(self):
        
        Frame.__init__(self) # initialising Frame object
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Calculate Distance")
        self.master.geometry("325x200")

        self.label1 = Label(self, text= "Airport 1")
        self.label1.place(x=10, y=25)
        self.text1 = Entry(self, name = "text1")
        self.text1.place(x=75, y=25)

        self.label2 = Label(self, text = 'Airport 2')
        self.label2.place(x=10, y=75)
        self.text2 = Entry(self, name = 'text2')
        self.text2.place(x=75, y=75)

        self.button1 = Button(self, text = 'Calculate', command=self.onClicked)
        self.button1.place(x=75, y=100)

    def onClicked(self):
        ap = AirportAtlas("input files/airport.csv")
        while 1:
            airport1 = self.text1.get().upper()
            isValidCode1 = ap.checkCode_airportDict(airport1)
            if isValidCode1 == False:
                pass
            else:
                break;
            
        while 1:
            airport2 = self.text2.get().upper()
            isValidCode2 = ap.checkCode_airportDict(airport2)
            if isValidCode2 == False:
                pass
            else:
                break;
            
        if isValidCode1 and isValidCode2:
            distance = ap.get_dist_between_airports(airport1, airport2)
            showinfo("The distance is ", distance)

def main():
    DistanceCalculator().mainloop()
if __name__ == "__main__":
        main()
