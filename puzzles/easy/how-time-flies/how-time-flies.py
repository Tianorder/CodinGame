from datetime import datetime

# the standard input according to the problem statement.
begin = input()
end = input()

date_format = "%d.%m.%Y"
date1 = datetime.strptime(begin, date_format)
date2 = datetime.strptime(end, date_format)

# 计算年份差距
year_diff = date2.year - date1.year

# 计算月份差距
if date2.month >= date1.month:
    month_diff = date2.month - date1.month
else:
    month_diff = 12 + date2.month - date1.month
    year_diff -= 1
if date2.day < date1.day:
    month_diff -= 1

# 计算天数差距
day_diff = (date2 - date1).days

# 输出结果
if year_diff > 1:
    print(f"{year_diff} years, ", end = "")
elif year_diff == 1:
    print(f"{year_diff} year, ", end = "")
if month_diff > 1:
    print(f"{month_diff} months, ", end = "")
elif month_diff == 1:
    print(f"{month_diff} month, ", end = "")
if day_diff == 1:
    print(f"total {day_diff} day")
else:
    print(f"total {day_diff} days")
