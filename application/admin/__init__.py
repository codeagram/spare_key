from flask import Blueprint


AdminBP = Blueprint("AdminBP",
                    __name__,
                    template_folder="templates")


from . import routes, models
