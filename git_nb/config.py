class Config:
    def __init__(self, username: str = None, email: str = None, repo_name: str = None):
        self._username = username
        self._repo_name = repo_name
        self._email = email

    @property
    def username(self) -> str:
        if self._username is None:
            print("You have to set an username using cfg.username.")
            assert AttributeError
        return self._username

    @property
    def repo_name(self) -> str:
        if self._repo_name is None:
            print("You have to set a repo_name using cfg.repo_name.")
            assert AttributeError
        return self._repo_name

    @property
    def email(self) -> str:
        if self._repo_name is None:
            print("You have to set an email using cfg.email.")
            assert AttributeError
        return self._email

    @username.setter
    def username(self, username: str):
        self._username = username

    @email.setter
    def email(self, email: str):
        self._email = email

    @repo_name.setter
    def repo_name(self, repo_name: str):
        self._repo_name = repo_name


cfg = Config()
