# -*- coding: utf-8 -*-
"""
@Description : 
@File        : demo.py
@Project     : SYProject
@Time        : 2021/9/4 下午5:23
@Author      : dj
@Software    : PyCharm
"""

import pandas as pd
import pytest
li = [1,2,23]

class test:


    def test_001(self):
        # global li
        li.extend([1,2,3])
        print("li= "+str(li))

    @pytest.mark.parametrize('id',li)
    def test_002(self,id):
        print(id)

    print("li是："+str(li))


if __name__ == '__main__':
    # test().test_002()
    a = [1,3,4,5,6]
    b = ["A","b","c","d","e"]
    df1 = pd.DataFrame(data=a,index=b,columns=[""])
    print(df1)
    r = []
    r.append(b)
    r.append(a)
    print(r)
    re = list(map(list, zip(*r)))
    df = pd.DataFrame(re)
    print(df)
