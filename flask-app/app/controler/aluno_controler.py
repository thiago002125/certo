from app import app, db, Aluno
from flask import request, jsonify

@app.route("/aluno/add", methods=["POST"])
def aluno_add():
    data = request.get_json()

    aluno = Aluno(data["nome"])

    db.session.add(aluno)
    db.session.commit()


    print(data)

    return  jsonify({"success": True})

@app.route("/aluno/list")
def aluno_list():
    alunos = Aluno.query.all()

    output = []

    for al in alunos:
        output.append(al.to_dict())

    return jsonify(output)

