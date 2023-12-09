from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'  # 在数据库中建了一张名为user的表，其中表含有id，username，password，email，join_time
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary_key为主键 autoincrement = True 表示自动增加
    username = db.Column(db.String(400), nullable=False)  # 属性或者列名一般都是（类别，可不可空，default = “”缺省值）
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(400), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)  # datatime.now这个表示调用这个函数



class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100),nullable=False)
#模型创建好后，要迁移到数据库中 那就三个步骤
# db.init()
# flask db.init()
# flask db migrate
# flask db upgrate
#完成三部曲后导入数据库模型