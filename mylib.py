class Radio:
    def __init__(self):
        self.__current_station = 0

    def next(self):
        if self.__current_station != 9:
            self.__current_station += 1
        else:
            self.__current_station = 0

    def get_current_station(self):
        return self.__current_station

    def set_current_station(self, current_station):
        if 0 <= current_station <= 9:
            self.__current_station = current_station


