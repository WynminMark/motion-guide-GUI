import time

dt_s = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
f = open(dt_s + ".txt", "w")
f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
f.close()




