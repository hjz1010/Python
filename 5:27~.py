#5/27

_input = input().split(" ")
n = int(_input[0])
_list = _input[1:]
new_list = _list[(-1*n):] + _list[:(-1*n)]
print(" ".join(new_list))


import datetime
_input = input("")
result = 0
with open('timelog.txt','r') as timelog:
       for time in timelog:
           time_list = time.strip('\n').split(" ")
           time1 = datetime.datetime.strptime(time_list[0],'%H:%M:%S').timestamp()
           time2 = datetime.datetime.strptime(time_list[1],'%H:%M:%S').timestamp()
           input_time = datetime.datetime.strptime(_input,'%H:%M:%S').timestamp()

           if time1 - input_time < 0 and input_time - time2 < 0:
               result += 1
print("%s명이 사무실에 있습니다." %result)

_input = input("")
result = 0
with open('timelog.txt','r') as timelog:
       for time in timelog:
           time_list = time.strip('\n').split(" ")
           time1 = "".join(time_list[0].split(":"))
           time2 = "".join(time_list[1].split(":"))
           input_time = "".join(_input.split(":"))

           if time1 < input_time and input_time < time2:
               result += 1
print("%s명이 사무실에 있습니다." %result)
