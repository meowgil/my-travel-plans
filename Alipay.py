# coding=utf-8

import csv
from collections import defaultdict

RAW_RECORD = 'alipay_record_20190429_1707_1.csv'  ## 填写你下载的文件名称，需要包括 .csv 后缀
CLEANED_RECORD = RAW_RECORD.split('.')[0] + '_cleaned.csv'

def clean_csv(input, output):
    with open(input, encoding='gbk') as f, open(output, 'w') as o:
        lines = f.readlines() ## 注意这行代码会一次性读取整个文件，若文件非常大时不推荐使用
        lines = lines[4:-7] ## 去掉开头结尾非 CSV 的内容
        lines = [line.replace(' ', '') for line in lines] ## 去掉空格
        o.writelines(lines)

def analyze_income_expense(record):
    income = 0
    expense = 0

    with open(record, 'r') as f:
        records = csv.DictReader(f)
        for r in records:
            if r['收/支'] == '支出':
                expense  += float(r['金额（元）'])
            elif r['收/支'] == '收入':
                income += float(r['金额（元）'])

    print(f'\n总收入：{income:.2f}，总支出：{expense:.2f}')


def analyze_max_expense_item(record):
    max_expense_row = []
    max_expense = 0

    with open(record, 'r') as f:
        records = csv.DictReader(f)
        for r in records:
            if r['收/支'] == '支出':
                if float(r['金额（元）']) > max_expense:
                    max_expense_row = r
                    max_expense = float(r['金额（元）'])

    print(f"\n单笔支出最高的款项发生在：{max_expense_row['交易创建时间']}，商品名称为：{max_expense_row['商品名称']}，交易对方为：{max_expense_row['交易对方']}，金额为：{max_expense_row['金额（元）']}")


def analyze_max_expense_date(record):
    expense_date = defaultdict(int) ## 使用 defaultdict 避免键值不在字典中的情况，详情：https://www.jianshu.com/p/bbd258f99fd3  

    with open(record, 'r') as f:
        records = csv.DictReader(f)
        for r in records:
            if r['收/支'] == '支出':
                r['交易创建时间'] = r['交易创建时间'][:10]
                expense_date[r['交易创建时间']] += float(r['金额（元）'])

    ## 循环遍历 expense_date 中的日期和支出，找出支出最多的一天
    date_max = ''
    expense_max = 0
    for k, v in expense_date.items():
        if expense_max < v:
            expense_max = v
            date_max = k
    print(f'\n支出金额最多的一天发生在：{date_max}，总计花费：{expense_max:.2f}')


if __name__ == "__main__":
    clean_csv(RAW_RECORD, CLEANED_RECORD)
    analyze_income_expense(CLEANED_RECORD)
    analyze_max_expense_item(CLEANED_RECORD)
    analyze_max_expense_date(CLEANED_RECORD)