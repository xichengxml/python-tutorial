# ---------------------------
# @description 类的继承: 属性的继承、方法的继承与重写
# @author xichengxml
# @date 2019/10/5 下午 09:31
# ---------------------------


# 定义怪物类
class Monster:
    def __init__(self, hp, longitude=0, latitude=0):
        self.hp = hp
        self.longitude = longitude
        self.latitude = latitude

    def move(self):
        print('move to: %s, %s' % (self.longitude, self.latitude))


# 普通怪物
class Animal(Monster):
    pass


# boss怪物
class Boss(Monster):
    pass


monster = Monster(100)
print(monster.hp)
monster.move()

animal = Animal(10)
print(animal.hp)
animal.move()

# type和instance
print(type(animal))
print(isinstance(animal, Monster))
