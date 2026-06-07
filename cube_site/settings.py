from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'IUIT&TGBUG)&#*VB@(F#)DB@E)'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'cube_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {},
    }
]
