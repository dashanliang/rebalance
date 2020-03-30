def sigmoid(x):
    if (x > 0):
        return 1
    else:
        return 0

def realGot(data):
    result = 0
    for singledata in data:
        result = result + sigmoid(int(singledata))
    return result * result

def combainData(**data):
    result = 0
    for value in data.values():
        result = result + realGot(value)
    return result

def combainDataUpdate(data):
    result = 0
    for value in data:
        result = result + sigmoid(int(value))
    return result


def realTime(data):
    result = 0
    for singledata in data:
        result = result + sigmoid(int(singledata))
    return result

def combainDataTime(**data):
    result = 0
    for singledata in data.values():
        result = result + sigmoid(realTime(singledata))
    return result