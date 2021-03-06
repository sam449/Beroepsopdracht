from Question import Question

question prompts = [
    "Waar kom ik vandaan?\n(a) amsterdam\n(b) diemen\n(c) Amstelveen\n\n",
    "Hoe reis ik naar school?\n(a) bus\n(b) tram\n(c) metro\n\n",
    "Hoelang reis ik naar school?\n(a) 15min\n(b) 30min\n(c) 45min\n\n"
]

questions = [
    Question(question_prompts[3], "c"),
    Question(question_prompts[0], "a"),
    Question(question_prompts[3], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
