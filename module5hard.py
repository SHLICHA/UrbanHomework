from time import sleep

class UrTube():
    users = []
    videos = []
    current_user = None

    def log_in(self, login, password):
        user_in = [user for user in self.users if user.nickname == login]
        if user_in == []:
            print('Такого пользователя не существует')
        elif user_in[0].password == hash(password):
            self.current_user = user_in[0]
        else:
            print("Неверный пароль")

    def register(self, login, password, age):
        if [user for user in self.users if user.nickname == login]:
            print(f'Пользователь {login} уже существует')
        else:
            new_user = User(login, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if not [temp for temp in self.videos if temp.title == video.title]:
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user:
            video = [video for video in self.videos if title == video.title]
            if video:
                if video[0].adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for t in range(1, video[0].duration):
                        video[0].time_now = t
                        print(video[0].time_now, end=" ")
                        sleep(1)
                    print("Конец видео")
                    video[0].time_now = 0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")



class Video():
    time_now = 0
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
