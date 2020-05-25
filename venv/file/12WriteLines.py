f = open('abcde.txt', 'w')
list = ["item1\n", "item2", "item3\n", "item4"]
tuple = ("tuple1\n", "tuple2\n", "tuple3\n", "tuple4")
set = {"set1\n", "set2\n", "set3\n", "set4"}
dict = {"dict1": "dict2\n", "dict3\n": "dict4",
        # 100: "dict6\n", "dict7\n": 200}
        # "dict7\n": 200}
        "dict7\n": "200"}
f.writelines(list)
f.writelines(tuple)
f.writelines(set)
f.writelines(dict)
f.writelines(dict.values())
f.writelines([dict['dict1'], dict['dict7\n']])
# Traceback (most recent call last):
#   File "=/Code/venv/file/12WriteLines.py", line <>, in <module>
#     f.writelines(dict)
# TypeError: write() argument must be str, not int
print('Write done')
f.close()

# Write done

# abcde.txt
# item1
# item2item3
# item4tuple1
# tuple2
# tuple3
# tuple4set3
# set2
# set1
# set4dict1dict3
# dict7
# dict2
# dict4200dict2
# 200
