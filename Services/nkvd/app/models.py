from datetime import datetime

from flask import url_for
from flask_login import UserMixin
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class User(UserMixin, PaginatedAPIMixin, db.Model):
    __tablename__ = "web-user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    flags = db.relationship('Flag', backref='user', cascade='all,delete', lazy='dynamic')

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def create_token(self) -> None:
        return create_access_token(self.username, additional_claims={"is_admin": False, 'id': self.id})

    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'email': self.email,
            'id': self.id,
            '_links': {
                'self': url_for('api.get_user', uid=self.id),
                'flags': url_for('api.get_flags', fid=self.id)
            }
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Flag(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('web-user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            'flag': self.name,
            'created_at': self.created_at.isoformat() + 'Z',
            'id': self.id,
            '_links': {
                'self': url_for('api.get_flag', fid=self.id),
                'user': url_for('api.get_user', uid=self.user_id)
            }
        }
