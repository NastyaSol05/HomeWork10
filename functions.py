import json

def load_candidates():
    with open('candidates.json', 'r') as condidates:
        return json.load(condidates)


def get_by_pk(pk):
    return load_candidates()[pk - 1]


def get_by_skill(skill_name):
    return [i for i in load_candidates() if skill_name.lower() in i['skills'].lower()]



print(get_by_skill('python'))

def main_page(list_condidate):
    str_ =  ''
    for i in range(len(list_condidate)):
        str_+= f'''
        имя кандидата - {list_condidate[i]['name']}
        позиция кандидата - {list_condidate[i]['position']}
        навыки - {list_condidate[i]['skills']}
        '''
    return f'<pre>{str_}</pre>'

