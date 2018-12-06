import os
import string
import random

from pytube import YouTube


def get_video(link, user):
    video = YouTube(link)
    path = 'files/media/user_' + str(user) + '/'
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    title = video.title
    description = video.description
    media = 'user_' + str(user) + '/' + '_'.join(['_'.join(title.split(' ')), random_string]) + '.mp4'
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    video.download(path, filename='_'.join(['_'.join(title.split(' ')), random_string]))
    return [title, description, media]
