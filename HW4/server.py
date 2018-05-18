from flask import Flask, request, render_template, redirect
from database import Database

app = Flask(__name__)
app.config.from_pyfile('server.cfg')

"""
Use the following commands to interact with the database:
  db.get() to get all of the reviews
  db.get(id) to get a single review
  db.create(title, text, rating) to add a new review
  db.update(id, title, text, rating) to update a review
  db.delete(id) to delete a review
"""
db = Database(app)

@app.route('/')
def show_all_reviews():
	movies = db.get()
	return render_template('allreviews.html', movies= movies)


@app.route('/review')
def show_specific_review():
	for key,val in request.args.items():
		movie = db.get(val)
		
	return render_template('singlereview.html', movie = movie)

@app.route('/create',methods=['GET','POST'])
def create_review():
	if request.method == 'GET':
		return render_template('createreview.html', movie = None)
	else:
		title = request.form['title']
		review = request.form['review']
		rating = request.form['rating']
		db.create(title, review, rating)
		return redirect("/")

@app.route('/edit',methods=['GET','POST'])
def edit_review():
	if request.method == 'GET':
		for key,val in request.args.items():
			movie = db.get(val)	
		return render_template('createreview.html', movie = movie)
	else:
		title = request.form['title']
		review = request.form['review']
		rating = request.form['rating']
		db.update(request.args['id'],title, review, rating)
		return redirect("/")

@app.route('/delete')
def delete_review():
	db.delete(request.args['id'])
	return "The Review has been deleted"


if __name__ == '__main__':
	app.run(port=8001)
