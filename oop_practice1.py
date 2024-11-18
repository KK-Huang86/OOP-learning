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



#11/14

#繼承

class Dog:
  def __init__(self,color,tall,leg=4):
    self.leg=leg
    self.__tall=tall #私有屬性
    self.color=color

  def attack(self):
    print("attack!!")

  # 提供取得私有屬性的公開方法A
  def get_tall(self):
    return self.__tall
  
  # 提供取得私有屬性的公開方法B

  def set_tall(self,tall):
      if tall > 0:  # 可以加入條件檢查
          self.__tall = tall
      else:
        print("身高必須高於0")



class LittleDog(Dog):
  def __init__(self,color,tall,leg,yell):
    super().__init__(color,tall,leg)
    self.yell=yell

#多型

  def attack(self):
    print("攻擊其他人")

littledog2=LittleDog("white",4,4,"WOO")
littledog2.attack()
print(littledog2.color)
print(littledog2.leg)

print(littledog2.get_tall())
print("Tall before:", littledog2.get_tall())  # 取得 __tall 的值
littledog2.set_tall(6)  # 修改 __tall 的值
print("Tall after:", littledog2.get_tall())


# 一個Shape的類別
# 並使用ger_area()
# 然後還有Square的類別要繼承Shape
# 並使用Get_area()
# Square的side=2 要得到結果 2*2 = 4 
# 還有一個Triangle的類別要繼承Shape
# 並使用Get_area()
# Triangle的base=2 height=4 要得到結果2*4/2 

class Shape:
    def get_area(): #多形
        raise NotImplementedError("子類別必須使用 get_area 方法") #抽象

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def get_area(self):
        return self.side*self.side
    
class Triangle(Shape):
    def __init__ (self,base,height):
        self.base=base
        self.height=height
    def get_area(self):
        return int((self.base*self.height)/2)


square=Square(side=2)
triangle=Triangle(base=2,height=4)

print(f"面積{square.get_area()}")
print(f"面積{triangle.get_area()}")
