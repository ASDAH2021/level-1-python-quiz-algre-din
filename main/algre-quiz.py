from operator import truediv
#importing the Question folder
from Question import Question

question_prompts = [
    "1. What is Larry's superhero name?\nA Minnesota Cuke\nB Larryboy\nC Supercuke\nD Green Larry\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "2. What bible story does Veggietales portray in Duke and the Great Pie War episode?\nA Ruth and Boaz\nB Rahab and the spies\nC David and Goliath\nD Adam and Eve\n\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "3. What is the name of the computer?\nA Asdf\nB Qwerty\nC Uiop\nD Ghjkl\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "4. What type of vegetable is Petunia?\nA Radish\nB Broccoli\nC Rhubarb\nD Asparagus\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "5. Who sang the song ‘Pizza Angel’?\nA Bob\nB Larry\nC Petunia\nD Pa Grape\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "6. Who sang the song ‘Lance the Turtle’?\nA Bob\nB Larry\nC Petunia\nD Archibald\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "7. Finish the sentence: “We are the pirates...”\nA who don’t do anything.\nB who sail the seven seas.\nC who are searching for the whale.\nD who crashed their ship.\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "8. Who is the Supper Hero?\nA Archibald\nB Larry\nC Jerry\nD Jimmy\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "9. Who played Jonah in Jonah: A Veggietales Movie?\nA Jerry\nB Bob\nC Pa Grape\nD Archibald\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "10. Who is the very model of a modern major general?\nA Jerry\nB Bob\nC Pa Grape\nD Archibald\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "11. Who played the angel in Gideon the Tuba Warrior?\nA Petunia\nB Pa Grape\nC Madame Blueberry\nD Archibald\nPLEASE TYPE JUST THE LETTER e.g. A >>",
    "12. How did Toto (Junior) save the land of Woe in Lord of the Beans?\nA He tosses the bean into the dry well.\nB He fights off all the sporks.\nC He sells grape soda to all the people in town.\nD He wishes for eternal riches and gives a portion to each veggie in the land.\nPLEASE TYPE JUST THE LETTER e.g. A >>",
]
#Setting the questions, the right answers and tha wrong answers.
questions = [
    Question(question_prompts[0], ["B", "b"], ["A", "a","c","C","d","D"]),
    Question(question_prompts[1], ["A", "a"], ["B", "b","c","C","d","D"]),
    Question(question_prompts[2], ["B", "b"], ["A", "a","c","C","d","D"]),
    Question(question_prompts[3], ["C", "c"], ["B", "b","a","A","d","D"]),
    Question(question_prompts[4], ["B", "b"], ["A", "a","c","C","d","D"]),
    Question(question_prompts[5], ["A", "a"], ["B", "b","c","C","d","D"]),
    Question(question_prompts[6], ["A", "a"], ["B", "b","c","C","d","D"]),
    Question(question_prompts[7], ["D", "d"], ["B", "b","c","C","a","A"]),
    Question(question_prompts[8], ["D", "d"], ["B", "b","c","C","a","A"]),
    Question(question_prompts[9], ["D", "d"], ["B", "b","c","C","a","A"]),
    Question(question_prompts[10], ["B", "b"], ["A", "a","c","C","d","D"]),
    Question(question_prompts[11], ["A", "a"], ["B", "b","c","C","d","D"]),
]

print("And now it's time for the veggietales quiz, the part of your day when you test your knowledge of veggietales(Not the reboot). Welcome.")

def run_test(questions):
    score = 0
    continuing = True
    while(continuing):
        for question in questions:
            answer = input(question.prompt)
            if answer in (question.answer):
                score += 1
                print("\nCorrect! your score is now " + str(score) + "\n")
                continuing = False
            elif answer in (question.test):
                print("\nWrong! Your score is still {}.\n" .format(score))
                continuing = False
            else:
                #while answer not in question.answer or answer not in question.test:-didn't work
                print("\nThat's not an option! Try again.\n")
                break#-doesn't work but Idk what else to do :(
                #answer = input(question.prompt)#-didn't work

    print("Our quiz is done! Let's see what you got...\n")
    #Deciding what to tell them depending on their end score.
    if score >= 0 and score <= 4: 
        print("You got " + str(score) + "/12 points. Well, I guess VeggieTales isn’t everyone’s cup of tea.\n") 
    elif score > 4 and score <= 7: 
        print("You got " + str(score) + "/12 points. Maybe you'd still rather have a coffee?\n")
    else:
        print("You got " + str(score) + "/12 points. This is your tea!.\n")

    print("That’s all the time we have for today kids. Just remember, God made you special, and he loves you very much. Goodbye!\n") 

run_test(questions)