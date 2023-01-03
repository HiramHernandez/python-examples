from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    request,
    url_for,
    session,
    logging
)
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from dump_data.articles import Articles
from forms.register import RegisterForm

app = Flask(__name__)
# Config MySQL DB
app.config ['MYSQL_HOST'] = 'localhost'
app.config ["MYSQL_USER"] = 'root'
app.config ["MYSQL_PASSWORD"] = 'lmZ1415&'
app.config ["MYSQL_DB"] = 'blog'
app.config ["MYSQL_CURSORCLASS"] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index() -> str:
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles())

@app.route('/articles/<string:id>/')
def display_article(id):
    return render_template('article.html', articles = Articles())

@app.route('/article/<string:id>/')
def display_article_by_id(id):
    return render_template('article.html', id=id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data 
        email = form.email.data
        username = form.username.data 
        password = sha256_crypt.hash(str(form.password.data))
        print(name, email, username, password)
        # Creates cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password)) 
        # commit to db 
        mysql.connection.commit()
        #Close db
        cur.close()
        flash('You are now registered and may login. Welcome to BlogIt!', 'success')
        
        redirect(url_for('index'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.secret_key = 'Secret145'
    app.run(debug=True)