l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in l:
    print(x if x % 2 == 0 else '', end='\n' if x % 2 == 0 else '')
    # print(x if x % 2 == 0 else pass, end='\n' if x % 2 == 0 else '')
    #   File "/Code/venv/list/09TraverseEven.py", line <>
    #     print(x if x % 2 == 0 else pass, end='\n' if x % 2 == 0 else '')
    #                                   ^
    # SyntaxError: invalid syntax

# 0
# 2
# 4
# 6
# 8
# 10
