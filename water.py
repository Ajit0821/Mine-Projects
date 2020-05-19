import time
from plyer import notification
drink=0
while True:
    left=str(4000-drink)
    drink=200+drink
    notification.notify(
        title='WATER REMAINDER {} ml left to drink'.format(left),
        message='Please Drink Water!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                'Drink 200 ml liter of water',
                #'{} More water to be put inside the belly...'.format(left)
        app_icon='C:/Users/kumar/PycharmProjects/Water_remainder/food.ico',
        timeout=10


    )
    time.sleep(60*30)

