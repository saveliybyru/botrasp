'''Helper by Saveliy Burkov is licensed under CC BY-SA 4.0.'''

import datetime


#Date
today = datetime.datetime.today().strftime('%d.%m.%Y')
todayd = int(datetime.datetime.today().strftime('%d'))
tomorrow = str((todayd)+1) + datetime.datetime.today().strftime('.%m.%Y')
tomorrowd = todayd + 1


#Time
t12 = str('12:00')
t15 = str('15:45')
t17 = str('17:00')
t20 = str('20:00')


class DutyOperator(object):
    '''This class generate structured data for operator'''
    def __init__(self, name, number, messenger):
        self.name = name
        self.number = number
        self.messenger = messenger

    def dater(self):
        data = self.name + '\n' + self.messenger + '\n' + str(self.number)
        return data

Operator=DutyOperator('FirstName', 'Number', 'AnyMessenger')


#Generated list operator's
def Dej(day):

    first=Dej1(day)
    second=Dej2(day)
    night=Dejn(day)
    time=Dejsm(day)

    askday = (
        '\n ⌛️ 08:00 - {0} \n {1}  \n'
        '\n⌛  {0} - 20:00\n {2} \n'
        '\n ⌛ С 20:00 в ночь\n {3}'.format(time, first,
                                           second, night))
    return askday

def Dej1(day):
    if day in [1, 4, 5, 13, 18, 25, 26, 29]:
        d1 = Operator.dater()
    elif day in [6,  8, 11, 12,  15, 19, 20, 23, 27, 28]:
        d1 = Operator.dater()
    else:
        d1 = Operator.dater()
    return d1

def Dej2(day):
    if day in [7, 9, 10, 14, 17]:
        d2 = Operator.dater()
    elif day in [2, 3, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31]:
        d2 = Operator.dater()
    elif day in [16]:
        d2 = Operator.dater()
    else:
        d2 = Operator.dater()
    return d2

def Dejn(day):
    if day in [1, 2, 9, 10]:
        d3 = Operator.dater()
    elif day in [3, 4, 11, 12, 23, 24, 27, 28]:
        d3 = Operator.dater()
    elif day in [5, 6, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30]:
        d3 = Operator.dater()
    else:
        d3 = Operator.dater()
    return d3

def Dejsm(day):
    if day in [7, 9, 14, 16, 20, 21, 27, 28, 29]:
        timesm = t17
    elif day in [1, 4, 5, 6, 8, 11, 12, 13, 15, 18, 19, 25, 26]:
        timesm = t20
    elif day in [3, 10, 17, 24, 31]:
        timesm = t15
    else:
        timesm = t12
    return timesm
