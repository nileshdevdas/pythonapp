class User:
    """
        User data model class
        hold username and password and domain
    """
    def __init__(self):
        """
        constructor
        intitializes empty username and password
        :param self:
        :return:
        """
        self.username = None;
        self.password = None;
        self.domain = None;

    def __repr__(self):
        if self.username is not None and self.password is not None:
            return self.username + "," + self.password;
        else:
            return "Empty User";

    

    def __validate(self):
        """
        Interanal validation functionality
        :param self:
        :return:
        """
        if self.username == None:
            raise Exception("Username cannot be None");
        if self.password == None:
            raise  Exception ("Password");
            
