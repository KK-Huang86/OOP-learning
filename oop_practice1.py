class Car:
  def __init__(self,brand,model,color,year):
    self.brand=brand
    self.model=model
    self.color=color
    self.year=year
    self.__type="200"
    print("資料初始化中")

  def drive(self):
    print(self.model+"正在行駛中")

  def stop(self):
    print(self.brand+"的"+self.model+"停了下來")

  def fly(self):
    self.__go()

  def hey(self):
    print(self.__type)

#封裝，只有在類可以呼叫
  def __go(self):
    print("走吧！")

# car1=Car("Ford","Kuga","black","2019")
# car1.fly()
# print(car1.color)


#self
#Class （類）尚未實體化，缺少self參數
# Car.fly()  #TypeError: Car.fly() missing 1 required positional argument: 'self' 

#有一個物件，並將它丟進類所需的參數裡
car2=Car("cc","g1","blue","2019")
Car.stop(car2)
car2.hey()


#繼承

class ElectricCar(Car):
  def __init__(self, brand, model, color, year, battery_capacity):
    super().__init__(brand, model, color, year)
    self.battery_capacity= battery_capacity
  def charge(self):
    print(self.model+ "正在充電中" + self.battery_capacity )



# print(car1.brand)

# car1.drive()


# electic_car1=ElectricCar("特斯拉","Model S" , "gray","2","50")
# electic_car1.charge()