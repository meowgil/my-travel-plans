import pandas as pd
import re
import os 
import numpy as np
import pinyin
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import PIL.Image as Image

# 读取并转换数据的格式
# 这里我们使用了假数据来完成项目，如果您倾向于探索自己微信好友的数据，您可以参考以下资料在本地完成
# https://github.com/udacity/AIPND-cn-trial
dataset = pd.read_csv('wechat_friends.csv').fillna('').to_dict('records')

## 任务1：好友男女比例
# 根据我们希望探索的问题，需要从数据集中取出以下几个部分：
# * NickName：微信昵称
# * Sex：性别，1表示男性，2表示女性，其它表示 unknown
# * Province：省份
# * City：城市
# * Signature：微信签名

## TODO：打印 dataset 的数据类型
print('dataset 的数据类型：', type(dataset))

## TODO：打印第一条数据及数据类型
print('dataset 中的第一条数据：', dataset[0])
print('dataset 中第一条数据的数据类型：', type(dataset[0]))

## TODO：打印第一条数据的微信昵称
print('dataset 中第一条数据的微信昵称：', dataset[0]['NickName'])


# ## 任务2：统计男女比例
# 统计好友性别，分为男性、女性与未知三种，赋值到已经定义好的 sex 字典中。
# 虽然我们这里没有要求，但是实际的名单中，索引为0的实际是自己；

## TODO：统计好友性别
sex = {
    'male': 0,
    'female': 0,
    'unknown': 0
}

for f in dataset:
    if f['Sex'] == 1:
        sex['male'] += 1
    elif f['Sex'] == 2:
        sex['male'] += 1
    else:
        sex['unknown'] += 1

print("我的好友中共有", sex['male'],"位男性、", sex['female'], "位女性，有", sex['unknown'], "位好友未填写。")

## 使用饼图分析好友的性别信息，饼图用来分析不同分类的占比情况。
## 以下代码不需要更改，matplotlib 是 Python 下常用的可视化工具。
## 若有兴趣，你可以学习优达学城的数据分析（入门）课程。
plt.figure(figsize=(8,5), dpi=80)
plt.axes(aspect=1) 
plt.pie([sex['male'], sex['female'], sex['unknown']],
        labels=['Male','Female','Unknown'],
        labeldistance = 1.1,
        autopct = '%3.1f%%',
        shadow = False,
        startangle = 90,  
        pctdistance = 0.6 
)

plt.legend(loc='upper left',)
plt.title("My Wechat Friends' Sex Ratio")
plt.savefig('sex_ratio.png') # 导出图片

# ## 任务 3：统计好友省份
# 使用 list 中 append() 方法将好友省份添加至 province 中，注意要去除空的字符串
# 提示：这里要去除的空字符串，指的是好友省份信息中为空的那些。空字符串是''，你可以用 == 来判断它。

### TODO：将好友所在省份（不为空）添加到 province 中
province = []
for f in dataset:
    if f['Province'] != '':
        province.append(f['Province'])

### 以下内容无需修改，直接运行即可
province = [pinyin.get(i, format="strip", delimiter="") for i in province if i != '']
province = pd.DataFrame(province)
province.columns = ['Province']
province['Number of Friends'] = 1
# 条形图用于描述分类变量的分布情况。在条形图中，分类变量的每个级别用长条表示，高度表示数据在该级别的出现频率。
province.groupby('Province').sum().sort_values('Number of Friends', ascending=False)[:10].plot.bar()
plt.savefig('provice.png')


# ## 任务 4：打印个性签名
# 使用 print() 语句打印出第 2 条签名

### TODO：打印出第2条签名
print(dataset[1]['Signature'])

### 以下内容无需修改，直接运行即可

tList = []
for i in dataset:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    if len(signature) > 0:
        tList.append(signature)

text = "".join(tList)

wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

alice_coloring = np.array(Image.open("wechat.jpg"))

my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                         max_font_size=40, random_state=42, font_path='./NotoSansHans-DemiLight.otf').generate(wl_space_split)


plt.imshow(my_wordcloud)
plt.axis("off")

my_wordcloud.to_file("wechatfriends_wordcloud.png")