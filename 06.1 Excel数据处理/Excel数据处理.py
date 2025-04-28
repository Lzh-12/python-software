import openpyxl
import pymysql
import pandas as pd
from openpyxl.chart import BarChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows


# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Root2092',
    'port': 3306,
    'charset': 'utf8mb4',
    'database': 'sakila'
}

# 建立数据库连接
try:
    db = pymysql.connect(**db_config)
except pymysql.err.OperationalError as e:
    print(f"数据库连接失败：{e}")
    exit(1)  # 如果数据库连接失败，则退出程序

try:
    # 创建一个游标
    cursor = db.cursor()

    # 定义SQL查询命令
    query = """
    SELECT rating, AVG(length) as avg_length, AVG(rental_duration) as avg_duration,
           AVG(rental_rate) as avg_rate, MIN(rental_rate) as min_rate,
           MAX(rental_rate) as max_rate, AVG(replacement_cost) as avg_cost
    FROM film
    GROUP BY rating
    ORDER BY avg_rate DESC, avg_cost DESC;
    """

    # 执行SQL查询
    cursor.execute(query)

    # 获取查询结果
    results = cursor.fetchall()

    # 列名
    column_names = [desc[0] for desc in cursor.description]

    # 使用pandas创建DataFrame
    df = pd.DataFrame(results, columns=column_names)

    # 将DataFrame保存到Excel文件中
    excel_path = 'yootk_sakila.xlsx'
    df.to_excel(excel_path, index=False, sheet_name='Sheet1')

    print(f'数据已保存到 {excel_path} 文件的第一个Sheet中。')

    # 打开之前保存的Excel文件
    excel_path = 'yootk_sakila.xlsx'
    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active

    # 将DataFrame转换为Excel中的行
    for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    # 创建柱状图
    chart = BarChart()
    # 第二列开始，因为第一列是索引
    data = Reference(ws, min_col=2, min_row=1, max_row=len(df) + 1, max_col=8)
    # 定义类别区域
    categories = Reference(ws, min_col=1, min_row=2, max_row=len(df) + 1)
    # 添加数据到柱状图
    chart.add_data(data, titles_from_data=True)
    # 设置类别轴
    chart.set_categories(categories)
    # 设置图表标题和轴标题
    chart.title = "电影评分统计柱状图"
    chart.y_axis.title = "平均租赁费用和重置成本"
    chart.x_axis.title = "电影评分"

    # 将柱状图添加到工作表
    ws.add_chart(chart, "A10")

    # 保存新的Excel文件
    new_excel_path = 'yootk_sakila_with_charts.xlsx'
    wb.save(new_excel_path)
    print(f'包含柱状图的数据已保存到 {new_excel_path} 文件中。')

except Exception as e:
    print(f"发生错误：{e}")
finally:
    # 关闭游标和数据库连接
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
