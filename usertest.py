from datamodels import  User;
from datamodels import Group;
from dao import UserDAO;

user = User();
user.username="Nilesh";
user.password ="Nilesh";

admin = Group();
admin.addUser(user);
print(user);
userDao = UserDAO();
userDao.save();

