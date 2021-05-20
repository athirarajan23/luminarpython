#quantifiers
# x='a+'  a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a

#eg1
# import re
# x="a+"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg2
# import re
# x="a*"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg3
# import re
# x="a?"
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg4
# import re
# x="a{2}"
# r="aaa abc aaaa cga"    #cursur stop skiyad tott check chyum
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg4
# import re
# x="a{2,3}"    #minimum 2 max 3
# r="aaa abcaaaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


#eg5
#import re
# x="^a" #whole string starting with a?
# r="aaa abc aaaa cga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg6
# import re
# x="a$"
# r="aaa abc aaaa cg"  #check whether the string is ending with a
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())