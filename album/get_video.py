import os
import string
import random

from pytube import YouTube


def get_video(link, user):
    video = YouTube(link)
    title = video.title
    description = video.description
    media = 'user_' + str(user) + '/' + title + '.mp4'
    path = 'files/media/user_' + str(user) + '/'
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    video.download(path, filename='_'.join([path, '_'.join(title.split(' ')), random_string]))
    return [title, description, media]
