class CarColor:
    def __init__(self, color_name, rgb_value):
        self.color_name = color_name
        self.rgb = rgb_value
    
    def __str__(self):
        return f"{self.color_name}, RGB: {self.rgb}"

class ColorFactory:
    _colors = {}
    
    @classmethod
    def get_color(cls, color_name):
        if color_name not in cls._colors:
            if color_name == "red":
                cls._colors[color_name] = CarColor("red", (255, 0, 0))
            elif color_name == "blue":
                cls._colors[color_name] = CarColor("blue", (0, 0, 255))
            elif color_name == "green":
                cls._colors[color_name] = CarColor("green", (0, 255, 0))
            elif color_name == "white":
                cls._colors[color_name] = CarColor("white", (255, 255, 255))
            elif color_name == "black":
                cls._colors[color_name] = CarColor("black", (0, 0, 0))
        return cls._colors[color_name]
class Car:
    def __init__(self, year, brand, name, fuel_type, color_name):
        self.year = year
        self.brand = brand
        self.name = name
        self.fuel_type = fuel_type
        self.color = ColorFactory.get_color(color_name)
    
    def __str__(self):
        return f"Car: {self.brand} {self.name}, Year: {self.year}, Fuel: {self.fuel_type}, Color: {self.color}"

# 자동차 객체 생성
car1 = Car(2020, "Hyundai", "Sonata", "Gasoline", "red")
car2 = Car(2021, "Kia", "Sorento", "Diesel", "red")

print(car1)
print(car2)

# 두 자동차의 색상이 같은지 확인
print(car1.color is car2.color)
