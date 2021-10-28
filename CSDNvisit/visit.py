# from urllib import request
# import time
#
# url = ['https://blog.csdn.net/weixin_42724359/article/details/88564928']
#
# countUrl = len(url)
# count = 0
# count1 = 0
#
# while True:  # 让程序一直执行
#     if count1 < 1000:
#         try:  # 正常运行
#             count = count + 1
#             print(count, 'times')  # 监视程序是否在正常运行，输出运行了多少次
#             for i in range(countUrl):  # 遍历所有url
#                 request.urlopen(url[i])  # 访问网页
#             time.sleep(70)  # 间隔执行
#
#         except Exception:  # 出现异常
#             print('Retry')
#             count1 = count1 + 1
#             time.sleep(70)
#键入终止循环

flag = 1
count = 0
while count < 10 and flag:
    print(count)
    count += 1
    flag = input("input flag:")