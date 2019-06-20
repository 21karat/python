# -*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
import uuid
############################################################################################
app = Flask(__name__)
app.secret_key = 'aone'
#   数据库配置'mysql+pymysql://root:dzd123@localhost/你的数据库名'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@47.107.121.215/ssm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

############################################################################################
class Role(db.Model):
    #   定义表名
    __tablename__='roles'
    #   定义字段
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(16),unique=True)

    #   类似toString
    def __repr__(self):
        return self.name


class User(db.Model):
    #   定义表名
    __tablename__='users'
    #   定义字段
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    #  db.ForeignKey('roles.id')外键，表名.id
    roles_id = db.Column(db.Integer)
    def __init__(self , name , roles_id):
        self.name = name
        self.roles_id = roles_id

############################################################################################
#   查
@app.route('/', methods=['GET', 'POST'])
def select():
    #   查看
    user =User.query.all()
    return render_template('user.html',user=user)

#   增
@app.route('/add',methods=['GET','POST'])
def add():
    name = request.form.get('name')
    roles_id = request.form.get('roles_id')
    user = User(name,roles_id)
    #   添加数据
    db.session.add(user)
    db.session.commit()
    #   查看
    user = User.query.all()
    return render_template('user.html',user=user)

#   删
@app.route('/delUser/<id>',methods=['GET','POST'])
def delUser(id):
    print(id)
    if id != "":
        user =User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        #   查看
        user = User.query.all()
        flash(u'删除成功')
        return render_template('user.html', user=user)
    else:
        #   查看
        user = User.query.all()
        flash(u'删除失败')
        return render_template('user.html', user=user)


if __name__ == '__main__':
      app.run(debug=True)
