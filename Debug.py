message_stack = []
__number = 1


def log(args: ""):
    global __number
    message_stack.append(str(args))
    #print(__number, " ", str(args))
    __number = __number + 1
