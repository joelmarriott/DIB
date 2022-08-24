from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from models import Display, app, db


@app.route('/', methods=['POST', 'GET'])
def index():
    new_display = Display.query.order_by(desc(Display.date_created)).first()
    return render_template('index.html', new_display=new_display)


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/manage')
def manage():
    return render_template('manage.html')


@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        postcode = request.form['postcode']
        if postcode == "ALL":
            displays = Display.query.order_by(Display.date_created).all()
        else:
            displays = Display.query.filter(Display.postcode.contains(postcode)).order_by(Display.date_created).all()
        return render_template('listdisplays.html', displays=displays, postcode=postcode)
    else:
        displays = Display.query.order_by(Display.date_created).all()
        return render_template('listdisplays.html', displays=displays, postcode="ALL")


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        print(str(request.form))
        form_data = { key:request.form[key] for key in request.form }
        print(str(form_data))
        form_data['owners'] = 1
        new_display = Display(**form_data)

        try:
            db.session.add(new_display)
            db.session.commit()
            db.session.flush()
            return redirect('/')
        except:
            return 'There was an issue adding your display'
    else:
        return render_template('newdisplay.html')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        display = db.session.query(Display).get_or_404(id)
        form_data = { key:request.form[key] for key in request.form }
        form_data['owners'] = 1
        try:
            for key, value in form_data.items():
                print(key, value)
                setattr(display, key, value)
            db.session.commit()
            db.session.flush()
            return redirect('/')
        except:
            return 'There was an issue adding your display'
    else:
        display = Display.query.get_or_404(id)
        return render_template('updatedisplay.html', display=display)


@app.route('/view/<int:id>')
def view(id):
    display = db.session.query(Display).get_or_404(id)
    return render_template('viewdisplay.html', display=display)


@app.route('/delete/<int:id>')
def delete(id):
    display_to_delete = Display.query.get_or_404(id)    
    db.session.delete(display_to_delete)
    db.session.commit()
    db.session.flush()
    return redirect('/list')

if __name__ == "__main__":
    app.run(debug=True)
