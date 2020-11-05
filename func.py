'''Helper by Saveliy Burkov is licensed under CC BY-SA 4.0.'''
import data
import datetime




#Дата
today = datetime.datetime.today().strftime('%d.%m.%Y')
todayd = int(datetime.datetime.today().strftime('%d'))
tomorrow = str((todayd)+1) + datetime.datetime.today().strftime('.%m.%Y')
tomorrowd = todayd + 1


#Формирование дежурных и времени
def Dej(day):
    # Первый дежурный

    def Dej1(day):
        if day in [1, 4, 5, 13, 18, 25, 26, 29]:
            d1 = data.HumDej1D
        elif day in [6,  8, 11, 12,  15, 19, 20, 23, 27, 28]:
            d1 = data.HumDej2D
        else:
            d1 = data.HumDej3D

        return d1

    # второй дежурный, если есть

    def Dej2(day):
        if day in [7, 9, 10, 14, 17]:
            d2 = data.HumDej1D
        elif day in [2, 3, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31]:
            d2 = data.HumDej4D
        elif day in [16]:
            d2 = data.HumDej2D
        else:
            d2 = data.NaND

        return d2

    # ночной дежурный

    def Dejn(day):
        if day in [1, 2, 9, 10]:
            d3 = data.HumDej5D
        elif day in [3, 4, 11, 12, 23, 24, 27, 28]:
            d3 = data.HumDej6D
        elif day in [5, 6, 13, 14, 17, 18, 21, 22, 25, 26, 29, 30]:
            d3 = data.HumDej7D
        else:
            d3 = data.HumDej8D

        return d3

    # время смены дневных

    def Dejsm(day):
        if day in [7, 9, 14, 16, 20, 21, 27, 28, 29]:
            timesm = data.t17
        elif day in [1, 4, 5, 6, 8, 11, 12, 13, 15, 18, 19, 25, 26]:
            timesm = data.t20
        elif day in [3, 10, 17, 24, 31]:
            timesm = data.t15
        else:
            timesm = data.t12

        return timesm

    askday = (
        '\n ⌛️ 08:00 - {0} \n {1}  \n\n⌛  {0} - 20:00\n {2} \n\n ⌛ С 20:00 в ночь\n {3}'.format(Dejsm(day),
                                                                                                   Dej1(day),
                                                                                                   Dej2(day),
                                                                                                   Dejn(day)))
    return askday

