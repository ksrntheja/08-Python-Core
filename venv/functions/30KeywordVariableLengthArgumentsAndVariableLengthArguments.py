def var(**kwargs, *args):
    print('Printing kwargs :', kwargs, 'type of kwargs :', type(kwargs))
    print('Printing args   :', args, 'type of args :', type(args))

# After keyword args, positional args are not allowed

#   File "/Code/venv/functions/30KeywordVariableLengthArgumentsAndVariableLengthArguments.py", line <>
#     def var(**kwargs, *args):
#                       ^
# SyntaxError: invalid syntax
