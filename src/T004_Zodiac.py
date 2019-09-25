
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座',
               u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座',
               u'天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (4, 22)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)

zodiac_index = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_index])


