
def read_logger():
    file = "../../record.log"
    with open(file, "rb+") as f:
        f = f.readlines()
    
    list = []
    for line in f:
        if "(process_request_thread)" in f:
            list.append(line)
    f.close()


read_logger()   