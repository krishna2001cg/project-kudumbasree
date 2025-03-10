from flask import Flask
from admin import admin
from public import public

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)

app.run(debug=True)