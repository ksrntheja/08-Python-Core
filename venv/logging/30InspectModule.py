from InspectModuleTest import getInfo


def f1():
    getInfo()


f1()

# inspect.stack()
# [FrameInfo(frame=<frame object at 0x1d51a88>, filename='/Code/venv/logging/InspectModuleTest.py', lineno=5, function='getInfo', code_context=['    print(inspect.stack())\n'], index=0), FrameInfo(frame=<frame object at 0x1cbc7e8>, filename='/Code/venv/logging/30InspectModule.py', lineno=5, function='f1', code_context=['    getInfo()\n'], index=0), FrameInfo(frame=<frame object at 0x1cd9f48>, filename='/Code/venv/logging/30InspectModule.py', lineno=8, function='<module>', code_context=['f1()\n'], index=0)]

# inspect.stack()[1]
# FrameInfo(frame=<frame object at 0x27917e8>, filename='/Code/venv/logging/30InspectModule.py', lineno=5, function='f1', code_context=['    getInfo()\n'], index=0)

# Caller module: /Code/venv/logging/30InspectModule.py
# Caller function name: f1
