#!/usr/bin/python3

import requests

ITEMURL = "https://opentdb.com/api.php"

def main():
    QUESTIONS = input('Enter the number of trivia questions you would like: ')
    DIFFICULTY = input('Enter the difficulty level (easy, medium or hard): ')
    items = requests.get(f"{ITEMURL}?amount={QUESTIONS}&difficulty={DIFFICULTY}")
    items = items.json()
    count = 1
    for q in items["results"]:
        print("\n" + str(count) + ") " + q.get("question") + "\n")
        print("Correct answer is: \n" + q.get("correct_answer") + "\n")
        count +=1
# https://opentdb.com/api.php?amount=10&difficulty=medium


if __name__ == "__main__":
    main()
