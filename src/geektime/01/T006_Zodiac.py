chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座',
               u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座',
               u'天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

cz_map = {}
for i in chinese_zodiac:
    cz_map[i] = 0

zname_map = {}
for i in zodiac_name:
    zname_map[i] = 0

while True:
    year = int(input("请输入年份: "))
    month = int(input("请输入月份: "))
    day = int(input("请输入日期: "))

    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1

    # 输出生肖和星座
    print(zodiac_name[n])
    print("%s 年的生肖是: %s" % (year, chinese_zodiac[year % 12]))

    cz_map[chinese_zodiac[year % 12]] += 1
    zname_map[zodiac_name[n]] += 1

    # 输出生肖和星座统计信息
    for each_key in cz_map.keys():
        print("生肖 %s 有 %d 个" % (each_key, cz_map[each_key]))

    for each_key in zname_map.keys():
        print("星座 %s 有 %d 个" % (each_key, zname_map[each_key]))
