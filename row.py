
#1
text = 'kndklsnxlknsd'
print(len(text))
for i in range(3):
    result = text * 3
    print(text.split())

#6
text = 'hello world'

for i in range(3, 11, 3):
    print(text[i])

#11
text = 'hello world'

if len(text) > 10:
    print(text[6:])
else:
    print(text.ljust(12, 'o'))


#14
txt = 'djnajknxk'
print(len(txt))


#15
text = "some text"

for i in text:
    if i not in "abc":
        print("contains other characters")
        break
    else:
        print("ok")



#16
txt = "word word word"
print(txt.replace("word", "letter"))


#17
txt = "xabsabcxabsabc4rj"

txt = txt.replace("xabc", "abc")
print(txt)


#18
txt = "abc2 test abc2 abc"

for i in range(10):
    txt = txt.replace('abc' + str(i), '')
print(txt)


#19
txt = "aba aba aba dada dada "
print(txt.count("aba"))

#20



#21
text =  'hello# world!one!kdmc'
separators = [' ', '!', '#', '{']

for i in separators:
    text = text.replace(i, ' ')


#22
txt = 'hello123hello56'
result = 0
sequences = []

for i in text:
    if i.isdigit():
        result += 1
    else:
        if result:
            sequences.append(result)
            result = 0

sequences.append(result)
print(max(sequences))


#23
txt = 'hello123hello56'
result = 0

for i in text:
    if i.isdigit():
        result += int(i)

    print(result)

