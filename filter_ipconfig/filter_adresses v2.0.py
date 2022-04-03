######################################################################## MAC BEFORE IP ############################################################################
final = {}
ip = "0"
mac = "0"
nics = ["Realtek", "Intel(R) Ethernet", "Asus", "Nvidia"]
tmp = []
default_file = "319.txt"
ready_file = "319_new.txt"

def strTolist():
    with open(default_file, "r") as file:
        for line in file:
            tmp.append(line)

def filterCreateReadyData():
    count = 0
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
                count += 1          
   
    print("Raw quantity: ", count)           

strTolist()
filterCreateReadyData()


