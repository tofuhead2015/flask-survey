from flask import Flask, request, render_template, flash, redirect
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "top secret"

survey = surveys.personality_quiz
answers = []

@app.route('/')
def show_start():
    print(survey)
    return render_template('start.html', title=survey.title, instructions=survey.instructions)

@app.route("/questions/<q_id>")
def show_question(q_id):    
    id = int(q_id)
    if (len(answers) == len(survey.questions)):
        return render_template('thank_you.html', answers = answers)
    if id == len(answers):
        return render_template('question.html', question = survey.questions[id], question_id = str(id))
    else:
        flash("You are trying to access an invalid question!", "error")
        return render_template('question.html', question = survey.questions[len(answers)], 
        question_id = str(len(answers)))

@app.route('/answer', methods=['POST'])
def save_answer_and_show_next():
    if (len(answers) >= len(survey.questions)):
        return render_template('thank_you.html', answers = answers)
    answers.append(request.form['answer'])
    if (len(answers) == len(survey.questions)):
        return render_template('thank_you.html', answers = answers) 
    return redirect("/questions/" + str(len(answers)))
    
