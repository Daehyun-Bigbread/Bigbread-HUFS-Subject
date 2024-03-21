# 객체: Button, ScrollBar, CheckBox, Slider, TextBox
# Theme: Dark, Light, Red, Blue
# 제품 생성
class UIFactory:
    def getButton(self):
        pass
    
    def getScrollBar(self):
        pass
    
    def getCheckBox(self):
        pass   
    
    def getSlider(self):
        pass
    
    def getTextBox(self):
        pass

# Dark 테마용 구체적인 제품 클래스들
class DarkButton:
    pass

class DarkScrollBar:
    pass

class DarkCheckBox:
    pass

class DarkSlider:
    pass

class DarkTextBox:
    pass

# Light 테마용 구체적인 제품 클래스들
class LightButton:
    pass

class LightScrollBar:
    pass

class LightCheckBox:
    pass

class LightSlider:
    pass

class LightTextBox:
    pass

# Red 테마용 구체적인 제품 클래스들
class RedButton:
    pass

class RedScrollBar:
    pass

class RedCheckBox:
    pass

class RedSlider:
    pass

class RedTextBox:
    pass

# Blue 테마용 구체적인 제품 클래스들
class BlueButton:
    pass

class BlueScrollBar:
    pass

class BlueCheckBox:
    pass

class BlueSlider:
    pass

class BlueTextBox:
    pass

# 자식클래스 DarkFactory
class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    
    def getScrollBar(self):
        return DarkScrollBar()
    
    def getCheckBox(self):
        return DarkCheckBox()
    
    def getSlider(self):
        return DarkSlider()
    
    def getTextBox(self):
        return DarkTextBox()

# 자식클래스 LightFactory
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    
    def getScrollBar(self):
        return LightScrollBar()
    
    def getCheckBox(self):
        return LightCheckBox()
    
    def getSlider(self):
        return LightSlider()
    
    def getTextBox(self):
        return LightTextBox()

# 자식클래스 RedFactory
class RedFactory(UIFactory):
    def getButton(self):
        return RedButton()
    
    def getScrollBar(self):
        return RedScrollBar()
    
    def getCheckBox(self):
        return RedCheckBox()
    
    def getSlider(self):
        return RedSlider()
    
    def getTextBox(self):
        return RedTextBox()

# 자식클래스 BlueFactory
class BlueFactory(UIFactory):
    def getButton(self):
        return BlueButton()
    
    def getScrollBar(self):
        return BlueScrollBar()
    
    def getCheckBox(self):
        return BlueCheckBox()
    
    def getSlider(self):
        return BlueSlider()
    
    def getTextBox(self):
        return BlueTextBox()
