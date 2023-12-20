#!/usr/bin/python3

import requests

itemurl = "https://opentdb.com/api.php"

def main():
    questions = input('Enter the number of trivia questions you would like: ')
    difficulty = difficulty.lower(input('Enter the difficulty level (easy, medium or hard): '))
    items = requests.get(f"{itemurl}?amount={questions}&difficulty={difficulty}").json()
    count = 1
    for q in items["results"]:
        print("\n" + str(count) + ") " + html.unescape(q.get("question")) + "\n")
        print("Correct answer is: \n" + html.unescape(q.get("correct_answer")) + "\n")
        count +=1
# https://opentdb.com/api.php?amount=10&difficulty=medium

if __name__ == "__main__":
    main()
	
