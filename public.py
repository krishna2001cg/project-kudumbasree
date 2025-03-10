from flask import *
from database import *
public=Blueprint('public',__name__)
@public.route('/')
def home():
    return render_template('home.html')
@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
      uname=request.form['username']
      passw=request.form['passw']
      print("username",uname)
      print("password",passw)
      qr="insert into login values(null,'%s','%s','user')"%(uname,passw)
      insert(qr)
      qr="select * from login where user_name='%s' and password='%s'"%(uname,passw)
      res=select(qr)
      if res[0]['user_type']=='admin':
          return redirect(url_for('admin.admin_home'))
    return render_template('login.html')

@public.route('/user_registration',methods=['get','post'])
def user_registration():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        uname=request.form['uname']
        passw=request.form['passw']
        qr="insert into login values(null,'%s','%s','user')"%(uname,passw)
        res=select(qr)
        qn="insert into user values(null,'%s','%s','%s','%s')"%(res,fname,lname,place)
        res=select(qn)
    return render_template('user_registration.html')
  
    
    