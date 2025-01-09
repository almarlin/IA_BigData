from datetime import datetime

def conv(fecha):
    f = datetime.strptime(fecha,"%Y/%m/%d")
    f2 = datetime.strftime(f,"%d/%m/%Y")
    return f2

print(conv("2024/11/08"))