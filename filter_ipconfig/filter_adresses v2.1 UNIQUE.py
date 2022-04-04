# ######################################################################## MAC BEFORE IP ############################################################################
import re

tmp = []
default_file = "107.txt"
ready_file = "new.txt"
def strTolist():
    with open(default_file, "r") as deffile:
        for line in deffile:
            tmp.append(line)

def filter():
    last_ip = ""
    with open("new.txt", "w") as newfile:
        for i in tmp:
            if re.findall("IPv4", i):
                tmp_ip = str(re.findall("\d{3}\.\d{2}\.\d.*\.\d.*", i))
                ip = re.sub("[\[\]']", '', tmp_ip)
            if re.findall("Adapter:\s{2}Intel.*Ethernet|Realtek|Asus|Nvidia", i):
                index = tmp.index(i) + 1
                tmp_mac = str(re.findall("..-..-..-..-..-..", tmp[index]))
                mac = re.sub("[\[\]']", '', tmp_mac)
                if last_ip == ip:
                    result = "НЕТ АДРЕСА" + " " + mac
                    newfile.writelines(result + "\n")
                    del tmp[tmp.index(i)]
                else:
                    result = ip + " " + mac
                    newfile.writelines(result + "\n")
                    del tmp[tmp.index(i)]   
                last_ip = ip     

strTolist()
filter()

