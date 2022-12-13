from random import shuffle
from string import ascii_uppercase
from trivia import Trivia
from insults import Insults

def main() -> None:
    '''General function description:asks user the answer to each question, then the dict tracks the users response
    args:strings
    return: it returns whether the user answer is right or wrong then displays a insult if its the wrong answer'''
    question_api = Trivia()
    insults = Insults()
    questions = question_api.get()

    # asking the user to answer each question
    for question in questions:
        # getting all the answers and shuffling them
        possible_answers: list[str] = question['incorrect_answers']
        possible_answers.append(question['correct_answer'])
        shuffle(possible_answers)

        # Creating a dictionary with letters as keys to responses
        choices: dict[str, str] = {}
        for letter, possible_answer in zip(ascii_uppercase, possible_answers):
            choices[letter] = possible_answer
        
        # Printing the question and the choices to user
        print(question['question'])
        for letter, choice_option in choices.items():
            print(f"{letter}: {choice_option}") 
        
        # Getting response from user
        while True:
            user_response: str = input("Enter the letter of your answer choice: ").upper()
            choice = choices.get(user_response, None)
            if choice is None:
                print("Not valid input... please put the letter of the choice.")
                continue
            if choice == question['correct_answer']:
                print("Good job that's the correct answer!\n")
                break
            
            print("WRONG!!!")
            print(insults.get())
            print()
            break


if __name__ == "__main__":
    main()
    