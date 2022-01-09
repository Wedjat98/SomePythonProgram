from datetime import datetime

dt01 = datetime.now()


def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H-%M-%S")


print(datetime_toString(dt01))

