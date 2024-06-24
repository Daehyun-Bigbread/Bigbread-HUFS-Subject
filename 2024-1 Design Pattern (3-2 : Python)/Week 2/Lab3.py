# 수정 전

# 자식 클래스 정의: 전등 클래스
class Light:
    def turn_on(self):
        print("Light turned on")
    def turn_off(self):
        print("Light turned off")

# 자식 클래스 정의: 팬 클래스
class Fan:
    def turn_on(self):
        print("Fan turned on")
    def turn_off(self):
        print("Fan turned off")

# 2자식 클래스 정의: 스위치 클래스
class Switch:
    def __init__(self):
        self.light = Light()
        self.Fan = Fan()

    def turn_light_on(self):
        self.light.turn_on()

    def turn_light_off(self):
        self.light.turn_off()

    def turn_fan_on(self):
        self.Fan.turn_on()

    def turn_fan_off(self):
        self.Fan.turn_off()

# 예시의 사용
switch = Switch()
switch.turn_light_on()
switch.turn_light_off()
switch.turn_fan_on()
switch.turn_fan_off()



# 수정 후

# 장치 인터페이스 정의
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# 전등 클래스 - Device 인터페이스 구현
class Light(Device):
    def turn_on(self): 
        print("Light turned on")

    def turn_off(self): 
        print("Light turned off")

# 팬 클래스 - Device 인터페이스 구현
class Fan(Device):
    def turn_on(self):
        print("Fan turned on")

    def turn_off(self): 
        print("Fan turned off")

# 스위치 클래스
class Switch:
    def __init__(self, device):
        self.device = device

    def turn_on(self):  
        self.device.turn_on()

    def turn_off(self): 
        self.device.turn_off()

# 예시 사용
light = Light()
fan = Fan()

light_switch = Switch(light)
fan_switch = Switch(fan)

light_switch.turn_on()  
light_switch.turn_off()  
fan_switch.turn_on() 
fan_switch.turn_off()  
