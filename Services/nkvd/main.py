from app import app, db
from app.models import User, Flag


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Flag': Flag}

# app.run(host='127.0.0.1', port=5001)

