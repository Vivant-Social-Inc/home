from flask import Flask, render_template, request, redirect 
import re

app = Flask(__name__) 

# GET Index Page
@app.route('/')
def index():
    return render_template('index.html')


# GET About page
@app.route('/about')    
def about(): 
    return render_template('about.html')


# GET Host page
@app.route('/host')    
def host(): 
    return render_template('host.html')


# GET Form page
@app.route('/form')    
def form(): 
    return render_template('form.html')


# POST request for "stay connected" forms on Index & About
@app.route('/connect', methods=['POST'])
def connect(): 
    return redirect('/form')


""" Note that the POST request for the Host page should be managed by an automated email """


# POST request for Form page data
@app.route('/post_form_data', methods=['POST'])
def post_form_data(): 
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=False)