# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (3:57:36)

from question import Question

question_prompts = [ # question prompts for multiple choice quiz
    "What color are honeycrisp apples?\n(a) Red\n(b) Green\n(c) Purple\n(d) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

# note to self: make this project later after done with tutorial