import csv
import itertools
from tkinter import *
from tkinter.messagebox import *
from AirportAtlas import AirportAtlas
from AircraftCatalog import AircraftCatalog
from CurrencyCatalog import CurrencyCatalog
from CurrencyRatesCatalog import CurrencyRatesCatalog

# Create objects
atlas = AirportAtlas("input files/airport.csv")
aircraft = AircraftCatalog("input files/aircraft.csv")
currency = CurrencyCatalog("input files/countrycurrency.csv")
currencyRates = CurrencyRatesCatalog("input files/currencyrates.csv")


class MainGUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pack(expand = YES, fill =BOTH)
        self.master.title("Airline Fuel Manager - Bobga Nti (D16126842)")
        self.master.geometry("800x370")
        self.configure(bg='gray')

        # GUI Image header and Icon
        root.iconbitmap('input files/plane.ico')
        photo = PhotoImage(file='input files/plane2.gif')
        label = Label(image=photo, bg='gray')
        label.image = photo
        label.place(x=275, y=5)

        self.label1 = Label(self, text= "Enter Home Airport", bg='gray')
        self.label1.place(x=80, y=81)
        self.homeAirport = Entry(self, name = "homeAirport", bg='green')
        self.homeAirport.place(x=75, y=103)

        self.labelAircraft = Label(self, text = 'Other Airports (enter in any order)', bg='gray')
        self.labelAircraft.place(x=35, y=143)
        
        self.label2 = Label(self, text = 'Airport 2', bg='gray')
        self.label2.place(x=10, y=165)
        self.airport2 = Entry(self, name = 'airport2')
        self.airport2.place(x=75, y=165)

        self.label3 = Label(self, text = 'Airport 3', bg='gray')
        self.label3.place(x=10, y=195)
        self.airport3 = Entry(self, name = 'airport3')
        self.airport3.place(x=75, y=195)

        self.label4 = Label(self, text = 'Airport 4', bg='gray')
        self.label4.place(x=10, y=225)
        self.airport4 = Entry(self, name = 'airport4')
        self.airport4.place(x=75, y=225)

        self.label5 = Label(self, text = 'Airport 5', bg='gray')
        self.label5.place(x=10, y=255)
        self.airport5 = Entry(self, name = 'airport5')
        self.airport5.place(x=75, y=255)

        self.btn1 = Button(self, text='Find Cheapest Route', bg='#5B5453', command=self.onClicked)
        self.btn1.place(x=75, y=290)

        self.labelInfo = Label(self, text='OUTPUT SCREEN', bg='grey')
        self.labelInfo.place(x=500, y=81)

        info_board_frame = Frame(root)
        info_board_frame.place(x=360, y=103)

        scrollbar = Scrollbar(info_board_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.info_board = Text(info_board_frame, width=57, height=15, wrap=WORD, font=('arial',10), bg='#D0CBCA')
        self.info_board.pack()
        self.info_board.insert(END, 'INFORMATION BOARD')

        self.info_board.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.info_board.yview)


        self.labelList = Label(self, text='SELECT AIRCRAFT', bg='gray')
        self.labelList.place(x=230, y=113)
        
        listbox_frame = Frame(root)
        listbox_frame.place(x=230, y=135)

        scrollbar = Scrollbar(listbox_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
                               
        self.listbox = Listbox(listbox_frame, width=15, height=8, bg='#D0CBCA')
        self.listbox.insert(END, "A319")
        for item in ["A320", "A321", "A330", "737", "747", "757", "767", "777", "BAE146", "DC8", "F50", "MD11", "A400M", "C212", "V22"]:
            self.listbox.insert(END, item)
        self.listbox.pack()
        self.listbox.config(yscrollcommand =scrollbar.set)
        scrollbar.config(command=self.listbox.yview)      
        
    def onClicked(self):
        self.longestStage = 0
        self.planeRange = 0
        while 1:
            homeAirport = self.homeAirport.get().upper()
            isValidCode1 = atlas.checkCode_airportDict(homeAirport)
            if isValidCode1 == False:
                pass
            else:
                break;

        while 1:
            airport2 = self.airport2.get().upper()
            isValidCode2 = atlas.checkCode_airportDict(airport2)
            if isValidCode2 == False:
                pass
            else:
                break;

        while 1:
            airport3 = self.airport3.get().upper()
            isValidCode3 = atlas.checkCode_airportDict(airport3)
            if isValidCode3 == False:
                pass
            else:
                break;

        while 1:
            airport4 = self.airport4.get().upper()
            isValidCode4 = atlas.checkCode_airportDict(airport4)
            if isValidCode4 == False:
                pass
            else:
                break;

        while 1:
            airport5 = self.airport5.get().upper()
            isValidCode5 = atlas.checkCode_airportDict(airport5)
            if isValidCode5 == False:
                pass
            else:
                break;

        if isValidCode1 and isValidCode2 and isValidCode3 and isValidCode4 and isValidCode5:
            other_airtports_list = [airport2, airport3, airport4, airport5]

            permList = list(itertools.permutations(other_airtports_list))

            myDict = dict()
            myDict_cost = dict()
            myDict_trips = dict()

            """
            Each week, an aircraft begins flight at home airport and will return to the home airport to close the week's mission.
            permList produces 24 list of itinerary options (i). Each i list consists of 4 airports from the other airport list.
            So, home airport is inserted at the beginning and at the end of each i.
            This gives a total of 5 trips from home and back to home
            """
            for i in permList:
                i = list(i)
                i.insert(0, homeAirport)
                i.insert(len(i), homeAirport)

                """ This calculates the total distance and cost for each possible itinerary. """
                trip1 = atlas.get_dist_between_airports(i[0], i[1])
                trip1_cost = (currencyRates.get_currency_rates_details(currency.get_currency_details(atlas.getAirport(i[0]).country).currencyCode).currency_to_euro)*trip1

                trip2 = atlas.get_dist_between_airports(i[1], i[2])
                trip2_cost = (currencyRates.get_currency_rates_details(currency.get_currency_details(atlas.getAirport(i[1]).country).currencyCode).currency_to_euro)*trip2

                trip3 = atlas.get_dist_between_airports(i[2], i[3])
                trip3_cost = (currencyRates.get_currency_rates_details(currency.get_currency_details(atlas.getAirport(i[2]).country).currencyCode).currency_to_euro)*trip3

                trip4 = atlas.get_dist_between_airports(i[3], i[4])
                trip4_cost = (currencyRates.get_currency_rates_details(currency.get_currency_details(atlas.getAirport(i[3]).country).currencyCode).currency_to_euro)*trip4

                trip5 = atlas.get_dist_between_airports(i[4], i[0])
                trip5_cost = (currencyRates.get_currency_rates_details(currency.get_currency_details(atlas.getAirport(i[4]).country).currencyCode).currency_to_euro)*trip5

                stages = [trip1, trip2, trip3, trip4, trip5]
                total_distance_per_route = trip1 + trip2 + trip3 + trip4 + trip5
                total_cost_per_route = float("%.2f" % (trip1_cost + trip2_cost + trip3_cost + trip4_cost + trip5_cost))

                myDict[total_distance_per_route] = i
                myDict_cost[total_cost_per_route] = i
                myDict_trips[total_cost_per_route] = stages

            distances = list(myDict.keys())
            shortest_distance = min(distances)
            longest_distance = max(distances)
            shortest_route = myDict[shortest_distance]

            costs = list(myDict_cost.keys())
            smallest_cost = min(costs)
            largest_cost = max(costs)
            cheapest_route = myDict_cost[smallest_cost]

            longestStage = max(myDict_trips[smallest_cost])
            longestStage = ('%.2f' % longestStage)
            

            # Display output on screen
            self.info_board.delete(1.0, END)
            self.info_board.insert(1.0, 'Shortest Route: ')
            self.info_board.insert(3.0, shortest_route)
            self.info_board.insert(4.0, '%s %.2f %s' %('\nShortest Distance = ', shortest_distance, ' km'))

            self.info_board.insert(6.0, ('\n\nCheapest route: '))
            self.info_board.insert(7.0, cheapest_route)
            self.info_board.insert(10.0, '%s %.2f %s' % ('\nCost = ', smallest_cost, ' euros'))
            self.info_board.insert(11.0, '\n\nCheapest Route Stages: ')
            self.info_board.insert(12.0, myDict_trips[smallest_cost])
            self.info_board.insert(13.0, '\nLongest stage: ')
            self.info_board.insert(14.0, longestStage)

            plane = aircraft.get_aircraft_details(self.listbox.get(ACTIVE))
            self.planeRange = aircraft.get_aircraft_range(self.listbox.get(ACTIVE))
            self.longestStage = longestStage

            self.info_board.insert(18.0, '\n\nSelected Aircraft Details\n')
            self.info_board.insert(19.0, plane) 

            if self.planeRange > longestStage:
                self.info_board.insert(17.0, '\n\n%s %s %s %s %s %s %s' % ('The ', plane.manufacturer, ' ', plane.planeType, ' ',
                                                                           plane.planeCode, ' is ready to take-off'))
            else:     
                showinfo('Aircraf Range Error!', 'Select a bigger aircraft')                                  

def main():
    root = Tk()
    #root.iconbitmap('plane.ico')
    ap = MainGUI(root)
    root.mainloop()
if __name__ == "__main__":
        main()
