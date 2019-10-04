try:
    year = int(input("input year"))
except ValueError:
    print("年份要输入数字")

# except(ValueError, AttributeError, KeyError):
print("------------------")

try:
    print(1 / 'a')
except Exception as e:
    print("error: %s" % e)

print("-------------------")
try:
    raise NameError("hello error")
except NameError as e:
    print("my custom error: %s" % e)

print("-------------------")
try:
    file = open("name.txt")
except Exception as e:
    print(e)
finally:
    file.close()

