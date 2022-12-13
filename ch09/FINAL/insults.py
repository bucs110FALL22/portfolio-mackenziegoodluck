import requests


class Insults:
    '''API to get insults'''

    def __init__(self) -> None:
        '''general function description:Creating an object of the API
        args:It's a string(allows url to be a string)
        return:none'''
        self.url: str = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

    def get(self) -> str:
        '''general function:Calling the api with the request
        args:string(allows for the insults to be in dictornary)
        return:it return the insult '''
        r = requests.get(self.url)
        response: dict = r.json()
        return response.get('insult', None)
        