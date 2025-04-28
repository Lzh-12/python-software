from pymysqlpool import ConnectionPool

pool_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Root2092',
    'database': 'yootk',
    'autocommit': False
}  # 连接池配置项

connect_pool = ConnectionPool(size=5, maxsize=100, pre_create_num=10,
                              con_lifetime=3600, name='yootk-cp', **pool_config)  # 连接配置项


def connection():  # 获取数据库连接
    return connect_pool.get_connection()
