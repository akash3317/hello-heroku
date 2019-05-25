from flask import Flask
app=(__name__)
@app.route('/')
def index():
return 'hello world'
