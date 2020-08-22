import datetime


def convert_time(str_time):
    return datetime.datetime.strptime(str_time, '%H:%M:%S')


if __name__ == '__main__':
    target_time = convert_time(input())
    result = 0
    with open('time_data.txt', 'r') as file:
        for line in file:
            timeline = list(map(convert_time, line.split()))
            if len(timeline) == 2:
                if timeline[0] <= target_time <= timeline[1]:
                    result += 1
    print(f'해당시간에 사무실 총 인원은 {result}명 입니다.')