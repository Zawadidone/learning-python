from dis import dis


def hello():
    return 1


print(dis(hello))
