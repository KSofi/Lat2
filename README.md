## Use python 3.4.2
## Syntax ini menggunakan fungsi dictionary

###### dictionary yang akan dieksekusi
```javascript
a = {'Jane Doe' : '+27 555 5367', 'John Smith' : '+27 555 6254', 'Bob Stone' : '+27 555 5689'}
```
## perintah menambahkan dictionary
``javascript
a['Jane Doe']='+27 555 1024'
```
# program nama dari dictionary yang telah dibuat
```javascript
a.keys()
```
## program isi dari dictionary yang telah dibuat
```javascript
a.values()
```
## program nama dan isi dictionary yang telah dibuat
```javascrip
a.items()
```
## perintah mengganti isi dictionary
```javascript
a['Anna Cooper']='+27 555 3237'
```
## perintah untuk menampilkan salah satu dictionary
```javascript
print ('Bob Stone', a['Bob Stone'])
```
## perintah menampilkan nama dictionary, isi dictionary, serta nama dan isi dictionary secara bersamaan
```javascript
for k in a.keys():
    print (k)

for v in a.values():
    print (v)

for k,v in a.items():
    print (k,v)
```

## demikian sedikit penjelasannya, semoga bermanfaat...
