#использование %
print('Количество участников команды %(team1_num)s !:' % {'team1_num': 5})
print('Количество участников в обеих командах %(team1_num)s и %(team2_num)s !' % {'team1_num': 5, 'team2_num': 6})

#использование .format()
print('Количество задач, решенных командой 2 {score_2}'.format(score_2=42))
print('время, за которое команда 2 решила задачи {team_time}'.format(team_time=18015.2))

#использоваине f-строк
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
time_avg = 45.2
if score1 > score2 or (score1 == score2 and team1_time > team2_time):
    result = "победа команды Мастер кода"
elif score1 < score2 or (score1 == score2 and team1_time < team2_time):
    result = "победа команды Волшебники данных"
else:
    result = "Ничья"
print(f'Количество решенных задач по командам: {score1} и {score2}')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {score1 + score2} задач, в среднем по {time_avg} секунды за задачу!')