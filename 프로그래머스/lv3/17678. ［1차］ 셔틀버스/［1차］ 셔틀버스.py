def solution(n, t, m, timetable):
    answer = ''
    crews_time = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable]
    crews_time.sort()
    bus_time = [9 * 60 + t * i for i in range(n)]
    
    idx = 0
    for bus in bus_time:
        in_cnt = 0
        while in_cnt < m and idx < len(crews_time) and crews_time[idx] <= bus:
            idx += 1
            in_cnt += 1
    answer = bus if in_cnt < m else crews_time[idx - 1] - 1
    
    return f'{str(answer // 60).zfill(2)}:{str(answer % 60).zfill(2)}'