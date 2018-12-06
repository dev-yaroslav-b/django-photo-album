# Photo album app created using Django
It allows you:
1. Create post with media files(Images, Videos)
2. Edit or Delete your posts
3. Share YouTube videos via link

You can try it!
http://devyab.pythonanywhere.com/

## Installation
Clone repo:
```
git clone https://github.com/dev-yaroslav-b/Django-PhotoAlbum.git
```
Create virtual env:
    cd Django-PhotoAlbum
    virtualenv --python=python3.6 venv
Activate venv:
  source venv/bin/activate
Install requirements:
  pip install -r requirements.txt 
Make migrations:
  ./manage.py makemigrations
  ./manage.py migrate
Start server:
  ./manage.py runserver
