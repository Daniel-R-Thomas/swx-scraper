def appendToAddress(nameString, addressString):
    f=open("data/address.txt","a+")
    f.write(nameString + "\r\n")
    f.write(addressString+ "\r\n")
    f.close()

#appendToAddress("John Smith", "Grove Streeeet")
def checkAddress(nameString):
    datafile = open("data/address.txt","r")
    for line in datafile:
        if nameString in line:
            datafile.close()
            return "true"
    datafile.close()
    return "false"

#The other data can easily be implimented from above
