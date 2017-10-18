#developping
class cal:
    def __init__(self, rawdata, openID):
        self.openid = openID
        self.calinfo = []
        while(rawdata.find('\n')!=-1) or len(rawdata) != 0:
            if rawdata.find('\n') == -1:
                temp = rawdata[0:len(rawdata)]
            else:
                temp = rawdata[0:rawdata.find('\n')]
            seq = temp[0:temp.find(',')]
            temp = temp[temp.find(',') + 1:len(temp)]

            item = temp[0:temp.find(',')]
            temp = temp[temp.find(',') + 1:len(temp)]

            time = temp[0:temp.find(',')]
            temp = temp[temp.find(',') + 1:len(temp)]

            place = temp[0:len(temp)]

            #print(seq,item,time,place)
            self.calinfo.append(subcal(seq,item,time,place))

            if rawdata.find('\n')!=-1:
                rawdata = rawdata[rawdata.find('\n')+1:len(rawdata)]
            else:
                rawdata = ''

    def __str__(self):
        result = ''
        n = 0
        while(n < len(self.calinfo)):
            result += self.calinfo[n].testreturn() + '\n'
            n += 1
        return result

class subcal:
    def __init__(self,seqinput,iteminput,timeinput,placeinput):
        self.seq = seqinput
        self.item = iteminput
        self.time = timeinput
        self.place = placeinput

    def __str__(self):
        return self.seq + ' ' + self.item + ' ' + self.time + ' ' + self.place

    def testreturn(self):
        return '#' + self.seq + ' 项目' + self.item + ' 时间代码' + self.time + ' 地点' + self.place

    #def userreturn(self):

    def readabletime(self):
        #时间代码：重复+重复设定+具体时间+t+持续时长
        #时间代码开头：A每日重复；B每周重复；C每月重复；D每年重复；E自定义重复；F不重复
        #时间代码段2：
        return