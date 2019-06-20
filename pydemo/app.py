# -*- coding:utf-8 -*-

# 步骤：
#   1.导入Flask扩展
from flask import Flask , render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField
from wtforms.validators import DataRequired,EqualTo
#   2. 创建Flask应用程序实列
#   需要传入__name__，作用是为了确定资源所在路径
app = Flask(__name__)
app.secret_key = 'aone'
#   3.定义路由以及试图函数
#   Flask中定义路由是通过装饰器实现的
#   路由默认只支持GET，如果需要增加，就用methods=['GET','POST']
@app.route('/',methods=['GET','POST'])
def hello_world():
    url = '123.456.789.000' # 字符串
    list = [1, 2, 3, 4, 5, 6]    # 列表
    dict = {
        'name': '123',
        'age': '456'
    }                       # 字典
    int_ = 18                 # 整型
    # 通常，模板中使用变量名和要传递数据的变量名保持一致
    return render_template('index.html',url=url,list=list,dict=dict,int_=int_)


#   <>定义一个路由参数，内部名称就是入参
@app.route('/order/<int:orderId>',methods=['GET','POST'])
def order(orderId):
    print(type(orderId))
    #对路由做访问优化，订单orderId为int类型:/order/<int:orderId>
    #需要在视图函数()内填入参数名，那么后面的代码才能使用
    return 'orderId %s' % orderId


'''
目的：实现一个简单登陆逻辑处理
1.路由需要有get和post两种请求方式--->需要判断请求方式
2.获取请求参数
3.判断参数是否填写以及密码是否相同
4.判断OK，返回success
'''

'''
给模板传递消息：用flash--->需要对内容加密，需要设置secret_key：做加密的key
模板中需要遍历消息
解决编码问题可以在字符串前面加一个u
'''
@app.route('/login',methods=['GET','POST'])
def login():
    # 1.路由需要有get和post两种请求方式--->需要判断请求方式
    if request.method == 'POST':
        # 2.获取请求参数
        name = request.form.get('username')
        pw = request.form.get('password')
        pwd = request.form.get('password2')
        print(name+pw+pwd)
        # 3.判断参数是否填写以及密码是否相同
        if not all([name.pw.pwd]):
            # print('参数不完整')
            flash(u'参数不完整')
        elif pw != pwd:
            # print('密码不一致')
            flash(u'密码不一致')
        else:
            # print('成功')
            flash(u'成功')
            return 'success'
    return render_template('login.html')

'''
使用WTF实现表单类
自定义表单类
'''
class LoginForm(FlaskForm):
    username =StringField(u'用户名', validators=[DataRequired()])
    password = StringField(u'密码', validators=[DataRequired()])
    password2 = StringField(u'确认密码', validators=[DataRequired(),EqualTo('password','密码填写不一致')])
    submit = SubmitField(u'提交')

@app.route('/aaa', methods=['GET', 'POST'])
def aaa():
    login_from=LoginForm()
    # 1.路由需要有get和post两种请求方式--->需要判断请求方式
    if request.method == 'POST':
        # 2.获取请求参数
        name = request.form.get('username')
        pw = request.form.get('password')
        pwd = request.form.get('password2')

        # 3.验证参数。WTF可以一句话就实现所有的效验
        if login_from.validate_on_submit():
            print(name+pw)
            return 'ok'
        else:
            flash('参数错误')
    return render_template('login.html',login_from = login_from)




#  4.启动程序
if __name__ == '__main__':
    #   执行了app.run，就会将Flask程序运行在一个简易的服务器上(Flask提供的，用于测试)
    app.run()
