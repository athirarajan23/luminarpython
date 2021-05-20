import re
r=open("contact","r")
f=open("num","w")
rule="[+][9][1]\d{10}$"
for num in r:
    number =num.rstrip("\n")
    match=re.fullmatch(rule,number)
    if match is not None:
        f.write(number)
        f.write("\n")

#contact enna file store chyda phnnumbersl valid numbers matram num enna file lk write chyan ila program.