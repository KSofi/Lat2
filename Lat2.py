a = {'Jane Doe' : '+27 555 5367', 'John Smith' : '+27 555 6254', 'Bob Stone' : '+27 555 5689'}

a['Jane Doe']='+27 555 1024'

a.keys()
a.values()
a.items()

a['Anna Cooper']='+27 555 3237'

print ('Bob Stone', a['Bob Stone'])

for k in a.keys():
    print (k)

for v in a.values():
    print (v)

for k,v in a.items():
    print (k,v)
