from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "*** Drink Water ***",
            message = "Water is important",
            app_icon = "E:/Programming/Full_Stack_Python/Python-Projects/11Asset 1.ico",
            timeout = 5)
        time.sleep(10)