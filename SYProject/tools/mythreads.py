# -*- coding: utf-8 -*-
"""
@Description : 
@File        : mythreads.py
@Project     : SYProject
@Time        : 2021/8/31 上午11:31
@Author      : dj
@Software    : PyCharm
"""

import threading
import time
import requests
import json

exitFlag = 0

#并发极速问诊医生接诊
class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        # self.counter = counter
        self.url = 'https://test2a.everjiankang.cn/api-ih/titan-cms/titan-cms-speed/race_answer'
        self.hearders = {"Content-Type": "application/json",
                         "x-access-token": "ODn6jPzGEabeP7ajlk5oCYbj0j4iCL5NSsmNLSCBZu8ht23sS4z/ukw1E+QCtz9LoE9XbG84QhtfUuOTWh15xkl7lZaOYGnxC70BPUE9ES8+TVZfbzgzv4AO4QWvXxOPzc/daIYyaFEv3SEEoSJuQuBT0ClFn7kOIuhyRwFdf3U=,AkGq74MXQ8HjM7GjQRpVVCnEjO5IblreJ5Eikun7VC0EwI9s2eeBN/jEaTyVOeOQ4ZlM7FfOSyCQxTeT5SZL3Q2oAFlqbNae5jMZJ0g+7i+LsXE31+NBBH+GsoSZDZIlQSifVSThqjmmeW6KFAsGkVH29aU0HfvKrZdknXlQVa8=,dc8qm6jhpUw043rqU7SSPKerj/go7fAIlApC8T8OszUCnLWkB2OsI189NvkHUJXjkAOSiAQRPaykuzJeSBzxSX17FzKoZp4o3ICWB1drnTfw7AvsGujj+KJNcxa1oe4Of5k/xBKWnu0D5GKT8OmgRYAoKvJeJL5cLrW8M2AmELE=,Gh1J7VcGAZCzQhx50tB7l59VDc4u8VNeeOY59R0CWeU9Gb41qftiLwzQjIPOL6emjrTGQ8MiJZzL8OwPczlypl6MVNM9lq3rQ1hpPiCfn/AjJEJE7PwzQGiHheo/+ISIsWiuSQxgAPvmW3zJzfMdJEn9TPiZ5nseL3UtQsJ1wJ0=,L6SkpFaKYchoONCxRAM9FSNnXlkUdFAVsC0Cef2k2qc58oKLLd+nPU2kxpzZ9VahcQKPtnsjOF3k1PjeMFGaII9kDMjkzMbjz7bRngm1MDk7KIV+ovS9lXUiLEaCUeL4fFGiMHsDP00vc16xjKgDfjXAlAp7+VtaUMrCpAHbS38="}
        self.data = {"id": "762e516939c74221b0b49fa0d985df19"}

    def run(self):
        self.wenzhen(self.name, 2)

    def wenzhen(self, threadName, counter):
        if threadName == 'Thread-1':
            self.hearders['x-access-token'] = 'f+A01jGoYfSjDUcBwYEmWaP3AzFZNsaGeNbGWemQ3+D/p/gFBboUqreWoW9XHPxvHvdvscUaojUSV2MLenPwclqBeC37JSynTJrN3PuTlsOwhA7CLK7BjkCwYJVk8R0j6mNSepX315hlfb3HcVXIfq2MMUZn92PpJKLkn+XgZso=,MUTFUxLWBx8f9dIdl4cddRax+t7RAY4o+fJVl7Oj5/Xk5etG60Lnu2z1BopFxOvU3NIw7cAzNv2S4VsYkzxonqNB8DvMFdSYp8fMe+IA59ARp42hhMWAf5bykbVOk+QfLxXfdMMbWfFdu00NNqZeKPdZBmaMb0Il+O6VxnlqScQ=,YbCQMd9jqKOjylAG4Pbxrezl1+Pak3RSTIAufQ6Jbuu+u1/bU68lux3B5mLDH2XUiIIdig6LLXz95fPn3WsHs3RL31zlEzSvnQYppcqoTCb3GdOhldpfPi2AKlK8M7mvEgAXD5HIqGO/ncn2kC78E1Zld3isz4MmG+uzKDS5CWI=,O2BZPIa/Wp2SyylPkZiJIAX27x4DA8uVejlfK60s6z9KIujlkgOx45ush09EExAYQS7TBrRdNSaJUrluu0OQALirvlzqgZW0Jp3/kxXNSc2zl1pziEVYw9u0MV57Z9opjMkFcDTj6d6K0DzopiVtKFk5Bo+DEo7PUPrKDze16M4=,VkTBpfeDpK+RS7+RVzga0bOiUFfV3vqi/Rkut8n3YGq57SHJ0AYZxvwwfwh4SM6Pue8FCqvNBwFEy5W5VQqqhPF1oLVRC3clBcVPxmyppP5rSSuFAb2e/LwJxKbYJ3Ibs+DMey6LsRtVr59qOvbZHEvUOofGi1H1B9+WuXPD+NE='
            while counter:
                res = requests.post(url=self.url, headers=self.hearders, data=json.dumps(self.data))
                print(res.text)
                print("%s: %s" % (threadName, time.ctime(time.time())))
                counter -= 1

        elif threadName == 'Thread-2':
            self.hearders['x-access-token'] = 'f+A01jGoYfSjDUcBwYEmWaP3AzFZNsaGeNbGWemQ3+D/p/gFBboUqreWoW9XHPxvHvdvscUaojUSV2MLenPwclqBeC37JSynTJrN3PuTlsOwhA7CLK7BjkCwYJVk8R0j6mNSepX315hlfb3HcVXIfq2MMUZn92PpJKLkn+XgZso=,MUTFUxLWBx8f9dIdl4cddRax+t7RAY4o+fJVl7Oj5/Xk5etG60Lnu2z1BopFxOvU3NIw7cAzNv2S4VsYkzxonqNB8DvMFdSYp8fMe+IA59ARp42hhMWAf5bykbVOk+QfLxXfdMMbWfFdu00NNqZeKPdZBmaMb0Il+O6VxnlqScQ=,YbCQMd9jqKOjylAG4Pbxrezl1+Pak3RSTIAufQ6Jbuu+u1/bU68lux3B5mLDH2XUiIIdig6LLXz95fPn3WsHs3RL31zlEzSvnQYppcqoTCb3GdOhldpfPi2AKlK8M7mvEgAXD5HIqGO/ncn2kC78E1Zld3isz4MmG+uzKDS5CWI=,O2BZPIa/Wp2SyylPkZiJIAX27x4DA8uVejlfK60s6z9KIujlkgOx45ush09EExAYQS7TBrRdNSaJUrluu0OQALirvlzqgZW0Jp3/kxXNSc2zl1pziEVYw9u0MV57Z9opjMkFcDTj6d6K0DzopiVtKFk5Bo+DEo7PUPrKDze16M4=,VkTBpfeDpK+RS7+RVzga0bOiUFfV3vqi/Rkut8n3YGq57SHJ0AYZxvwwfwh4SM6Pue8FCqvNBwFEy5W5VQqqhPF1oLVRC3clBcVPxmyppP5rSSuFAb2e/LwJxKbYJ3Ibs+DMey6LsRtVr59qOvbZHEvUOofGi1H1B9+WuXPD+NE='
            while counter:
                res = requests.post(url=self.url, headers=self.hearders, data=json.dumps(self.data))
                print(res.text)
                print("%s: %s" % (threadName, time.ctime(time.time())))
                counter -= 1

        else:
            while counter:
                res = requests.post(url=self.url, headers=self.hearders, data=json.dumps(self.data))
                print(res.text)
                print("%s: %s" % (threadName, time.ctime(time.time())))
                counter -= 1


threadList = ["Thread-1", "Thread-2", "Thread-3"]
threads = []
num = 1

for tName in threadList:
    thread = myThread(num, tName)
    thread.start()
    threads.append(thread)
    num += 1

for t in threads:
    t.join()
