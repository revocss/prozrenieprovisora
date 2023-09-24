class Product:
    def __init__(self, owner):
        self.owner = owner


class Lesson:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration


class UserAccess:
    def __init__(self, user, product):
        self.user = user
        self.product = product


class UserLessonStatus:
    def __init__(self, user, lesson):
        self.user = user
        self.lesson = lesson
        self.viewed_time = 0
        self.status = "не просмотрено"

    def update_viewed_time(self, time):
        self.viewed_time = time
        if self.viewed_time >= 0.8 * self.lesson.duration:
            self.status = "просмотрено"
