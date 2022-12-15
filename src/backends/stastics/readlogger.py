
def read_logger():
    file = "../../record.log"
    with open(file, "rb+") as f:
        f = f.readlines()
    
    list = []
    for line in f:
        if b"(process_request_thread)" in f:
            list.append(line)
    


    print(f)



read_logger()   