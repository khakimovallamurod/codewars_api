import requests
class User:
    """
    User class
    """
    def __init__(self,username):
       self.data = requests.get(f'https://www.codewars.com/api/v1/users/{username}').json() 

    def check_username(self):
        return self.data['reason']
    def get_total(self):
        return self.data['codeChallenges']
