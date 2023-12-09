#配置数据库
# HOSTNAME = 主机名
# PROT = "端口号“
# DATABASE = "数据库名称"
# USERNAME = ”用户名"
# PASSWORF = "密码"
# DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)"
# SQLALCHEMY_DATABASE_URL = DB_URI
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "mathpro"
USERNAME = "root"
PASSWORD = "root"
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


SECRET_KEY = 'DASDAFAJNAWBDNOWADNAWDNAWJOA-EDAWK'

# uahzhvnmcphnbbbd
#邮箱配置信息
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "990637259@qq.com"
MAIL_PASSWORD = "xcsonxvocqorbcdb"
MAIL_DEFAULT_SENDER = "990637259@qq.com"






