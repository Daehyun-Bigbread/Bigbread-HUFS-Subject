class Button:
    def click(self):
        pass

class DarkButton(Button):
    def click(self):
        print("dark click")

class LightButton(Button):
    def click(self):
        print("light click")

class CheckBox:
    def check(self):
        pass

class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")

class LightCheckBox(CheckBox):
    def check(self):
        print("light check")

class ScrollBar:
    def scroll(self):
        pass

class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark scrollbar")

class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light scrollbar")

class UIFactory:
    def getButton(self):
        pass
    
    def getScrollBar(self):
        pass
    
    def getCheckBox(self):
        pass

class DarkUIFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    
    def getScrollBar(self):
        return DarkScrollBar()
    
    def getCheckBox(self):
        return DarkCheckBox()

class LightUIFactory(UIFactory):
    def getButton(self):
        return LightButton()
    
    def getScrollBar(self):
        return LightScrollBar()
    
    def getCheckBox(self):
        return LightCheckBox()

# 사용 예시
df = DarkFactory()
bt = df.getButton()
ck = df.getCheck()
sc = df.getScroll()
bt.click()
ck.check()
sc.scroll()