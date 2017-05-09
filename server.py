from flask import Flask, request, render_template
app = Flask(__name__)


def import_from_file(file_name="pinaszaft.csv"):
    story_list = []
    with open(file_name, "r") as file_content:
        stories = file_content.readlines()
    for i in stories:
        stock_list.append(i.replace('\n', '').split(', '))
    return story_list


@app.route("/")
def hello():
    return render_template('form.html')


@app.route("/story", methods=['POST'])
def nem_story():
    story_title = request.form['story_title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    status = request.form['status']
    stuff_list = [story_title, user_story, acceptance_criteria, business_value, estimation, status]
    with open('pinaszaft.csv', "a") as stuff:
        for i in stuff_list:
            if i == stuff_list[len(stuff_list)-1]:
                stuff.write(i + '\n')
            else:
                stuff.write(i + ', ')
    return render_template('form.html')
if __name__ == "__main__":
    app.run()
