#삼각형 클래스 만들기
print("================================")
class Triangle(object):
    def __init__(self, b, h):
        self.b = b
        self.h = h
        print('가로 : %d 세로 : %d' % (self.b, self.h))

    def area(self):
        print('넓이 : ', end='')
        return self.b * self.h / 2


t1 = Triangle(10, 20)
print(t1.area())
t2 = Triangle(30, 4)
print(t2.area())

#사각기둥 클래스 만들기
print("================================")

class squareColumn(object):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        print('가로 : %d 세로 : %d 높이 : %d' % (self.a, self.b, self.h))

    def volume(self):
        print('부피 : ', end='')
        return self.a * self.b * self.h

    def surface(self):
        print('겉넓이 : ', end='')
        return 2*(self.a*self.b+self.b*self.h+self.a*self.h)


s1 = squareColumn(10, 20, 30)
print(s1.volume())
print(s1.surface())

s2 = squareColumn(10, 5, 3)
print(s2.volume())
print(s2.surface())

#오버라이딩
print("================================")

class character(object):
    def __init__(self):
        self.life = 100

    def attacked(self):
        pass


class AD(character):
    def __init__(self):
        super().__init__()

    def attacked(self):
        self.life -= 10


class AP(character):
    def __init__(self):
        super().__init__()

    def attacked(self):
        self.life -= 20
        
c1 = AD()
c2 = AP()
print(c1.life)
c1.attacked()
print(c1.life)
print(c2.life)
c2.attacked()
print(c2.life)

#car class
print("================================")

class car(object):
    def __init__(self):
        self.max_speed = 160
        self.speed = 0

    def speed_up(self):
        if(self.speed + 20 <= self.max_speed):
            self.speed += 20

    def speed_down(self):
        if (self.speed - 20 >= 0):
            self.speed -= 20

c = car()
print(c.speed)
for i in range(10):
    c.speed_up()
    print(c.speed)

for i in range(10):
    c.speed_down()
    print(c.speed)
