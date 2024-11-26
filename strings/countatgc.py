seq='''atgcccdfgetrgdvdatgctagctuuuagaATGC'''
atgc_upper=seq.upper()
print(atgc_upper)
atgc_count=atgc_upper.count('ATGC')
print(atgc_count)
p=seq.count('gc')
q=len(seq)
gcperc=(p*100)/q
print(gcperc)
print(seq.startswith("aug"))
print(seq.find("uuu"))
# name1="Om"
# name2="Prakash"
# full_name=name1," "+name2
# print(full_name)
txt="Good NIght Sam"
x='Good'
y='Food'
z='odnght'
my_table=txt.maketrans(x,y)
print(txt.maketrans(my_table))