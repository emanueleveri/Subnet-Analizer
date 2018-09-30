class subnetAnalizer:
    def __init__(self, ip1, ip2, mask):
        self.ip1=ip1
        self.ip2=ip2
        self.mask=mask

    def split(self):
        pointer = subnetAnalizer(self.ip1.split("."),(self.ip2.split(".")),(self.mask.split(".")))
        pointer.retBin(pointer)

    def retBin(self, pointer):
        ip1ret,ip2ret,maskret="","",""
        for element in pointer.ip1:
            ip1ret+=bin(int(element))[2:].zfill(8)
        for element in pointer.ip2:
            ip2ret+=bin(int(element))[2:].zfill(8)
        for element in pointer.mask:
            maskret+=bin(int(element))[2:].zfill(8)
        pnter = subnetAnalizer(ip1ret,ip2ret,maskret)
        pnter.maskCounter(maskret)
        pnter.check(pnter)
    def check(self,pointer):
            index = 0
            while index < self.count:
                if pointer.ip1[index]==pointer.ip2[index]:
                    same =True
                else:
                    same = None
                index+=1
            if same ==True:
                print ("This ip's are in the same subnet")
            else:
                print ("This ip's are in different subnets")

    def maskCounter(self, mask):
        count = 0
        for char in mask:
            if char=="1":
                count+=1
        self.count = count