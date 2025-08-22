from flask import Blueprint, render_template, request, flash, jsonify, session, url_for, redirect
from flask_login import login_required
from .models import Note, User
from . import db
import json
from .security import ManageSession


views = Blueprint('views', __name__)
#MS = ManageSession()

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    
    if (session.get('id', None) is None):
        return redirect(url_for('auth.login'))

    #user_id =(session.get('id'))
    #session["id"] = (user_id)
    if request.method == 'POST':
        note = request.form.get('note')
        

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            user_id = (session.get('id'))
            new_note = Note(data=note, user_id = user_id)
            db.session.add(new_note)
            db.session.commit()                
            flash('Note added!', category='success')
            
            

    return render_template("home.html", user = User.query.filter_by(id = (session.get('id'))).first())


@views.route('/delete-note', methods=['POST'])
def delete_note():
    
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == (session.get('id')):
            db.session.delete(note)
            db.session.commit()


   # user_id = MS.GetDecipher(session.get('id'))
   #session["id"] = MS.GetNewCipher(user_id)

    return jsonify({})
