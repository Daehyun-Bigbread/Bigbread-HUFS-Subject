class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

class Drawing:
    def draw_shape(self, shape):
        if shape_type == cirlce:
            circle= Circle()
            cirlce.draw()
        elif shape_type == square:
            square= Square()
            square.draw()
        elif shape_type == rectangle:
            rectangle= Rectangle()
            rectangle.draw()
        else:
            print("Error: Invalid shape type")

# 사용 예시
drawing= Drawing()
drawing.draw_shape("circle")
drawing.draw_shape("square")
drawing.draw_shape("rectangle")