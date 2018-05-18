from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True;

# @app.route('/hello/<name>')
# def hello(name):
# 	return "hello, " + name

# @app.route('/hello/<name>')
# def hello(name):
# 	foo_val=request.args['foo'] This returns arguments passed to the route
# 	return foo_val

# @app.route('/hello/<name>')
# def hello(name):
# 	return render_template('index.html',name=name)

@app.route('/params')
def hello():
	return render_template('index.html',my_args=request.args)


@app.route('/form',methods=['GET','POST'])
def process_form():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		return render_template('index.html', my_args=request.form)

@app.route('/pic',methods=['GET','POST'])
def upload_pic():
	if request.method == 'GET':
		return render_template('pic.html')
	else:
		my_photo = request.files['photo']
		fname = my_photo.filename
		my_photo.save('static/{0}'.format(fname))
		dl_link = 'static/{0}'.format(fname)
		return render_template('pic.html', dl_link=dl_link)

app.run()