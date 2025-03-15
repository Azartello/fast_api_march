import os
from pathlib import Path
from .img_extension import IMG_EXTENSION_LIST
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


SECRET_KEY = b"SECRET_KEY"
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./site.db'

ROOT_URL = Path(__file__).resolve().parent.parent
MEDIA_URL = os.path.join(ROOT_URL, 'media')
templates = Jinja2Templates(directory="templates")


TemplateResponse = templates.TemplateResponse


mail_conf = ConnectionConfig(
    MAIL_USERNAME="timuhinasofa",
    MAIL_PASSWORD="ваш пароль gmail",
    MAIL_FROM="timuhinasofa@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="FastAPI",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
