 #rules used for pattern matching
 # #1. x='[abc]' either a,b or c
#eg:
# import re
# x="[abc]"
# matcher=re.finditer(x,"abt cq5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#2. x='[^abc]' except abc
#eg:
# import re
# x="[^abc]"
# matcher=re.finditer(x,"abt cq5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#3. x='[a-z]' a to z ^ cap means that is not included
#eg
# import re
# x="[a-z]"
# matcher=re.finditer(x,"abt cq5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#eg with ^
# import re
# x="[^a-z]"
# matcher=re.finditer(x,"abt cq5kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#4. x='[A-Z]' A TO Z
# import re
# x="[A-Z]"
# matcher=re.finditer(x,"abt SC5kZ")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#5.X="[a-zA-Z]" BOTH LOWER AND UPPERCASE ARE CHECKED
import re
x="[a-zA-Z]"
matcher=re.finditer(x,"abtABIkz")
for match in matcher:
    print(match.start())
    print(match.group())

#6. X="[0-9]"
# import re
# x="[0-9]"
# matcher=re.finditer(x,"ab1z7")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#7.x="[a-zA-Z0-9]"
# import re
# x="[a-zA-Z0-9]"
# matcher=re.finditer(x,"ab72ABIkz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#8.x='\s'  check space
# import re
# x="\s"
# matcher=re.finditer(x,"ab tAB  Ikz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#9.x='\d' check the digits
# import re
# x="\d"
# matcher=re.finditer(x,"ab7tAB12kz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#9. x='\D'  except digits
# import re
# x="\D"
# matcher=re.finditer(x,"ab001tAB5236Ikz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#10. x='\w' all words except special characters
# import re
# x="\w"
# matcher=re.finditer(x,"ab %tAB @Ikz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


#11.x='\W' for special characters
# import re
# x="\W"
# matcher=re.finditer(x,"ab!!tAB@Ikz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
