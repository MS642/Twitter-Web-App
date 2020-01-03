from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '916fd9b2b8bc5645d34dd9794ddafd44'

posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'

	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'

	}

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com'and form.password.data == 'password':
			flash('You are Logged in as an Admin!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Usuccessful! check email and password', 'danger')
	return render_template('Login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)

