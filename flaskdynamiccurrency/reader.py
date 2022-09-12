import json

path_ = "country-by-geo-cordinations.json"


class CordReader:

    def __init__(self, x=None, y=None, path=None):
        if x and y and path:
            self.init_app(x, y, path)

    def init_app(self, x, y, path):
        self.x = int(x)  # longitude
        self.y = int(y)  # latitude

        # file operation
        with open(path, 'r') as f:
            self.data = json.load(f)  # json data containing the coordinates.

    # returns a list of the coordinates that would be compared with the input.
    @staticmethod
    def lang_long(x, y):
        mylist = []

        if x > y:
            for i in range(y, x):
                mylist.append(i)

        elif x < y:
            for i in range(x, y):
                mylist.append(i)

        else:
            return [x]
        return mylist

    # the actual logic of comparison takes place.
    def logic(self):
        latitude = self.lang_long
        longitude = self.lang_long
        for i in range(len(self.data)):

            north = int(float(self.data[i]['north']))
            south = int(float(self.data[i]['south']))
            east = int(float(self.data[i]['east']))
            west = int(float(self.data[i]['west']))

            if int(self.x) in latitude(east, west) and int(self.y) in longitude(north, south):
                print(self.data[i]['country'])
                # print('latititude', self.x)
                # print('longitude', self.y)
                return self.data[i]['country'].upper()


def map_iso(path, country_name=None):
    # file operation
    with open(path, 'r') as f:
        data = json.load(f)  # json data containing the coordinates.

    for i in range(len(data)):
        if data[i]['Entity'] == country_name:
            return data[i]['Code']

