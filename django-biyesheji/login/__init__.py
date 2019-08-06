import pymysql, os

pymysql.install_as_MySQLdb()


default_app_config = 'login.apps.LoginConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]



