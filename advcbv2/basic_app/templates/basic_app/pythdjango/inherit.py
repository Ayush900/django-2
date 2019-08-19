class continents():
    def __init__(self):
        pass
    def north_zone(self):
        print("I am in the northern hemisphere")

    def south_zone(self):
        print("I am in the southern hemisphere")


class country(continents):
    def __init__(self):
        pass
asia=continents()
print("for Asia:")
asia.north_zone()
india=country()

print("for india:")
india.north_zone()

print("for antarctica:")
antarctica=country()
antarctica.south_zone()

