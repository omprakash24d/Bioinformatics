class Sequence:
    def __init__(self, seq = "Provide seq", func = "write func"):
        self.seq = seq
        self.func = func
    def print_seq(self):
        print('self',self)
        print(self.seq)
        #print(self.func)
    def __str__(self):
        return '%s \t %s' % (self.seq,self.func)
     
y  = Sequence('ATCGATGC','XXXXXX')

print(type(y))

z  = Sequence('TATA','BATA')

#z.print_seq()
#print(z)

zzz = Sequence('GGGGGATGC','XXXXXX')
#zzz.print_seq()

#delattr(zzz,'seq')
#zzz.print_seq()

#del zzz
#zzz.print_seq()


class Exon(Sequence):
    def __init__(self, seq = "Provide seq", func = "write func", posi = 'Numeric posi'):
        super().__init__(seq,func)
        self.posi = posi
    
    def print_seq(self):
       print(self.seq,self.func,self.posi)

p = Exon('ExonSeq','vvv',321)

print(type(p))

p.print_seq()

class Protein(Exon,Sequence):
    def __init__(self, seq, func, posi, prt_len = 'prt_len'):
        #Sequence.__init__(seq,func)
        #Exon.__init__(posi)
        super().__init__(seq,func,posi)
        self.prt_len = prt_len
prt = Protein('ExonSeq','vvv',321,300)

print(type(prt))

print(Protein.__mro__)

#print(Protein.mro())