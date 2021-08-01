from flask import Blueprint


AuthBP = Blueprint("AuthBP",
                    __name__,
                    template_folder="templates")


from . import routes, models
