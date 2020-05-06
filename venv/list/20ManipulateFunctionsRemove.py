n = [10, 20, 10, 30]
print(n.remove(10))
print(n)
n.remove(40)
print(n)

# None
# [20, 10, 30]
# Traceback (most recent call last):
#   File "/Code/venv/list/20ManipulateFunctionsRemove.py", line <>, in <module>
#     n.remove(40)
# ValueError: list.remove(x): x not in list
