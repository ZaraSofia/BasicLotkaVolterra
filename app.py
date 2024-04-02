from flask import Flask, jsonify, render_template, request

#jsonify: return/create response in JSON format
#render_template: render html for template engine
#request: uses POST and GET

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST']) 

#return index.html
def index():

    #If there is input data from form, json data will be return to output
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + " " + lastname

        #if both fields are entered
        if firstname and lastname:
            return jsonify({'output' : 'Your name is ' + output + ', right?'})
        
        #if missing a field  retunr error
        return jsonify({'error' : 'Missing data!'})
    
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug = True)

