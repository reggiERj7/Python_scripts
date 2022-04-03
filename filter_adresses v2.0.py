######################################################################## MAC BEFORE IP #############################################################################
ip = "0"
mac = "0"
final = {}
nics = ["Realtek", "Intel(R) Ethernet", "Asus", "Nvidia"]
tmp = []
default_file = "342.txt"
ready_file = "342_new.txt"
counter = 0

def convert_txt_to_list():
    with open(default_file) as file:
        for line in file:
            tmp.append(line)

def filter_and_create_ready_data():
    with open(ready_file, "w") as result:
        for i in tmp:
            for k in nics:
                if k in i:
                    nxtind = tmp.index(i) + 1
                    mac = tmp[nxtind]
                    del tmp[tmp.index(i)]   
            if "IPv4 Address. . . . . . . . . . . : 172.16." in i:
                ip = i
                final = {ip:mac}
                result.write(str(final) + "\n")                  
                counter = counter + 1
    print("Raw quantity: " + counter)                
        

convert_txt_to_list()
filter_and_create_ready_data()

