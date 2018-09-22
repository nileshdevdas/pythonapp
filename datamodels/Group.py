from datamodels.User import User;
class Group:
    """ Group class"""
    def __init__(self):
        """ Group Constructor"""
        self.groupName = None;
        self.groups = [];

    def addUser(self, user):
        self.groups.append(user);


    def listUser(self):
        return self.groups;