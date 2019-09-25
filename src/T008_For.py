list_a = []
for i in range(1, 11):
    if i % 2 == 0:
        list_a.append(i * i)
print(list_a)

list_b = [i * i for i in range(1, 11) if i % 2 == 0]
print(list_b)

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座',
               u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座',
               u'天蝎座', '射手座')
map_a = {}
for i in zodiac_name:
    map_a[i] = 0
print(map_a)

map_b = {i:0 for i in zodiac_name}
print(map_b)
