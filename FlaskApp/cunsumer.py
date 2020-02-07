import requests
import json

# STUDENT_OP_BASE_URI = "http://localhost:8000/student/"
STUDENT_OP_BASE_URI = "http://pary143.pythonanywhere.com/student/"


class Candidate:
    def __init__(self, id, name, age, gender, fees, address, active=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.fees = fees
        self.address = address

    def __str__(self):
        # return f'{self.__dict__}'
        return f'''
        Id : {self.id}
        Name : {self.name}
        Age : {self.age}
        Gender : {self.gender}
        Fees : {self.fees}
        Address : {self.address}\n'''

    def __repr__(self):
        return str(self)


def process_response(res):
    res = res.json()
    if type(res) == list:
        candidates = []
        for stud in res:
            candidates.append(Candidate(**stud))
        return candidates
    else:
        return Candidate(**res)


def get_all_students():
    response = requests.get(STUDENT_OP_BASE_URI)
    return process_response(response)


def get_single_student(stid):
    if stid > 0:
        response = requests.get(STUDENT_OP_BASE_URI + str(stid))
        if response.json().get('detail'):
            return response.json().get('detail')
        return process_response(response)
    else:
        return 'Invalid Id'


def delete_student(stid):
    if stid > 0:
        response = requests.delete(STUDENT_OP_BASE_URI + str(stid))
        if response.status_code != 204:
            return 'No student record present for id {}'.format(stid)
        else:
            return 'Student record removed for id {}'.format(stid), response.status_code
    else:
        return 'Invalid Id'


def update_student(stud):
    stud_dict = {
        "id": stud.id,
        "name": stud.name,
        "age": stud.age,
        "gender": stud.gender,
        "fees": stud.fees,
        "address": stud.address}
    response = requests.put(STUDENT_OP_BASE_URI + str(stud.id) + "/", json=stud_dict)
    if response.json().get('detail'):
        return response.json().get('detail')
    return process_response(response)


def save_student(stud):
    stud_dict = {
        "id": stud.id,
        "name": stud.name,
        "age": stud.age,
        "gender": stud.gender,
        "fees": stud.fees,
        "address": stud.address}
    response = requests.post(STUDENT_OP_BASE_URI, json=stud_dict)
    if response.json().get('detail'):
        return response.json().get('detail')
    return process_response(response)


if __name__ == '__main__':
    print(get_all_students())
    # print(get_single_student(1))
    # print(delete_student(3))
    # stud = Candidate(id=9, name='pary1', age=21, gender='F', fees=12000, address='Pune4')
    # print(save_student(stud))
    # print(update_student(stud))
