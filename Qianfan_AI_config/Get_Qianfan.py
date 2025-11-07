from datetime import datetime
from openai import OpenAI
from config import Config


def analyze_single_viedo(video_data, analysis_focus=None):
    AI_CONFIG = {
        'api_key': Config.api_key,
        'base_url': 'https://qianfan.baidubce.com/v2',
        'appid': Config.appid
    }

    client = OpenAI(
        api_key=AI_CONFIG['api_key'],
        base_url=AI_CONFIG['base_url'],
        default_headers={"appid": AI_CONFIG['appid']}
    )
    try:
        publish_date = datetime.strptime(video_data['发表时间'], "%Y.%m.%d")
        days_since_publish = (datetime.now() - publish_date).days
        days_info = f"已发布{days_since_publish}天"
    except:
        days_info = '发布时间数据异常'

    try:
        if isinstance(video_data['视频时长'], str):
            minutes, seconds = map(int, video_data['视频时长'].split(":"))
            video_duration = minutes * 60 + seconds
        else:
            video_duration = video_data['视频时长']
        interaction_rate = ((video_data['点赞数量'] + video_data['评论数量'] + video_data['分享数量']) / video_data[
            '粉丝数量']) * 100 if \
            video_data['粉丝数量'] > 0 else 0
        like_rate = (video_data['点赞数量'] / video_data['粉丝数量']) * 100 if video_data['粉丝数量'] > 0 else 0
    except Exception as e:
        print('指标异常')
        print(e)
        return str(e)
    prompt = f"""
    你是一个短视频内容策略专家，请分析以下视频信息数据，并提供优化建议。

    === 视频基础信息 ===
    - 粉丝数量: {video_data['粉丝数量']}
    - 发表时间: {days_info}
    - 视频描述: {video_data['视频描述']}
    - 视频时长: {video_duration}秒
    - 点赞数量: {video_data['点赞数量']}
    - 收藏数量: {video_data['收藏数量']}
    - 评论数量: {video_data['评论数量']}
    - 分享数量: {video_data['分享数量']}

    === 关键指标 ===
    - 点赞率: {like_rate:.2f}%
    - 互动率: {interaction_rate:.2f}%

    === 分析重点 ===
    {analysis_focus if analysis_focus else "1. 找出该视频表现优异/不足的指标. 提供内容优化建议. 建议发布时间调整（如有数据）"}

    请按照以下结构返回分析结果：
    === 表现评估 ===
    [分析点赞/评论/分享等指标的优劣]

    === 优化建议 ===
    1. [内容方向调整建议]
    2. [互动设计建议（如提问、投票等）]
    3. [标签/话题优化建议]
    """
    try:
        messages = [
            {
                "role": 'system',
                "content": "你是一个专业的短视频数据分析师，擅长从数据中发现优化机会。"
            },
            {
                "role": "user",
                "content": prompt
            }

        ]

        response = client.chat.completions.create(
            model='ernie-lite-8k',
            messages=messages,
            temperature=0.7,
            top_p=0.8,
        )

        return {
            "analysis": response.choices[0].message.content,
            "metrics": {
                "like_rate": like_rate,
                "interaction_rate": interaction_rate,
                "duration": video_duration,
                "days_since_publish": days_since_publish if "days_since_publish" in locals() else None,

            }
        }
    except Exception as e:
        print(e)
        return {"error": "AI分析失败"}
