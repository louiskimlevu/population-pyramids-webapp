from flask import Flask, render_template, flash, request, jsonify, Markup
app = Flask(__name__)


@app.before_first_request
def startup():
    pass

@app.route('/', methods=['POST', 'GET'])
def hello():
    name_in_flask = "Louis Kim"
    if request.method=='POST':
        name_in_flask=request.form['name_in_form_html']
        print('in POST')
        
    return render_template('index.html',
						name_in_html = name_in_flask)
if __name__=='__main__':
    app.run(debug=True)
    
