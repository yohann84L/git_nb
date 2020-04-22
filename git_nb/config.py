class Config:
    def __init__(self, username: str = None, email: str = None, repo_name: str = None):
        self._username = username
        self._email = email
        self._repo_name = repo_name

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def repo_name(self):
        return self._repo_name