#coding=utf-8
import math


long_year_day = 366
short_year_day = 365

gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
yue = ['正', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '腊',]

long_year_mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
short_year_mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_dict_en = {
	'0':'monday',
	'1':'tuesday',
	'2':'wednesday',
	'3':'thursday',
	'4':'friday',
	'5':'saturday',
	'6':'sunday',
}

week_dict_ch = {
	'0':'周一',
	'1':'周二',
	'2':'周三',
	'3':'周四',
	'4':'周五',
	'5':'周六',
	'6':'周日',	
}

class Date_my(object):
	"""docstring for Date_my"""
	def getLunarYear(self, year):
		return (year - 1864)%60

	def __init__(self, year,month,day,week=0,lunar_month=0,lunar_day=0):
		self.year = int(year)
		self.month = int(month)
		self.day = int(day)
		self.week = int(week)
		self.lunar_year = self.getLunarYear(year)
		self.lunar_month = int(lunar_month)
		self.lunar_day = int(lunar_day)

	def p(self):
		print(date.year, 'year', date.month, 'month', date.day, 'day', week_dict_en[str(int(date.week))])
		print('lunar:',gan[date.lunar_year%10]+zhi[date.lunar_year % 12]+'年', yue[date.lunar_month-1]+'月', str(date.lunar_day)+'日')


def getJieQi(year, count):
	year -= 1900 if year > 1900 else 0
	return 365.242 * year + 6.2 + 15.22 * count - 1.9 * math.sin(0.262 * count)  

def getLunarValues(year, month, day):
	return gan[year % 10]+zhi[year % 12]+'年', yue[month-1]+'月', str(day)+'日'

def getWeekValues(week, chinese=True):
	return week_dict_ch[str(week)] if chinese else week_dict_en[str(week)]

def getShuoRi(m):
	return 1.6 + 29.5306*m + 0.4 * math.sin(1 - 0.45058 * m)

def getShuoYue(day):
	# print(day)
	m = int((day -1.6)/29.5306) + 1
	# print(m)
	while int(day) < int(getShuoRi(m)):
		m -= 1
	return m

def calculateLunar_month_and_day(year, day):
	dongzhi_pre = getJieQi(year - 1, 23)#dong zhi
	m = getShuoYue(dongzhi_pre)
	# print(dongzhi_pre, m, year, day, '!fuck!', getShuoRi(m))
	jieqi = 0
	month = 10
	m += 1
	# print(day - getShuoRi(m))
	while day > int(getShuoRi(m)):
		m += 1
		if getJieQi(year, jieqi) < getJieQi(year, jieqi + 1):
			month += 1
		# print(month)
		month %= 12
		jieqi += 2

	return month + 1, day - int(getShuoRi(m-1)+0.2)

def convertDateToDaynum(date):
	year = date.year
	month = date.month
	day = date.day
	yearnum = year - 1900 - 1
	long_year_num = yearnum/4 + 1
	short_year_num = yearnum - long_year_num + 1
	# print(long_year_num, short_year_num)
	day += long_year_num*long_year_day + short_year_num*short_year_day
	# print(day)
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		month -= 2
		while month >= 0:
			day += long_year_mon[month]
			month -= 1
	else :
		month -= 2
		while month >= 0:
			day += short_year_mon[month]
			month -= 1
	# print(day)
	return day

def convertDaynumToDate(day):
	month = 0
	week = (day + 5)% 7
	year  = 1900 + 4 * int(day / (3*short_year_day + long_year_day))
	tmp_day = day
	# print(year)
	# print(day)
	day %= (3*short_year_day + long_year_day)
	# print(day)
	if day < long_year_day:
		while day >= long_year_mon[month]:
			day -= long_year_mon[month]
			month += 1
		month += 1
	else :
		day -= long_year_day
		year += 1
		while day >= short_year_day:
			day -= short_year_day
			year += 1
		while day >= short_year_mon[month]:
			day -= short_year_mon[month]
			month += 1
		month += 1
	lunar_month, lunar_day = calculateLunar_month_and_day(year, tmp_day)
	date = Date_my(year, month, day, week, lunar_month, lunar_day)
	# print(date.lunar_month, date.lunar_day)
	return date

def nextdate(date):
	return convertDaynumToDate(convertDateToDaynum(date)+1)


if __name__ == "__main__":
	year  = int(input('year:'))
	month = int(input('month:'))
	day   = int(input('day:'))
	date = nextdate(Date_my(year, month, day))
	date.p()