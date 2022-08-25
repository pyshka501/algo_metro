from math import *

# переменные
k_important_building = 1.12

class district:
    def __init__(self):
        self.live_people = int(input("live_area: "))//35
        self.office_people = int(input("office_area: "))//10
        self.all_people = self.live_people + self.office_people
        self.all_auto = self.all_people/1.2

        self.all_metro = self.all_people - int(self.all_auto)
    def getter(self):
        return [self.all_auto, self.all_metro]
        # all auto, all metro


# office, hotel, city house, жк

class Building:
    def __init__(self):
        self.type = None
        self.data = None
        self.metro_people = None
        self.auto = None
        self.distance = None
        self.work_place = None
        self.area = None
        self.important_buildings = None


    def setter(self, k):
        self.area = int(input("area: "))
        self.number_of_floors = int(input("number of floors: "))
        self.distance = int(input("distance: "))
        self.work_place = (self.area * self.number_of_floors) // k
        self.auto = round(self.work_place / 1.2)            # auto
        self.metro_people = self.work_place - self.auto         #metro people
        self.important_buildings = int(input("important_buildings: "))
        self.k = k*self.important_buildings


    def getter(self):
        self.data = [self.auto, self.metro_people, self.work_place, self.type, self.k ]  # answers [auto, metro, all_people, type, k]
        return self.data


class office(Building):
    def __init__(self):
        super().__init__()
        self.setter(10)
        self.type = "office"

        print(self.getter())


class house(Building):
    def __init__(self):
        super().__init__()


        self.setter(25)
        self.type = "houses"

        print(self.getter())


class houses(house):
    def __init__(self):
        super().__init__()


        self.n = int(input("n: "))
        self.setter(25)


        self.type = "houses"


class hotel(Building):
    def __init__(self):
        super().__init__()
        self.setter(45)


        self.type = "hotel"
        print(self.getter())


# инфраструктура

class infrastructure:
    def __init__(self):
        self.using_passenger_traffic = None
        self.max_bandwidth = None
        self.max_passenger_traffic = None
        self.using_bandwidth = None

    def settings(self):
        self.max_passenger_traffic = int(input("max_passenger_traffic"))


class metro(infrastructure):
    def __init__(self, b, al):
        super().__init__()
        self.settings()
        self.using_passenger_traffic = 0.35*(al[1]+b[1])*b[4] # b[]
        self.using_bandwidth = f"{round(b[4]*100*self.using_passenger_traffic / self.max_passenger_traffic)}%"   # b[]
        return(self.max_passenger_traffic, self.using_bandwidth)

#[auto, metro, all_people, type, k]
class road(infrastructure):
    def __init__(self, b, al):
        super().__init__()
        self.settings()
        self.using_passenger_traffic = 0.35*(b[0]+al[0])*b[4]  # b[]
        self.using_bandwidth = f"{round(b[4]*100*self.using_passenger_traffic / self.max_passenger_traffic)}%"
        return(self.max_passenger_traffic, self.using_bandwidth)

b = hotel()
info = b.getter()
first_district = district()
info_all = first_district.getter()
Bellorys = metro(info,info_all)
