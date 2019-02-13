from flask import Flask

app=Flask(__name__)

@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    return '%d+%d is %d' %(a,b,a+b)

if __name__ == '__main__':
    app.run()

