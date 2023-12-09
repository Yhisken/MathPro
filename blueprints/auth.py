from flask import Blueprint,url_for,session#引用蓝图
from flask import render_template
from flask import request
from exts import mail,db
from flask_mail import Message
import string
import random
from flask import redirect
from flask import jsonify
from models import UserModel,EmailCaptchaModel
from .forms import RegisterForm,Loginform
from werkzeug.security import generate_password_hash,check_password_hash   #加密密码



bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            username = form.username.data
            user = UserModel(email = email,password = generate_password_hash(password),username=username)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print('**************************')
            print(form.errors)
            return redirect(url_for('auth.register'))

@bp.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = Loginform(request.form)
        if form.validate():
            ### 进行表单验证
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email = email).first()
            if not user:
                print('邮箱账户不存在')
                return redirect(url_for('auth.register'))
            else:
                ### 就是邮箱存在，这时候我们得进行密码验证，又因为我们对密码进行了加密，所以得进行一系列的操作才行
                if check_password_hash(user.password,password):
                    # cooike 不适合存储太多数据，只适合存储少量数据  饼干碎屑 一般用于用户授权信息
                    # flask的session是经过加密后存储在cookie中的
                    session['user_id'] = user.id
                    return redirect('/')  # 找到根目录 就可以完成
                else:
                    print('登陆失败！')
                    return redirect(url_for('auth.login'))
        else:
            return f'{form.errors}'




@bp.route('/mail/test')
def mail_test():
    message = Message(subject='Test_qq_mail',recipients=['2942811564@qq.com'],body='hello,XiaoBu!')

    print(message)
    mail.send(message)
    return '发送成功！'
    #     mail.send(message)
    #     return "邮件发送成功！"
    #     # subject 表示发送主题
    #     # recipients 表示发送对象（发送的地址）
    #     # body 表示发送的内容

@bp.route("/captcha/email")
def get_email_captcha():#发送验证码 随机的四位
    ####生成验证码
    # 我们有两种传参方式
    #   /captcha/email/<email> 根据路径传参 用<>来传递参数
    #/captcha/email?email=2036801580@qq.com
    email = request.args.get("email")
    source = 4*string.digits#'0123456789012345678901234567890123456789'
    captcha = random.sample(source,4)#随机四位验证码长度
    captcha =''.join(captcha)#把列表变成字符串 就是列表袁术拼接
    ###发送验证码
    message = Message(subject='hello,goodmoring',recipients = [email],body = f"GOOD MORNING,能把验证码发给我吗？验证码时效60s：{captcha}")
    mail.send(message)
    # 把邮箱和验证码传入到数据库中
    #memcached/redis 缓存 验证码在服务器也得存储一份
    #用数据库中存储验证码，偏慢一点
    email_catpcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_catpcha)
    db.session.commit()

#restful api  返回数据统一一个格式
#  {code :200/400/500,message:"“，data：{}}
    return jsonify({'code':200,"messzge":"",'data':None})
    # return f"验证码为{captcha}"


