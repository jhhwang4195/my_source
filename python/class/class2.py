# -*- coding: utf-8 -*-
#!/usr/bin/python


class Rectangle:
    count = 0  # 클래스 변수

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area

    # 정적 메서드
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight

    # 클래스 메서드
    @classmethod
    def printCount(cls):
        print(cls.count)

if __name__ == '__main__':
    square = Rectangle.isSquare(5, 5)
    print(square)   # True

    rect1 = Rectangle(5, 5)
    rect1.printCount()  # 2

    # 객체 생성
    r = Rectangle(2, 3)

    # 메서드 호출
    area = r.calcArea()
    print("area = %d" % area)

    # 인스턴스 변수 엑세스
    r.width = 10
    print("width = %d" % r.width)

    # 클래스 변수 엑세스
    print(Rectangle.count)
    print(r.count)

    # print vars, dict, dir
    print "\n>>>> vars(r)"
    print vars(r)
    print "\n>>>> r.__dict__"
    print r.__dict__
    print "\n>>>> dir(r)"
    print dir(r)


"""
########################################
# Result
########################################
True
1
area = 6
width = 10
2
2

>>>> vars(r)
{'width': 10, 'height': 3}

>>>> r.__dict__
{'width': 10, 'height': 3}

>>>> dir(r)
['__doc__', '__init__', '__module__', 'calcArea', 'count', 'height', 'isSquare', 'printCount', 'width']
"""
