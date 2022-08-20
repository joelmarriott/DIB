from tempfile import TemporaryFile
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import Display

app = Flask('DIB')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dib.db'
db = SQLAlchemy(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        print(str(request.form))
        new_display = Display(**request.form)

        try:
            db.session.add(new_display)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your display'
    else:
        displays = Display.query.order_by(Display.date_created).all()
        return render_template('newdisplay.html', displays=displays)


if __name__ == "__main__":
    app.run(debug=True)