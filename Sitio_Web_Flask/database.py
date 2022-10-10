import email
import db
from models import User
from werkzeug.security import generate_password_hash

if __name__=='__main__':
    password = 'darkhokage'
    admin = User(name='Itachi Uchiha',email='LastUchiha@konoha.com',password=generate_password_hash(password, method='sha256'),type_user='administrator')
    db.create_Administrator(admin)
