from flask import Blueprint

appBlueprint("home",__name__)

@appBlueprint.route("/")
def index():
    return "Hello, I am Flask Application."