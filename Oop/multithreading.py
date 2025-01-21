import threading
import time


def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_thrash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You got the mail")

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_thrash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")