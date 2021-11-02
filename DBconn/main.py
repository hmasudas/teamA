from DBconn.member import *
from DBconn.DBconn import session

user = User()
for i in range(0,50):
    user = dict()
    user['id'] = '1'
    user['name'] = '麻生花子'
    user['age'] = 25
session.add(user)

session.commit()