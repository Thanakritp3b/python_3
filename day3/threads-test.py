import threading


def print_number():
    for i in range(10):
        print(i)

def print_letter():
    for i in range(10):
        print(chr(65+i))

a= threading.Thread(target=print_number)
b= threading.Thread(target=print_letter)

a.start()
b.start()

a.join()
b.join()
