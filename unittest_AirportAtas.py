#unittest Airport Atlas

import unittest
from AirportAtlas import AirportAtlas 


class AirportAtlasTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.known_values = ('DUB', 'DUB', 0)   #####Coordinates of Dublin.
        self.testAtlas = AirportAtlas("input files/airport.csv")

        
    def test_getDistBetween_known_values(self):
        code1 = self.known_values[0]
        code2 = self.known_values[1]
            
        result = self.testAtlas.get_dist_between_airports(code1, code2)
        self.assertEqual(0, result)  ######Distance fro Dublin to Dublin should be zero

        code3 = 'JFK'
        code4 = 'AAL'

        result = self.testAtlas.get_dist_between_airports(code3, code4)
        self.assertEqual(5966, result)

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
