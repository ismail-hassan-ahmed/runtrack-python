tab = {'zor' : 40, 'blog' : 35, 'zorus' : 52, 'zozor' :66, 'orzo' : 82, 'zozr' : 83,'rozr' : 94, 'zorzo' : 92,'rozoz' : 99}
new_result = {}
for key, data in tab.items():
    if(data < 40):
        print(key + ' : ' + str(data) + ' test echoué')
    else:
        #inf
        # if data % 5 == 1:
        #     data = data -1
        # if data % 5 == 2:
        #     data = data -2
        #sup
        if data % 5 == 3:
            data = data + 2
        if data % 5 == 4:
            data = data + 1
        
        print( key + ' : ' + str(data) + ' test réussi')



print(81%5)
print(82%5)
print(83%5)
print(84%5)