from sqlalchemy.orm import sessionmaker 
from app import session
from app.session import engine
from app.models import User
import random

Session = sessionmaker(bind=engine)
session = Session

usernames = ['Ken', 'Josh', 'Mike']

if __name__ == '__main__':
    session.query(User).delete()

    print('SEEDING USERS')
    users = []
    for i in range(3):
        new_username = User(user_name=random.choice(usernames))
    
    session.add(new_username)
    session.commit()

    print('**done**')

