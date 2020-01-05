import os
import string
import random

from pytube import YouTube


def generate_unique_filename(title):
    """
    Generate unique filename adding random string
    :param title: original video title
    :returns: generated filename
    """
    random_string = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(10))
    filename = '_'.join(['_'.join(title.split(' ')), random_string])
    return filename


def get_video(link, user):
    """
    Download video using provided link to local user's directory
    :param link: path to media directory
    :param user: user who made request
    :returns: list with video information(title, description, path_to_media)
    """
    path = f'files/media/user_{user}'
    # Create user folder if not exists
    if not os.path.exists(path):
        os.makedirs(path)

    video = YouTube(link)
    title = video.title
    description = video.description

    filename = generate_unique_filename(title)
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first()
    video.download(path, filename=filename)

    path_to_media = f'user_{user}/{filename}.mp4'
    return [title, description, path_to_media]
