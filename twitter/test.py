import re
from datetime import datetime

# test_date = '他的生日是2016-12-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'
test_date = '他的生日是是个可爱的小宝贝.二宝的生日是好可爱的.'

test_datetime = '他的生日是2016-12-12 14:34,是个可爱的小宝贝.二宝的生日是2016-12-21 11:34,好可爱的.'

# date
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})",test_date)
print(mat)
# print (mat.groups())
# # ('2016-12-12',)
# print (mat.group(0))
# # 2016-12-12