from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
import os
import config

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(config.test_config_name
                       or 'config.DevelopementConfig')

# инициализирует расширения
db = SQLAlchemy(app)

if True:
    from . import views
# from . import forum_views
# from . import admin_views
