from nextdate import *
testcases = [
	(Date_my(2015, 7, 1), Date_my(2015, 7, 2, 3)),
	(Date_my(1999, 12, 31), Date_my(2000, 1, 1, 5))
]
def judge(i, testcase, correctcase, casename):
	if testcase == correctcase:
		print('case' + str(i) + casename + ' test succeed ' + str(testcase))
	else:
		print('case' + str(i) + casename + ' test failed ' + str(testcase) +' '+ str(correctcase))

i = 0
for case in testcases:
	i += 1
	date = nextdate(case[0])
	judge(i, date.year, case[1].year, 'year')
	judge(i, date.month, case[1].month, 'month')
	judge(i, date.day, case[1].day, 'day')
	judge(i, date.week, case[1].week, 'week')
