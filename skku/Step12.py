# 상속: 부모 클래스의 기능을 그대로 사용하며 자식클래스에서 추가적인 기능을 사용할 때 사용.
# 오버로딩: 같은 클래스 내에서 같은 메소드를 사용하는 것
# 오버라이딩: 상위 클래스에 있는 같은 메소드를 사용하는 것
class Vehicle:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getName(self):
        return self.__name

class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.__model = model
    def getDescription(self):
        return self.getName()+self.__model+" in " +self.getColor()+ " color"

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())




