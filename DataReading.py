f = open('./weather.dat', 'r')
minimum = None
minimumDay = None

class Linea:
    def __init__(self, Dy, MxT,   MnT):
        self.Dy = int(Dy)
        self.MxT = int(MxT)
        self.MnT = int(MnT)

    def getspread(self):
        return self.MxT-self.MnT

    def getday(self):
        return self.Dy

for line in f:
    tokens = line.split()
    if tokens:
        try:
            day = int(tokens[0])
            obj = Linea(tokens[0], tokens[1], tokens[2])
            if minimum is None or obj.getspread() < minimum:
                minimumDay = obj.getday()
                minimum = obj.getspread()
            print "Day: " + str(obj.getday()) + " Spread: " + str(obj.getspread())
        except ValueError as e:
            print("You didn't enter a number! Shame on you.")
print "\nThe Day " + str(minimumDay) + " is the day with Minimum Spread " + str(minimum)
f.close()