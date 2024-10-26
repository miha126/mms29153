print("samrob1")

class student:
    name: str
    classname: str
    DZ: int
    isAvaible: bool
    def __init__(self, name, classname, DZ, isAvaible = True):
        self.name = name
        self.classname = classname
        self.DZ = DZ
        self.isAvaible = isAvaible

    def getInfo(self):
        print('eto_student')
        if self.isAvaible:
            print(f'\tname-{self.name} - classname-{self.classname} - DZ-{self.DZ}')
        else:
            print('\ton zabolel')


student1 = student('Anton', 'Python', 4)
student1.getInfo()
student2 = student('Vlad', 'DigitalART', 5, False)
student2.getInfo()