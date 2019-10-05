# ---------------------------
# @description 类的使用
# @author xichengxml
# @date 2019/10/5 下午 09:13
# ---------------------------


# 定义玩家类
class Player:
    # 定义三个属性
    def __init__(self, name, hp, occupation):
        # 增加两个下划线后，外部不可直接修改属性值，只能通过方法修改
        self.__name = name
        self.hp = hp
        self.occupation = occupation

    def print_role(self):
        print('name: %s, hp: %s, occupation: %s' % (self.__name, self.hp, self.occupation))

    def update_name(self, new_name):
        self.__name = new_name


# 定义怪物类，如果不想报错，类定义下面写一个pass即可
class Monster:
    pass


# 类的继承
class Animal(Monster):  # 普通怪物
    pass


class Boss(Monster):  # boss怪物
    pass


player01 = Player('Tom', 100, 'warrior')
player02 = Player('Jerry', 80, 'master')

player01.print_role()
player02.print_role()

# name值不会被修改
player01.name = 'NewTom'
player01.hp = 110
player01.print_role()
