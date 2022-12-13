import requests


class Trivia:
    

    def __init__(self, amount: int = 10) -> None:
        '''general function:Creating an object of the api to make certain calls
        args:(string) allows the url to be a string
        return:None'''

        self.url: str = f"https://opentdb.com/api.php?amount={amount}"

    def get(self) -> str:
        '''general function:Calling the api with the request
        args:(string) allows for url with trivia url be in json
        return:results'''
        r = requests.get(self.url)
        response: dict = r.json()

        return response.get('results', None)