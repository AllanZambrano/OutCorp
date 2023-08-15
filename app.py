from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template ("index.html")

@app.route("/content")
def content():
  return render_template ("content.html")

@app.route("/contact")
def contact():
  return render_template ("contact.html")

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)