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
    def textBox(self):
        pass

# 자식클래스 Darkfactory
class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    def getScrollBar(self):
        return DarkScrollBar()
    def getCheck(self):
        return DarkCheckBox()
    def getSlider(self):
        return DarkSlider()
    def gettextBox(self):
        return DarkTextBox()

# 자식클래스 LightFactory
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    def getScrollBar(self):
        return LightScrollBar()
    def getCheck(self):
        return LightCheckBox()
    def getSlider(self):
        return LightSlider()
    def gettextBox(self):
        return LightTextBox()

# 자식클래스 RedFactory
class RedFactory(UIFactory):
    def getButton(self):
        return RedButton()
    def getScrollBar(self):
        return RedScrollBar()
    def getCheck(self):
        return RedCheckBox()
    def getSlider(self):
        return RedSlider()
    def gettextBox(self):
        return RedTextBox()

# 자식클래스 BlueFactory
class BlueFactory(UIFactory):
    def getButton(self):
        return BlueButton()
    def getScrollBar(self):
        return BlueScrollBar()
    def getCheck(self):
        return BlueCheckBox()
    def getSlider(self):
        return BlueSlider()
    def gettextBox(self):
        return BlueTextBox()

