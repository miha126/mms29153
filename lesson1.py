print("lesson2")

class marker:
    color: str
    thikness: int
    isAvailbale: bool
    def __init__(self, color, thikness, isavailbale = True):
        self.color = color
        self.isAvailbale = isavailbale
        self.thikness = thikness

    def getInfo(self):
        print('parametry')
        if self.isAvailbale:
            print(f'\tcolor-{self.color} - thk-{self.thikness}')
        else:
            print('\ton zakonchilsya')


markerRed = marker('red', 2)
markerRed.getInfo()
markerRed.color = 'black'
markerRed.getInfo()