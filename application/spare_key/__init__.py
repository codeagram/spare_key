from flask import Blueprint


SpareKeyBP = Blueprint("SpareKeyBP", __name__,
                        template_folder="templates",
                        static_folder="static")


from . import routes
