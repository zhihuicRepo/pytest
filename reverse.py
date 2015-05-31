def reverse(text1):
    strA = ""
    for i in range(len(text1)-1,-1,-1):
        strA +=  text1[i]
    print strA
    return strA
reverse('abcdef')

def reverse2(text):
#    print letter(reversed(text))
     print text[::-1]
reverse2('chenzhihui')
s = '0987654321'
#print ''.join((s[i] for i in xrange(len(s)-1, -1, -1)))
print ''.join((s[i] for i in range(-1, -1-len(s), -1)))

name="mohit"
rev_name=''
for i in range(len(name)-1,-1,-1):
   rev_name+=name[i]
print rev_name
