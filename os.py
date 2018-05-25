from file_system import FileSystem
from user import User

class OS:


    def __init__(self):
        self.open_files_table = {}
        self.process_files_table = {}
        self.users = set()
        self.system_user = User()
        self.users.add(self.system_user)
        self.root_file_system = FileSystem()

    def new_user(self):
        user = User()
        self.users.add(user)
        return user

    def open(self, file_name, mode):
        pass

    def close(self, file_name):
        pass
