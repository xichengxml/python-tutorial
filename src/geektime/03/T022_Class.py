# ---------------------------
# @description 类的使用
# @author xichengxml
# @date 2019/10/5 下午 08:46
# ---------------------------


# 面向过程
user1 = {'name': 'Tom', 'hp': 100}
user2 = {'name': 'Jerry', 'hp': 80}


def print_role(role):
    print('role name: %s, role hp: %s' % (role['name'], role['hp']))


print_role(user1)
print_role(user2)


# 面向对象
class Role:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_info(self):
        print('role name: %s, role hp: %s' % (self.name, self.hp))


user3 = Role('Tom', 100)
user4 = Role('Jerry', 80)
user3.print_info()
user4.print_info()
