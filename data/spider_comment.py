import csv
import time
import pandas as pd
import execjs
import requests
import urllib.parse

headers = {
    'cookie': 'enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740994ca6f2da69565c2a01035a50875ecaf0c312760fec8c5c0bf03b6aa08b120b5e9b10903b349dcfbeb73d8f588cfee76fcabd41ff46db88c58b2e268391dc2d653bdbf014e2ea65ace71fd371416539; x-web-secsdk-uid=22d7d8d0-6896-4eb6-842c-ed04f6e98149; douyin.com; device_web_cpu_core=24; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; hevc_supported=true; fpk1=U2FsdGVkX1+zzWh/WJwyCorTzgT0QhBvvMvvcjH445iCQJkQgXBUFNXCQNeiInRjOBcl4ZySElz66F/VB8ERBQ==; fpk2=7ddeda88d0c599cc494da0dece6554d5; s_v_web_id=verify_me27yg1u_IItkJS99_ZMOi_40Wr_A7Ee_lbdmPoG7KDr8; __security_mc_1_s_sdk_crypt_sdk=7679762c-43c1-acbd; bd_ticket_guard_client_web_domain=2; passport_csrf_token=9e282ca8e70ddbc75c6e7eca33e59119; passport_csrf_token_default=9e282ca8e70ddbc75c6e7eca33e59119; passport_mfa_token=CjUFVHWhDzWqrs9EzNiNXIOZjZX%2FGKn%2Bnr2n1feCGvaisrrpWzQI%2BioGn0CZIxXQOq3CI6YgDBpKCjwAAAAAAAAAAAAAT1NQdTsdUUXeNeUpqzd%2F7ecD%2BZStio66U197Ymd8xW7z7W0ADzTDW09ZRYIcryv8jSUQ3e%2F4DRj2sdFsIAIiAQNBmpJ2; d_ticket=b9972f03ac812f7e72830d918d29dbbd091d0; passport_assist_user=Cj3JTBHi50CVZvDWIYZtYUHCpi7uzFWkVU7MYW0BKqYvm5I0D1dEnkOTjpSHRZN-KEb0ZzT1_6ljQk7V97waGkoKPAAAAAAAAAAAAABPUwUmMDlTIUWJOoPZZQ_SnOD1fZUVyghHTgPCwyhe02nRz134Md6Ahe2QjG-TqA6vSRD47_gNGImv1lQgASIBA4Ah9L0%3D; n_mh=OZY669vrjzh4YqlmUT8i34yHm-zfRxfUd53wRpefO60; sid_guard=0ebaf1e5dae11d8074751b37af1d0339%7C1754620884%7C5184000%7CTue%2C+07-Oct-2025+02%3A41%3A24+GMT; uid_tt=126c08ebd441180f06b702166a280796; uid_tt_ss=126c08ebd441180f06b702166a280796; sid_tt=0ebaf1e5dae11d8074751b37af1d0339; sessionid=0ebaf1e5dae11d8074751b37af1d0339; sessionid_ss=0ebaf1e5dae11d8074751b37af1d0339; session_tlb_tag=sttt%7C14%7CDrrx5drhHYB0dRs3rx0DOf________-_aiUrMDdCCiS22JBwN76VZUT3oRrsbDBktsX2ikOyzlY%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KDk0YmVjMzdmY2M1NmFmNWY5YzI2ODA1N2FlMDRlNTc1NzkxNjNlNjYKHwj8ksGggQMQ1MfVxAYY7zEgDDDuvfLbBTgHQPQHSAQaAmxxIiAwZWJhZjFlNWRhZTExZDgwNzQ3NTFiMzdhZjFkMDMzOQ; ssid_ucp_v1=1.0.0-KDk0YmVjMzdmY2M1NmFmNWY5YzI2ODA1N2FlMDRlNTc1NzkxNjNlNjYKHwj8ksGggQMQ1MfVxAYY7zEgDDDuvfLbBTgHQPQHSAQaAmxxIiAwZWJhZjFlNWRhZTExZDgwNzQ3NTFiMzdhZjFkMDMzOQ; login_time=1754620884802; _bd_ticket_crypt_cookie=da1d2d1ca5030a6e815243bf1a2e6d68; __security_mc_1_s_sdk_sign_data_key_web_protect=adf270f2-41ba-b956; __security_mc_1_s_sdk_cert_key=8b7e4a9f-44c6-a5c5; __security_server_data_status=1; __ac_signature=_02B4Z6wo00f01Jc4UtAAAIDCdPeiRNCWzriXGFZAAE1g88; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740994ca6f2da69565c2a01035a50875ecaf0c312760fec8c5c0bf03b6aa08b120bcd4bed448d289e921d24033abbb49ca7e948fc1e934656b98ff7a2ea81a62db2761f96e8c8e6325e6c6a1bbe012ffa25b9b117f3fa6758baea3c865dc56bf7660b680c6f1a7a4f5670077fb2407d32d9f68528843113b507ba9b594fd847aeea54d6e58279a4320f5c8f2814e9fa20f9; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A24%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; SelfTabRedDotControl=%5B%5D; strategyABtestKey=%221754620889.021%22; is_dash_user=1; publish_badge_show_info=%220%2C0%2C0%2C1754620889335%22; SEARCH_RESULT_LIST_TYPE=%22single%22; volume_info=%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; xg_device_score=7.9032904526753285; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; csrf_session_id=1560a0c85e588b96ad9c6ca21a2eb26c; download_guide=%223%2F20250808%2F0%22; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSVcrdkFtUUcwVlIzb3AwcHVUUzZsU2xoamZ5MW11cTFDTVBHMXFyZ3E2QWNQRXlnd1NyMFc0UHp0NGU1UkQ2VCtiL2czZ0ZVR1hEUk1Jd2hpTVpqR1E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; ttwid=1%7C35jmYVFFjT1gLNulTPHg-czzVWp0MOKRQZJeU5rnxGw%7C1754625314%7Cb98c46ed7901f325262fc089c2cf4e53a2fa9e017bbe95d28a9a59d0ba55f865; biz_trace_id=fd4fc9ae; WallpaperGuide=%7B%22showTime%22%3A1754621003735%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A34%2C%22cursor2%22%3A10%7D; IsDouyinActive=true; odin_tt=42c41434718779dbbfa295f2eb23f4a03ee974ea01d40f19aa3c5da95d7e5ea58d9bac58077d3ed28ba8d965ab3f6e673b34de502d2103a9b048b9c023522437',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'accept': 'application/json, text/plain, */*'

}


def get_time(ctime):
    time_local = time.localtime(ctime)

    time_format = time.strftime("%Y.%m.%d", time_local)

    return str(time_format)


def get_json(aweme_id, cursor):
    url = f"https://www.douyin.com/aweme/v1/web/comment/list/?aid=6383&aweme_id={aweme_id}&count=20&cursor={cursor}"

    query = urllib.parse.urlparse(url).query
    a_bogus = execjs.compile(open('XB.js').read()).call('sign', query, headers.get('user-agent'))
    video_url = url + '&X-Bogus=' + a_bogus
    time.sleep(1)

    response = requests.get(video_url, headers=headers)

    return response.json()


def parseData(feed, aweme_id):
    ip_label = feed.get('ip_label', '')
    try:
        username = feed['user']['nickname']
    except:
        username = '暂无用户名'

    comment_dict = {
        '用户id': feed['user']['uid'],
        '用户名': username,
        '评论时间': get_time(feed['create_time']),
        'IP地址': ip_label,
        '评论内容': feed.get('text', ''),
        '点赞数量': feed.get('digg_count', ''),
        'aweme_id': aweme_id
    }
    print(comment_dict)
    writer.writerow(comment_dict)


def spier_comment(aweme_id):
    cursor = 0
    page = 1
    while True:
        response = get_json(aweme_id, cursor)
        try:
            if response['comments'] is None:
                break

            feeds = response['comments']
            for feed in feeds:
                parseData(feed, aweme_id)
            if response['has_more'] == 0:
                break
            cursor += 20

            page += 1
            if page > 20:
                break
        except Exception as e:
            print(f'爬取失败，错误：{e}')
            continue


if __name__ == "__main__":
    header = ['用户id', '用户名', '评论时间', 'IP地址', '评论内容', '点赞数量', 'aweme_id']
    f = open('comment_data.csv', 'a', encoding='utf-8', newline='')
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    df = pd.read_csv('data.csv')
    for index, row in df.iterrows():
        spier_comment(row['视频id'])
