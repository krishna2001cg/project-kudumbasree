from flask import *
admin=Blueprint('admin',__name__)
@admin.route('/')
def home():
    return render_template('admin_home.html')
    
    