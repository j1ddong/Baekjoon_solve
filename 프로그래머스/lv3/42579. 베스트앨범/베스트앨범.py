def solution(genres, plays):
    answer = []
    genres_dict = dict()  # {'classic': 1450, 'pop': 3100}
    genres_play = dict()
    for i in range(len(genres)):
        if genres_dict.get(genres[i]):
            genres_dict[genres[i]] += plays[i]
            genres_play[genres[i]].append((plays[i], i))
        else:
            genres_dict[genres[i]] = plays[i] 
            genres_play[genres[i]] = [(plays[i], i)]
    genres_dict = sorted(genres_dict, key=lambda item: genres_dict[item], reverse=True)
    for genre in genres_dict:
        temp_list = sorted(genres_play[genre], key=lambda x: (x[0], -x[1]), reverse=True)[:2]
        for elem in temp_list:
            answer.append(elem[1])
    return answer

