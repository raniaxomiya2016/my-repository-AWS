


# Import Flask module.
from flask import Flask
# Create an object named `app` from imported Flask module.
app = Flask(__name__)
# Create a function `hello` which returns a string `Hello World`.
#Assign a URL route the `hello` function with decorator `@app.route('/')`.@app.route('/')

def hello():
    return "<h1>Hello World</h1>"
  
if __name__ == '__main__':
    app.run(debug=False)
    
    
    





#Import Flask module.
from flask import Flask

#Create an object named `app` from imported Flask module.
app = Flask(__name__)

#Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')
@app.route('/second')

def second():
    
    return "<h2>This is the second page</h2>"

if __name__ == '__main__':
    app.run(debug=False)   
    



#Import Flask module.
from flask import Flask

# Create an object named `app` from imported Flask module.
app = Flask(__name__)

#Create a function `third` which returns a string `This is the subpage of third page` and assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 

@app.route('/third/subthird')
def third():
    return "<h2>This is the subpage of the third page</h2>"

if __name__ == '__main__':
    app.run(debug=False)    
    
    
    
    
#Import Flask module.
from flask import Flask

# Create an object named `app` from imported Flask module.
app = Flask(__name__)

#Create a dynamic url which takes id number dynamically and return with a massage which show id of page.

@app.route('/forth/<string:id>')
def forth(id):
    return f'This is page id {id}'
