import os
from flask import Flask

def crate_app():
    app Flask(__name__)

    from . import app_01_home
    app.register_blueprint(app_01_home.appBlueprint)
    
    return app