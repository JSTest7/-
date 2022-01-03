import time

start = time.time()

x = 1.0015

average_list = []

price_list = []

import winsound

import csv

with open("D:/My Documents/Desktop/5yearsBTC1000data.csv", 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    list_of_rows = list(csv_reader)

a = len(list_of_rows)
for i in range(a):
    price_list.extend(list_of_rows[i])

mission_fail = 0

trash = 0

minute3 = 0
minute5 = 0
minute10 = 0
minute30 = 0
hour1 = 0
hour3 = 0
hour6 = 0
halfday = 0
day1 = 0
day3 = 0
day7 = 0
day15 = 0
month1 = 0
month3 = 0
month6 = 0
year1 = 0

for i in range(int(len(price_list) / 2)):
    j = 0
    if (i % 15 != 0):
        trash += 1
    else:
        print(round(100 * i / (int(len(price_list) / 2)), 3), '%', round((time.time() - start), 2), 'sec')
    while j <= (int(len(price_list) / 2) - 1 - i):
        if float(price_list[2 * i]) * x > float(price_list[2 * (i + j + 1) - 1]):
            if (j == int(len(price_list) / 2) - 1 - i):
                average_list.append(j)
                mission_fail += 1
                break
            else:
                j += 1
        else:
            average_list.append(j)
            break

print(average_list)

start2 = time.time()

for i in range(len(average_list)):

    if (i % 15 != 0):
        trash += 1
    else:
        print('두번째 진행중' ,round(100 * i / (len(average_list)), 3), '%', round((time.time() - start2), 2), 'sec')

    if float(average_list[i]) >= 525600:

        year1 += 1
        month6 += 1
        month3 += 1
        month1 += 1
        day15 += 1
        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 259200:

        month6 += 1
        month3 += 1
        month1 += 1
        day15 += 1
        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 129600:

        month3 += 1
        month1 += 1
        day15 += 1
        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 43200:

        month1 += 1
        day15 += 1
        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 21600:

        day15 += 1
        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 10080:

        day7 += 1
        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 4320:

        day3 += 1
        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 1440:

        day1 += 1
        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 720:

        halfday += 1
        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 360:

        hour6 += 1
        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 180:

        hour3 += 1
        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 60:

        hour1 += 1
        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 30:

        minute30 += 1
        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 10:

        minute10 += 1
        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 5:

        minute5 += 1
        minute3 += 1

    elif float(average_list[i]) >= 3:

        minute3 += 1

    else:
        trash += 1

print(100 * x - 100, '%의 이익을 얻는데에')

print('평균', sum(average_list) / (len(average_list)), '분 걸림')

print('전략이', mission_fail, '번 실패함')

print('3분 이상 걸린 케이스는', minute3, '건, 전체의', round(100 * minute3 / (len(average_list)), 2), "%")

print('5분 이상 걸린 케이스는', minute5, '건, 전체의', round(100 * minute5 / (len(average_list)), 2), "%")

print('10분 이상 걸린 케이스는', minute10, '건, 전체의', round(100 * minute10 / (len(average_list)), 2), "%")

print('30분 이상 걸린 케이스는', minute30, '건, 전체의', round(100 * minute30 / (len(average_list)), 2), "%")

print('1시간 이상 걸린 케이스는', hour1, '건, 전체의', round(100 * hour1 / (len(average_list)), 2), "%")

print('31시간 이상 걸린 케이스는', hour3, '건, 전체의', round(100 * hour3 / (len(average_list)), 2), "%")

print('6시간 이상 걸린 케이스는', hour6, '건, 전체의', round(100 * hour6 / (len(average_list)), 2), "%")

print('12시간 이상 걸린 케이스는', halfday, '건, 전체의', round(100 * halfday / (len(average_list)), 2), "%")

print('1일 이상 걸린 케이스는', day1, '건, 전체의', round(100 * day1 / (len(average_list)), 2), "%")

print('3일 이상 걸린 케이스는', day3, '건, 전체의', round(100 * day3 / (len(average_list)), 2), "%")

print('7일 이상 걸린 케이스는', day7, '건, 전체의', round(100 * day7 / (len(average_list)), 2), "%")

print('15일 이상 걸린 케이스는', day15, '건, 전체의', round(100 * day15 / (len(average_list)), 2), "%")

print('1달 이상 걸린 케이스는', month1, '건, 전체의', round(100 * month1 / (len(average_list)), 2), "%")

print('3달 이상 걸린 케이스는', month3, '건, 전체의', round(100 * month3 / (len(average_list)), 2), "%")

print('6달 이상 걸린 케이스는', month6, '건, 전체의', round(100 * month6 / (len(average_list)), 2), "%")

print('1년 이상 걸린 케이스는', year1, '건, 전체의', round(100 * year1 / (len(average_list)), 2), "%")

print('걸린 시간은', round((time.time() - start), 3), '초 입니다.')

print('총', (len(average_list)), '번의 테스트')

fileName = '{}_5yearsdata.csv'.format(x)

with open('D:/My Documents/Desktop/'+fileName, 'w') as file:

    write = csv.writer(file)
    write.writerow(average_list)

winsound.Beep(440,2000)