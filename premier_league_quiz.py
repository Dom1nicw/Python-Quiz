def start_quiz(questions):
    score = 0
    number_of_questions = len(questions)

    for question in questions:
        print(question["question_text"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter A, B, C, or D then press ENTER: ").upper()
        if user_answer == question["answer"]:
            print("Correct.\n")
            score += 1
        else:
            print("Incorrect. The correct answer is {}.\n".format(question["answer"]))

    print("You answered {} out of {} questions correctly.".format(score, number_of_questions))



questions = [
    {
        "question_text": "When did Man City get promoted to the Premier League?",
        "options": ["A. 1980", "B. 1998", "C. 2002", "D. 2007"],
        "answer": "C"
    },
    {
        "question_text": "Which player holds the record for most Premier League goals in a season?",
        "options": ["A. Erling Haaland", "B. Cristiano Ronaldo", "C. Mohammed Salah", "D. Luis Suarez"],
        "answer": "A"
    },
    {
        "question_text": "How many different teams have won the Premier League?",
        "options": ["A. 4", "B. 7", "C. 9", "D. 11"],
        "answer": "B"
    },
    {
        "question_text": "Which 2 players are tied with the record for most assists in a Premier League season?",
        "options": ["A. De Bruyne & Fabregas", "B. De Bruyne & Henry", "C. Giggs & Fabregas", "D. Henry & Giggs"],
        "answer": "B"
    }
]


start_quiz(questions)
