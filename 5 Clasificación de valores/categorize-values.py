# 5 Clasificación de valores 

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList: 
    print('{} is of the data type {}'.format(item, type(item)))

print(myMixedTypeList[2]);
myMixedTypeList[2] ="nuevo valor"
print(myMixedTypeList[2]);
print(myMixedTypeList);
