from application import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    """
        User Model
        User Role => 0 - Administrator, 1 - User
        Team => 0 - Administrator, 1 - Documentation, 2 - Collections
    """

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(264))
    role = db.Column(db.String(32), nullable=False)

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)

    def set_role(self, role):

        self.role = role

    def change_password(self, old_password, new_password):

        if self.check_password(old_password):
            self.set_password(new_password)

        db.session.add(self)
        db.session.commit()
        db.session.close()


@login_manager.user_loader
def user_loader(user_id):

    return User.query.get(int(user_id))
