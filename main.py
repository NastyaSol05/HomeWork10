from flask import Flask
from functions import *
app = Flask(__name__)



@app.route('/')
def print_candidates():
    return main_page(load_candidates())


@app.route('/candidate/<int:pk>')
def print_condidates(pk):
    return f'<img src="{get_by_pk(pk)["picture"]}">\n{main_page([get_by_pk(pk)])}'

@app.route('/skills/<skill>')
def print_skills(skill):
    return f'<pre>{main_page(get_by_skill(skill))}</pre>'

app.run()

