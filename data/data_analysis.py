import pandas as pd
from config import Config
from sqlalchemy import create_engine

engine = create_engine(
    f'mysql+pymysql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_NAME}?charset=utf8')

videodata = pd.read_sql_table('videodata', engine)
commentdata = pd.read_sql_table('commentdata', engine)


def part1():
    """
    用户ip分布
    """
    result1 = commentdata['userIP'].value_counts().reset_index()
    result1.columns = ['userIP', 'count']
    print(result1)
    result1.to_sql('part1', engine, if_exists='replace', index=False)


def part2():
    """

    点赞与收藏
    """
    result1 = videodata[['likeCount', 'collectCount', 'description']] \
        .sort_values('likeCount', ascending=False) \
        .head(10)

    result1['ratio'] = result1['collectCount'] / result1['likeCount']
    print(result1)

    result1.to_sql('part2', engine, if_exists='replace', index=False)


def part3():
    """

    粉丝数量区间
    """
    bins = [0, 100, 1000, 10000, 100000, float('inf')]
    labels = ['小于100', '小于1000', '小于10000', '小于100000', '大于100000']
    videodata['fansRange'] = pd.cut(videodata['fansCount'], bins=bins, labels=labels)

    result = videodata['fansRange'].value_counts().reset_index()
    result.columns = ['fansRange', 'count']
    result.to_sql('part3', engine, if_exists='replace', index=False)
    print(result)


def part4():
    """
    粉丝数量排行
    """
    videodata_df = videodata[['username', 'fansCount']]
    result = videodata_df.drop_duplicates('username')
    result = result.sort_values('fansCount', ascending=False)
    result = result.head(10)
    print(result)
    result.to_sql('part4', engine, if_exists='replace', index=False)


def part5():
    """
    评论与分享
    """
    videodata_df = videodata[['commentCount', 'shareCount', 'description']]
    result = videodata_df.sort_values('commentCount', ascending=False)
    result = result.head(10)
    result.to_sql('part5', engine, if_exists='replace', index=False)


if __name__ == "__main__":
    # part1()
    # part2()
    # part3()
    part4()
    part5()
