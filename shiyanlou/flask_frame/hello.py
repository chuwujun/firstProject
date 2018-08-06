from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/shiyanlou')
def hello_world2():
    return 'liuqian'

#send path variable to the function
@app.route('/user/<username>')
def show_user_profile(username):
    #show user name
    return 'User %s' %username

@app.route('/post/<int:postid>')
def show_post(postid):
    return 'post id is %d' %postid

#only url
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(debug=True)
