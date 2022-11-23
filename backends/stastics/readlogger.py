
def read_logger():
    file = "../../record.log"
    with open(file, "rb+") as f:
        print("connected")
    f.close()


read_logger()   