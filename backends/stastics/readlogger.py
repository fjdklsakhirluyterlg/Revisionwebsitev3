
def read_logger():
    file = "../../record.log"
    with open(file, "rb+") as f:
        f = f.readlines()
    f.close()


read_logger()   