import os
import random

trainval_percent = 0.3
train_percent = 0.7
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w', encoding='UTF-8')
ftest = open('ImageSets/Main/test.txt', 'w', encoding='UTF-8')
ftrain = open('ImageSets/Main/train.txt', 'w', encoding='UTF-8')
fval = open('ImageSets/Main/val.txt', 'w', encoding='UTF-8')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
