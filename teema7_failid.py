def loe_failist(file:str)->list:
    f=open(file,'r', encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def kirjuta_failisse(fail:str,jarjend:list)->list:
    f=open(fail,'w', encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

fail=loe_failist('TextFile1.txt')
print(fail)
for i in range(8,11,1):
    fail.append(input(f"{i}-i:"))
kirjuta_failisse('TextFile1.txt',fail)
fail=loe_failist('TextFile1.txt')


