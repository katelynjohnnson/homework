class Car:

    def __init__(self,yrmodel,make):
        self.__YearModel = yrmodel
        self.__Make = make
        self.__Speed = 0

    def accelerate(self):
        self.__Speed += 5

    def brake(self):
        self.__Speed -= 5

    def get_speed(self):
        return self.__Speed

def main():
    car = Car("2006 Pilot",'Honda')
    print('Accelerating')

    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    print('Decelerating')
    
    for i in range(5):
        car.brake()
        print(car.get_speed())

if __name__ == '__main__':
    main()



    