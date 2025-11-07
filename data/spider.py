import random
import time
import csv

import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "priority": "u=1, i",
    "referer": "https://www.douyin.com/root/search/%E5%93%AA%E5%90%922?aid=8f6341cc-39e3-4272-a6d5-33e2b6e49203&type=general",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "uifid": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740994ca6f2da69565c2a01035a50875ecaf0c312760fec8c5c0bf03b6aa08b120bcd4bed448d289e921d24033abbb49ca7e948fc1e934656b98ff7a2ea81a62db2761f96e8c8e6325e6c6a1bbe012ffa25b9b117f3fa6758baea3c865dc56bf7660b680c6f1a7a4f5670077fb2407d32d9f68528843113b507ba9b594fd847aeea54d6e58279a4320f5c8f2814e9fa20f9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "enter_pc_once": "1",
    "UIFID_TEMP": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740994ca6f2da69565c2a01035a50875ecaf0c312760fec8c5c0bf03b6aa08b120b5e9b10903b349dcfbeb73d8f588cfee76fcabd41ff46db88c58b2e268391dc2d653bdbf014e2ea65ace71fd371416539",
    "x-web-secsdk-uid": "22d7d8d0-6896-4eb6-842c-ed04f6e98149",
    "douyin.com": "",
    "device_web_cpu_core": "24",
    "device_web_memory_size": "8",
    "architecture": "amd64",
    "dy_swidth": "1920",
    "dy_sheight": "1080",
    "hevc_supported": "true",
    "fpk1": "U2FsdGVkX1+zzWh/WJwyCorTzgT0QhBvvMvvcjH445iCQJkQgXBUFNXCQNeiInRjOBcl4ZySElz66F/VB8ERBQ==",
    "fpk2": "7ddeda88d0c599cc494da0dece6554d5",
    "s_v_web_id": "verify_me27yg1u_IItkJS99_ZMOi_40Wr_A7Ee_lbdmPoG7KDr8",
    "__security_mc_1_s_sdk_crypt_sdk": "7679762c-43c1-acbd",
    "bd_ticket_guard_client_web_domain": "2",
    "passport_csrf_token": "9e282ca8e70ddbc75c6e7eca33e59119",
    "passport_csrf_token_default": "9e282ca8e70ddbc75c6e7eca33e59119",
    "passport_mfa_token": "CjUFVHWhDzWqrs9EzNiNXIOZjZX%2FGKn%2Bnr2n1feCGvaisrrpWzQI%2BioGn0CZIxXQOq3CI6YgDBpKCjwAAAAAAAAAAAAAT1NQdTsdUUXeNeUpqzd%2F7ecD%2BZStio66U197Ymd8xW7z7W0ADzTDW09ZRYIcryv8jSUQ3e%2F4DRj2sdFsIAIiAQNBmpJ2",
    "d_ticket": "b9972f03ac812f7e72830d918d29dbbd091d0",
    "passport_assist_user": "Cj3JTBHi50CVZvDWIYZtYUHCpi7uzFWkVU7MYW0BKqYvm5I0D1dEnkOTjpSHRZN-KEb0ZzT1_6ljQk7V97waGkoKPAAAAAAAAAAAAABPUwUmMDlTIUWJOoPZZQ_SnOD1fZUVyghHTgPCwyhe02nRz134Md6Ahe2QjG-TqA6vSRD47_gNGImv1lQgASIBA4Ah9L0%3D",
    "n_mh": "OZY669vrjzh4YqlmUT8i34yHm-zfRxfUd53wRpefO60",
    "sid_guard": "0ebaf1e5dae11d8074751b37af1d0339%7C1754620884%7C5184000%7CTue%2C+07-Oct-2025+02%3A41%3A24+GMT",
    "uid_tt": "126c08ebd441180f06b702166a280796",
    "uid_tt_ss": "126c08ebd441180f06b702166a280796",
    "sid_tt": "0ebaf1e5dae11d8074751b37af1d0339",
    "sessionid": "0ebaf1e5dae11d8074751b37af1d0339",
    "sessionid_ss": "0ebaf1e5dae11d8074751b37af1d0339",
    "session_tlb_tag": "sttt%7C14%7CDrrx5drhHYB0dRs3rx0DOf________-_aiUrMDdCCiS22JBwN76VZUT3oRrsbDBktsX2ikOyzlY%3D",
    "is_staff_user": "false",
    "sid_ucp_v1": "1.0.0-KDk0YmVjMzdmY2M1NmFmNWY5YzI2ODA1N2FlMDRlNTc1NzkxNjNlNjYKHwj8ksGggQMQ1MfVxAYY7zEgDDDuvfLbBTgHQPQHSAQaAmxxIiAwZWJhZjFlNWRhZTExZDgwNzQ3NTFiMzdhZjFkMDMzOQ",
    "ssid_ucp_v1": "1.0.0-KDk0YmVjMzdmY2M1NmFmNWY5YzI2ODA1N2FlMDRlNTc1NzkxNjNlNjYKHwj8ksGggQMQ1MfVxAYY7zEgDDDuvfLbBTgHQPQHSAQaAmxxIiAwZWJhZjFlNWRhZTExZDgwNzQ3NTFiMzdhZjFkMDMzOQ",
    "login_time": "1754620884802",
    "_bd_ticket_crypt_cookie": "da1d2d1ca5030a6e815243bf1a2e6d68",
    "__security_mc_1_s_sdk_sign_data_key_web_protect": "adf270f2-41ba-b956",
    "__security_mc_1_s_sdk_cert_key": "8b7e4a9f-44c6-a5c5",
    "__security_server_data_status": "1",
    "__ac_nonce": "0689563d40054549444d3",
    "__ac_signature": "_02B4Z6wo00f01Jc4UtAAAIDCdPeiRNCWzriXGFZAAE1g88",
    "UIFID": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740994ca6f2da69565c2a01035a50875ecaf0c312760fec8c5c0bf03b6aa08b120bcd4bed448d289e921d24033abbb49ca7e948fc1e934656b98ff7a2ea81a62db2761f96e8c8e6325e6c6a1bbe012ffa25b9b117f3fa6758baea3c865dc56bf7660b680c6f1a7a4f5670077fb2407d32d9f68528843113b507ba9b594fd847aeea54d6e58279a4320f5c8f2814e9fa20f9",
    "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A24%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22",
    "SelfTabRedDotControl": "%5B%5D",
    "strategyABtestKey": "%221754620889.021%22",
    "is_dash_user": "1",
    "publish_badge_show_info": "%220%2C0%2C0%2C1754620889335%22",
    "SEARCH_RESULT_LIST_TYPE": "%22single%22",
    "passport_fe_beating_status": "false",
    "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSVcrdkFtUUcwVlIzb3AwcHVUUzZsU2xoamZ5MW11cTFDTVBHMXFyZ3E2QWNQRXlnd1NyMFc0UHp0NGU1UkQ2VCtiL2czZ0ZVR1hEUk1Jd2hpTVpqR1E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D",
    "home_can_add_dy_2_desktop": "%221%22",
    "volume_info": "%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D",
    "odin_tt": "fe0123dcfcbde778f3f6fc5d3f60845b9896022b425386dbe5ae41c39452563ca15d5074cddb6b5343a24a2d12a2088aeb69591b177340a149c8132e4803f668acd6cdf91c6b6b2125bcea878f214484",
    "ttwid": "1%7C35jmYVFFjT1gLNulTPHg-czzVWp0MOKRQZJeU5rnxGw%7C1754621182%7C3e619018ac6235645b4c3f41e9fb5686f784be70b3b25e8608287c50c85ad9e4",
    "biz_trace_id": "f2a83325",
    "sdk_source_info": "7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273d3234363d3434373331303234272927676c715a75776a716a666a69273f2763646976602778",
    "bit_env": "AfwAtRa-lwm2FwzlnkJ2jvEpaCF0EWFBAH-96V_rfWewsguhFufFsUrWTwvV7JAdHaA9CH127Ol1v9bELt1k5uQH4VeaIt5QqRHJ4dk_LK706CVPdlnDPudhX3eodpxeNzNYRsFM7pKs5DxnSV7YEDzbA9Zte8-C0AJ5BFNoOxPTkDsD7m-vLtItetSrfAEDmc6eFc9-wD-bQ50g1kLLNhaVjdNR1fqJCgUv7E0JnNj-GTd0DusJ9dQj9Ye3M22Bke4Ki1cqi6gt1zVH1kFSm_aI1gNlQ2_58p9is43S8eu6_d6PsNy1cwq0fYnXkrDlk0QWcLmY88cOzNzL2QbphP-xIlKLxUmBPdb0VDTonaem3T_Ko0fHpepa6RLvlE9AvapFJ72YeSZA7ewvr89sRt2wB5_3BYOZfB4qsc3ij7ZW8I-oYT_NDeNcV78ubAVqpcyQtOY3AyFqgotcYzPaaUBcSWB_62-rVogJS9aIOV77pOl82RnYRBTSd5VS1tKB",
    "gulu_source_res": "eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9",
    "passport_auth_mix_state": "yam6nlo306croh34bnp9su0gmia13waa",
    "WallpaperGuide": "%7B%22showTime%22%3A1754621003735%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%7D",
    "xg_device_score": "7.9032904526753285",
    "download_guide": "%222%2F20250808%2F0%22",
    "stream_player_status_params": "%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22",
    "IsDouyinActive": "true"
}
url = "https://www.douyin.com/aweme/v1/web/search/item/"


def get_time(ctime):
    time_local = time.localtime(ctime)

    time_format = time.strftime("%Y.%m.%d", time_local)

    return str(time_format)


def get_json(keyword, offset, count):
    params = {
        'aid': 6383,
        'channel': 'channel_pc_web',
        'search_channel': 'aweme_video_web',
        'keyword': keyword,
        'offset': offset,
        'is_filter_search': 0,
        'publish_time': 0,
        'sort_type': 0,
        'update_version_code': 170400,
        'search_id': '20240722171308885F77C62F5C930657D3',
        'count': count,
        'need_filter_settings': 0
    }
    time.sleep(random.randint(1, 5))
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    return response.json()


def parseData(response):
    global video_dict
    minutes = response['video']['duration'] // 1000 // 60
    seconds = response['video']['duration'] // 1000 % 60
    video_dict = {
        '用户名': response['author']['nickname'].strip(),
        '粉丝数量': response['author']['follower_count'],
        '视频描述': response['desc'],
        '视频id': response['aweme_id'],
        '发表时间': get_time(response['create_time']),
        '视频时长': "{:02d}:{:02d}".format(minutes, seconds),
        '点赞数量': response['statistics']['digg_count'],
        '收藏数量': response['statistics']['collect_count'],
        '评论数量': response['statistics']['comment_count'],
        '分享数量': response['statistics']['share_count'],
        '下载数量': response['statistics']['download_count'],
    }

    print(video_dict)
    writer.writerow(video_dict)


def search(keyword):
    offset = 0
    count = 16
    while True:
        response = get_json(keyword, offset, count)

        feeds = response['data']
        for feed in feeds:
            parseData(feed['aweme_info'])
        if response['has_more'] == 0:
            break

        offset = offset + count
        count = 10


if __name__ == "__main__":
    # keyword = input('')

    header = ['用户名', '粉丝数量', '视频描述', '视频id', '发表时间', '视频时长', '点赞数量', '收藏数量', '评论数量', '分享数量', '下载数量']
    f = open('data.csv', 'a', encoding='utf-8', newline='')
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    keyword = '哪吒2'
    search(keyword)
