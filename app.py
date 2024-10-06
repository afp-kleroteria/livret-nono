"""test Flask with this"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import *
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?nhjjhjhk55WOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

class LivretForm(FlaskForm):
    name = StringField("Prénom de l'élève?", validators=[DataRequired(), Length(1, 40)])
    ortho=BooleanField("consolider / ortho")
    reso_pb_cm=BooleanField("aprofondir / Reso pb + CM")
    c_lecture=BooleanField("aprofondir / C.lecture")
    reso_pb=BooleanField("aprofondir / Reso pb")
    etude_doc=BooleanField("aprofondir / Etude doc")
    effort= RadioField("progression / effort", choices= ['Effort S1','Effort S2'], validate_choice = False)
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = LivretForm()
    message= ""
    if form.validate_on_submit():
        message=f"Ecris une appréciation scolaire pour l'élève {form.name.data} qui "
        if form.ortho.data == True :
            message+= ", doit poursuivre ses efforts pour consolider l'orthographe"
        if form.reso_pb_cm.data == True:
            message+= " , doit renforcer la résolution de problèmes et de calcul mental"
        if form.c_lecture.data == True:
            message+= ", doit approfondir la compréhension de lecture"
        if form.reso_pb.data == True:
            message+= ", doit approfondir la résolution de problèmes pour mieux progresser"
        if form.etude_doc.data == True:
            message+= ", doit approfondir l'étude de documents"
        if form.effort.data!= None:
            if form.effort.data== "Effort S1" :
                message+= ",doit poursuivre ses efforts pour continuer à progresser"
            elif form.effort.data == "Effort S2" :
                message += ", a su travailler régulièrement pour corriger ses erreurs et commence à appliquer les règles apprises de manière plus systématique"
    return render_template('index.html',the_title='Livrets élèves', form=form, message=message)


