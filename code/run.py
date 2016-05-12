import os
import time

startPageIdx = 47
maxiter = 1

for i in range(100):
    cmd = "python3 semiAutoCNKICrawler.py " + str(maxiter) + " " + str(startPageIdx)
    os.system(cmd)
    time.sleep(300)
    startPageIdx = startPageIdx + 20
