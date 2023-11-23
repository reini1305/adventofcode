from copy import deepcopy

class IntCode:
    def __init__(self, memory, ip):
        self.memory = deepcopy(memory)
        self.ip = ip
        self.go = 0

    def addii(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]] + self.memory[self.memory[self.ip+2]]
        self.ip += 4

    def addid(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] + self.memory[self.memory[self.ip+2]]
        self.ip += 4

    def adddd(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] + self.memory[self.ip+2]
        self.ip += 4

    def addrd(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]+self.go] + self.memory[self.ip+2]
        self.ip += 4

    def adddr(self):
        
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] + self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def addrr(self):
        
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]+self.go] + self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def addri(self):
        
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+2]] + self.memory[self.memory[self.ip+1]+self.go] 
        self.ip += 4

    def adddi(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]] + self.memory[self.ip+2]
        self.ip += 4

    def mulii(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]] * self.memory[self.memory[self.ip+2]]
        self.ip += 4

    def mulid(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] * self.memory[self.memory[self.ip+2]]
        self.ip += 4

    def muldd(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] * self.memory[self.ip+2]
        self.ip += 4

    def muldrr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.ip+1] * self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def mulrrr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]+self.go] * self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def mulirr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]] * self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def mulddr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.ip+1] * self.memory[self.ip+2]
        self.ip += 4

    def muldir(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.ip+1] * self.memory[self.memory[self.ip+2]]
        self.ip += 4

    def mulrdr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]+self.go] * self.memory[self.ip+2]
        self.ip += 4

    def addddr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.ip+1] + self.memory[self.ip+2]
        self.ip += 4

    def addidr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]] + self.memory[self.ip+2]
        self.ip += 4

    def addrrr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]+self.go]  + self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def adddrr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.ip+1] + self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def addrdr(self):
        
        self.memory[self.memory[self.ip+3]+self.go]  = self.memory[self.memory[self.ip+1]+self.go]  + self.memory[self.ip+2]
        self.ip += 4

    def muldr(self):
        
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+1] * self.memory[self.memory[self.ip+2]+self.go] 
        self.ip += 4

    def mulrd(self):
        
        self.memory[self.memory[self.ip+3]] = self.memory[self.ip+2] * self.memory[self.memory[self.ip+1]+self.go] 
        self.ip += 4

    def muldi(self):
        self.memory[self.memory[self.ip+3]] = self.memory[self.memory[self.ip+1]] * self.memory[self.ip+2]
        self.ip += 4

    def get(self,input):
        self.memory[self.memory[self.ip+1]] = int(input)
        self.ip += 2

    def getr(self,input):
        
        self.memory[self.memory[self.ip+1]+self.go]  = int(input)
        self.ip += 2

    def out(self):
        output = self.memory[self.memory[self.ip+1]]
        self.ip += 2
        return output

    def outr(self):
        output = self.memory[self.memory[self.ip+1]+self.go] 
        self.ip += 2
        return output

    def outd(self):
        output = self.memory[self.ip+1]
        self.ip += 2
        return output

    def jit(self):
        if self.memory[self.memory[self.ip+1]] != 0:
            self.ip = self.memory[self.memory[self.ip+2]]
        else:
            self.ip += 3

    def jitdd(self):
        if self.memory[self.ip+1] != 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jitrd(self):
        
        if self.memory[self.memory[self.ip+1]+self.go]  != 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jitdr(self):
        
        if self.memory[self.ip+1] != 0:
            self.ip = self.memory[self.memory[self.ip+2]+self.go] 
        else:
            self.ip += 3

    def jitdi(self):
        if self.memory[self.memory[self.ip+1]] != 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jitid(self):
        if self.memory[self.ip+1] != 0:
            self.ip = self.memory[self.memory[self.ip+2]]
        else:
            self.ip += 3

    def jif(self):
        if self.memory[self.memory[self.ip+1]] == 0:
            return self.memory[self.memory[self.ip+2]]
        self.ip += 3

    def jifdd(self):
        if self.memory[self.ip+1] == 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jifdr(self):
        
        if self.memory[self.ip+1] == 0:
            self.ip = self.memory[self.memory[self.ip+2]+self.go] 
        else:
            self.ip += 3

    def jifrd(self):
        
        if self.memory[self.memory[self.ip+1]+self.go]  == 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jifdi(self):
        if self.memory[self.memory[self.ip+1]] == 0:
            self.ip = self.memory[self.ip+2]
        else:
            self.ip += 3

    def jifid(self):
        if self.memory[self.ip+1] == 0:
            self.ip = self.memory[self.memory[self.ip+2]]
        else:
            self.ip += 3

    def lt(self):
        if self.memory[self.memory[self.ip+1]] < self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltid(self):
        if self.memory[self.ip+1] < self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltdi(self):
        if self.memory[self.memory[self.ip+1]] < self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltdd(self):
        if self.memory[self.ip+1] < self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltdr(self):
        
        if self.memory[self.ip+1] < self.memory[self.memory[self.ip+2]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltrr(self):
        
        if self.memory[self.memory[self.ip+1]+self.go] < self.memory[self.memory[self.ip+2]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltrd(self):
        
        if self.memory[self.ip+2] > self.memory[self.memory[self.ip+1]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def ltrdd(self):
        
        if self.memory[self.ip+1] < self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]+self.go]  = 1
        else:
            self.memory[self.memory[self.ip+3]+self.go]  = 0
        self.ip += 4

    def eqrdd(self):
        
        if self.memory[self.ip+1] == self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]+self.go]  = 1
        else:
            self.memory[self.memory[self.ip+3]+self.go]  = 0
        self.ip += 4

    def eqrir(self):
        
        if self.memory[self.ip+1+self.go] == self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]+self.go]  = 1
        else:
            self.memory[self.memory[self.ip+3]+self.go]  = 0
        self.ip += 4

    def eqid(self):
        if self.memory[self.ip+1] == self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqr(self):
        if self.memory[self.memory[self.ip+1]+self.go] == self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqdi(self):
        if self.memory[self.memory[self.ip+1]] == self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqrd(self):
        
        if self.memory[self.ip+2] == self.memory[self.memory[self.ip+1]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqdr(self):
        
        if self.memory[self.ip+1] == self.memory[self.memory[self.ip+2]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqrr(self):
        
        if self.memory[self.memory[self.ip+1]+self.go] == self.memory[self.memory[self.ip+2]+self.go] :
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eq(self):
        if self.memory[self.memory[self.ip+1]] == self.memory[self.memory[self.ip+2]]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def eqdd(self):
        if self.memory[self.ip+1] == self.memory[self.ip+2]:
            self.memory[self.memory[self.ip+3]] = 1
        else:
            self.memory[self.memory[self.ip+3]] = 0
        self.ip += 4

    def setgod(self):
        
        self.go += self.memory[self.ip+1]
        self.ip += 2

    def setgor(self):
        
        self.go += self.memory[self.memory[self.ip+1]+self.go] 
        self.ip += 2

    def setgo(self):
        
        self.go += self.memory[self.memory[self.ip+1]]
        self.ip += 2

    def get_operatormap(self):
        # maps from opcode to function, jump to
        return {1:self.addii,
                1001:self.adddi,
                101:self.addid,
                201:self.addri,
                1101:self.adddd,
                1201:self.addrd,
                2101:self.adddr,
                2201:self.addrr,
                21001:self.addidr,
                21101:self.addddr,
                22101:self.adddrr,
                21201:self.addrdr,
                22201:self.addrrr,
                2:self.mulii,
                1002:self.muldi,
                102:self.mulid,
                1102:self.muldd,
                1202:self.mulrd,
                2102:self.muldr,
                20102:self.muldir,
                21102:self.mulddr,
                21202:self.mulrdr,
                22102:self.muldrr,
                22202:self.mulrrr,
                22002:self.mulirr,
                3:self.get,
                203:self.getr,
                4:self.out,
                104:self.outd,
                204:self.outr,
                5:self.jit,
                105:self.jitid,
                1005:self.jitdi,
                1105:self.jitdd,
                1205:self.jitrd,
                2105:self.jitdr,
                6:self.jif,
                106:self.jifid,
                1006:self.jifdi,
                1106:self.jifdd,
                2106:self.jifdr,
                1206:self.jifrd,
                7:self.lt,
                107:self.ltid,
                1007:self.ltdi,
                1107:self.ltdd,
                1207:self.ltrd,
                2107:self.ltdr,
                2207:self.ltrr,
                21107:self.ltrdd,
                108:self.eqid,
                208:self.eqr,
                1008:self.eqdi,
                1108:self.eqdd,
                1208:self.eqrd,
                2108:self.eqdr,
                2208:self.eqrr,
                21108:self.eqrdd,
                20208:self.eqrir,
                8:self.eq,
                9:self.setgo,
                109:self.setgod,
                209:self.setgor}