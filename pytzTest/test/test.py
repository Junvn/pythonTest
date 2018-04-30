# coding:utf-8

__author__ = 'Janvn'

from dateutil import tz
from datetime import datetime,timedelta
import pytz

'''
微信收藏：pytzTest-西方最快的步枪    公众号：python程序员
原文URL: https://blog.ganssle.io/articles/2018/03/pytz-fastest-footgun.html

比较python时区模块：pytz模块和dateutil.tz模块

EST：东部标准时间
DST：夏时制
'''

#python的时区模型
def test_datetime():
    NYC = tz.gettz('America/New_York')    #NYC:  new york city 简称
    print(NYC)
    print(type(NYC))
    dt_spring = datetime(2018,2,14,12,30,30,30,tzinfo=NYC)
    print(dt_spring)  # 2018-02-14 12:30:30.000030-05:00

    dt_summer = dt_spring + timedelta(days=60)
    print(dt_summer)  # 2018-04-15 12:30:30.000030-04:00

    # datetime.tzname()
    # datetime.utcoffset()
    # datetime.dst()


#pytz的时区模型
def test_pytz():
    NYC = pytz.timezone('America/New_York')
    print(NYC)    # America/New_York

    dt=datetime(2018,2,14,12,30,30,30,tzinfo=NYC)
    print(dt)   # 2018-02-14 12:30:30.000030-04:56

    # dt=NYC.localize(datetime(2018,2,14,12,30,30,30))   # 调用本地化函数
    # print(dt)    # 2018-02-14 12:30:30.000030-05:00

    # dt_summer = dt + timedelta(days=60)
    # print(dt_summer)   # 2018-04-15 12:30:30.000030-05:00
    # print(NYC.normalize(dt_summer))   # 2018-04-15 13:30:30.000030-04:00


def test_fuzzyDate():
    NYC = pytz.timezone('America/New_York')
    dt_dst = NYC.localize(datetime(2018,11,4,1,30),is_dst=True)
    print(dt_dst)  # 2018-11-04 01:30:00-04:00

    dt_dts = NYC.localize(datetime(2018,11,4,1,30),is_dst=False)
    print(dt_dts)  # 2018-11-04 01:30:00-05:00

    # NYC_du = tz.gettz('America/New_York')
    # dt_dst = datetime(2018,11,4,1,30,fold=0,tzinfo=NYC_du)
    # print(dt_dst)  # 2018-11-04 01:30:00-04:00
    #
    # dt_dts = datetime(2018,11,4,1,30,fold=1,tzinfo=NYC_du)
    # print(dt_dts)  # 2018-11-04 01:30:00-05:00

#############################################################################################
# 比较dateutil.tz 和 pytz 模块性能
# pytz=2018.4
# python-dateutil=2.7.2

#############################################################################################
# %timeit NYC_p = pytz.timezone('America/New_York')
# #1.7 µs ± 6.21 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit NYC_d=tz.gettz('America/New_York')
# 844 ns ± 5.17 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
#############################################################################################

#############################################################################################
# %timeit dt_p=NYC_p.localize(datetime(2018,11,1))
# 38.7 µs ± 125 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# %timeit dt_d=datetime(2018,11,1,tzinfo=NYC_d)
# 1.5 µs ± 5.11 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
#############################################################################################

#############################################################################################
# %timeit dt_p.utcoffset()
# 662 ns ± 4.71 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit dt_d.utcoffset()
# 13.9 µs ± 212 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#############################################################################################

#############################################################################################
# %timeit NYC_p.localize(datetime(2018,11,1)).utcoffset()
# 39.8 µs ± 396 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# %timeit datetime(2018,11,1,tzinfo=NYC_d).utcoffset()
# 15.8 µs ± 233 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#############################################################################################

#############################################################################################
# LA_p=pytz.timezone('America/Los_Angeles')
# LA_d=tz.gettz('America/Los_Angeles')

# %timeit dt_p.astimezone(LA_p)
# 7.99 µs ± 18.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %timeit dt_d.astimezone(LA_d)
# 32.6 µs ± 80.8 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#############################################################################################
#############################################################################################


def main():
    # test_datetime()
    # test_pytz()
    test_fuzzyDate()


if __name__ == '__main__':
    main()