from functools import wraps

from flask import jsonify, request, url_for
from flask_jwt_extended import jwt_required, get_jwt, verify_jwt_in_request

from app import db
from app.api import bp
from app.models import User, Flag
from app.api.errors import bad_request, not_found


def jwt_user_required(f):
    @wraps(f)
    def decorated_function(uid, *args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get('is_admin', False):
            return f(uid, *args, **kwargs)
        elif claims.get('id') == int(uid):
            return f(uid, *args, **kwargs)
        else:
            return jsonify(msg="Permission denied"), 403
    return decorated_function


def jwt_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("is_admin", False):
            return f(*args, **kwargs)
        else:
            return jsonify(msg="Permission denied. Admin only"), 403

    return decorated_function


@bp.route('/users/<uid>', methods=['GET'])
@jwt_required()
def get_user(uid):
    user = db.engine.execute(f'SELECT * FROM "web-user" WHERE id = ' + uid)
    results = user.fetchone()
    if results is None:
        return bad_request(f'User with id \'{uid}\' not found')
    data = {
        '_links': {
            'flags': f'/api/users/{uid}/flags',
            'self': f'/api/users/{uid}'
        },
        'email': results['email'],
        'id': results['id'],
        'username': results['username']
    }
    return jsonify(data)


@bp.route('/users/<int:uid>/flags', methods=['GET'])
@jwt_user_required
def get_user_flags(uid):
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    user = User.query.get_or_404(uid)
    data = User.to_collection_dict(user.flags, page, per_page, 'api.get_user_flags', uid=uid)
    return jsonify(data)


@bp.route('/users/<int:uid>/flags/<int:fid>', methods=['GET'])
@jwt_user_required
def get_user_flag(uid, fid):
    user = User.query.get_or_404(uid)
    flag = Flag.query.get_or_404(fid)
    if flag.user_id == user.id:
        return jsonify(flag.to_dict())
    return bad_request('Permission denied')


@bp.route('/users/<int:uid>/flags', methods=['POST'])
@jwt_user_required
def create_flag(uid):
    flag = request.values.get('flag')
    user = User.query.get_or_404(uid)
    if flag is None:
        return bad_request('Flag cannot be empty')
    if Flag.query.filter_by(name=flag).first():
        return bad_request('Such flag already exists')

    flag = Flag(name=flag, user=user)
    db.session.add(flag)
    db.session.commit()
    response = jsonify(flag.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user_flag', uid=user.id, fid=flag.id)
    return response


@bp.route('/flags/<int:fid>', methods=['GET'])
@jwt_admin_required
def get_flag(fid):
    return jsonify(Flag.query.get_or_404(fid).to_dict())


@bp.route('/flags/', methods=['GET'])
@jwt_admin_required
def get_flags():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return jsonify(Flag.to_collection_dict(Flag.query, page, per_page, 'api.get_flags'))


@bp.route('/users/', methods=['GET'])
@jwt_admin_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return jsonify(User.to_collection_dict(User.query, page, per_page, 'api.get_users'))
