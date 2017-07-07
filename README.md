"Bobga-Airline-Fuel-Manager" 
The "Bobga Airline Fuel Manager" is a Software Development Project for my Object Oriented Software Development assignment for the Higher Diploma in Computing at the Dublin Institute of Technology

 Speciﬁcation. 
 
 Imagine you work for a small Irish software company that has won the tender to deliver a fuel management software solution to a large Irish Airline. 
The airline is entering the European air freight cargo business and wants a software tool to manage their fuel purchasing strategy. Each week, an aircraft will ﬂy up to six trips. The airplane will start and end in the same home airport each week and can optionally visit one other airport twice. The company has a number of diﬀerent aircrafts that have diﬀerent fuel capacities
and the cost of fuel varies from airport to airport. 
Given a list of 5 airports (including to the home airport) that a given plane needs to visit in a week, the most economic route must be found. 
• The distance between airports is calculated as the great circle distance between them 

• The cost of fuel is assumed to be 1 euro per 1 litre at Airports where the currency is Euros 

• The cost of fuel in airports where the local currency is not euros is assumed to be the exchange rate from the local currency to euro. e.g. if you travel from London to Dublin and the exchange rate is GBP1 = e1.4029 and you purchase 1000 litres of fuel, it will cost e1402.

Product Features. 
The program will take ﬁle inputs and give ﬁle outputs using CSV formats. 
It should also have a basic GUI to allow input of an individual itinerary. 
At a minimum, the program should work with a command line interface to interact with the user - this is not necessary if you have ﬁle and/or GUI interfaces.

Code style and eﬃciency. 
The program code should be created in a logical and eﬃcient manner. 
This includes: eﬃcient use of data structures (think for loops rather than repeated code), code re-use in functions and classes), breaking code up into logical chunks that keep code-blocks and ﬁles.
Reasonable length i.e. no 1000 line ﬁles!), eﬃcient storage and searching of data (think dictionaries).

Class Model Structure. 
Create classes that model the problem and abstract the main program from the underlying data structure. For example, the mainline code shouldn’t need to understand anything about parsing a CSV ﬁle or calculating great circle distance or currency rates calculation. 
This means it should be apparent that you have to create classes that model the problem and assigned useful attributes and methods to the classes. 
The solution should deﬁne classes for holding data that will be used in the problem, e.g. there will need to be a class for Currency and Airport? (HINT: Yes, there will!)
