import time

delay = int(input("Digite seu tempo de delay: "))
for i in reversed(range(delay)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("O tempo acabou")

