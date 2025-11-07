import json
import re
from collections import Counter

import pandas as pd
from django.shortcuts import render
from project_logger import Paginator
from project_logger import JsonResponse
from project_logger import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

import util
from video.models import User, VideoData, CommentData
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        password = request.POST.get("password")
        print(uname, password)
        try:
            user = User.objects.get(username=uname, password=password)
            request.session['username'] = uname
            request.session['uid'] = user.id
            return redirect('/home/index/')
        except:
            messages.error(request, "请输入正确的用户名和密码")
            return HttpResponseRedirect('/home/login/')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=uname)
            messages.error(request, '用户已存在')
            return HttpResponseRedirect('/home/register/')
        except:
            User.objects.create(username=uname, password=password)
            messages.success(request, '注册成功')
            return HttpResponseRedirect("/home/login/")
    else:
        return render(request, 'register.html')


def index(request):
    maxData = VideoData.objects.count()
    maxLike = VideoData.objects.order_by('-likeCount').first().likeCount
    maxComment = VideoData.objects.order_by('-commentCount').first().commentCount
    maxCollect = VideoData.objects.order_by('-collectCount').first().collectCount

    # 查询可视化图表数据
    sql = 'select * from part2'
    res = util.query(sql)
    xData = [i[2] for i in res]
    xData1 = [i[0] for i in res]
    xData2 = [i[1] for i in res]
    xData3 = [i[3] for i in res]

    page = request.GET.get("page", 1)
    per_page = 10
    all_data = VideoData.objects.all().order_by("-id")
    paginator = Paginator(all_data, per_page)
    page_obj = paginator.get_page(page)
    content = {
        'maxData': maxData,
        'maxLike': maxLike,
        'maxComment': maxComment,
        'maxCollect': maxCollect,
        'xData': xData,
        'xData1': xData1,
        'xData2': xData2,
        'xData3': xData3,
        'page_obj': page_obj,
    }
    return render(request, 'index.html', content)


def comment_list(request):
    page = request.GET.get('page', 1)

    comment_info = CommentData.objects.all()
    per_page = 10
    paginator = Paginator(comment_info, per_page)
    page_obj = paginator.get_page(page)

    content = {
        'page_obj': page_obj
    }
    return render(request, 'comment_list.html', content)


def part1(request):
    sql = 'select * from part1'
    res = util.query(sql)

    result = []
    for i in res:
        result.append({'name': i[0], 'value': i[1]})

    return render(request, 'part1.html', {'result': result})


def part2(request):
    sql1 = 'select * from part3'
    res = util.query(sql1)
    result = []
    for i in res:
        result.append({"value": i[1], "name": i[0]})

    sql2 = 'select * from part4'
    res = util.query(sql2)

    name_list = [i[0] for i in res]
    value_list = [i[1] for i in res]
    content = {
        'result': result,
        'name_list': name_list,
        'value_list': value_list,
    }
    return render(request, 'part2.html', content)


from project_logger import messages


def part3(request):
    sql = 'select * from part5'
    res = util.query(sql)

    value_list1 = [i[0] for i in res]
    value_list2 = [i[1] for i in res]
    name_list = [i[2] for i in res]

    df = pd.read_csv('./data/nlp_result.csv')
    chinese_word_pattern = re.compile(r'^[\u4e00-\u9fff]+$')
    all_words = []
    for segmented_text in df['segmented']:
        if isinstance(segmented_text, str):
            words = segmented_text.strip()
            chinese_words = [word for word in words if chinese_word_pattern.fullmatch(word)]
            all_words.extend(chinese_words)

    word_counts = Counter(all_words)

    word_counts_list = [{"name": word, "value": count} for word, count in word_counts.items()]

    content = {
        'value_list1': value_list1,
        'value_list2': value_list2,
        'name_list': name_list,
        'word_counts_list': word_counts_list[:100],
    }

    return render(request, 'part3.html', content)


from project_logger import messages


def part4(request):
    df = pd.read_csv('./data/nlp_result.csv')
    bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    labels = ['0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5',
              '0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1.0']

    df['score_group'] = pd.cut(df['scores'].astype(float), bins=bins, labels=labels)

    score_counts = df['score_group'].value_counts()

    name_list = []
    value_list = []
    for k, v in score_counts.items():
        name_list.append(k)
        value_list.append(v)

    scoresDict = {"积极": 0, "消极": 0, "中性": 0}

    for i in df['scores']:
        if float(i) < 0.5:
            scoresDict['消极'] += 1
        elif float(i) == 0.5:
            scoresDict['中性'] += 1
        elif float(i) > 0.5 and float(i) < 1.0:
            scoresDict['积极'] += 1

    result = []
    for k, v in scoresDict.items():
        result.append({"value": v, "name": k})
    content = {
        'name_list': name_list,
        'value_list': value_list,
        'result': result,
    }

    return render(request, 'part4.html', content)


def part5(request):
    return render(request, 'part5.html')


def part6(request):
    return render(request, 'part6.html')


from forecast import predict_likes


def predict(request):
    if request.method == 'POST':
        try:
            input_data = {
                'duration': float(request.POST.get('duration')),
                'collect': float(request.POST.get('collect')),
                'comment': float(request.POST.get('comment')),
                'share': float(request.POST.get('share')),
                'fans': float(request.POST.get('fans')),
                'interaction_rate': float(request.POST.get('interaction_rate')),
                'hour': int(request.POST.get('hour')),
            }
            prediction = predict_likes(input_data)
            return render(request, 'predict.html',
                          {'preResult': prediction, 'inputData': input_data, 'showResult': True})
        except:

            return None
    else:
        return render(request, 'predict.html')


from Get_Qianfan import analyze_single_viedo


def get_ai(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        result = analyze_single_viedo({
            '粉丝数量': int(data.get('fans', 0)),
            '发表时间': data.get('publish_date', ''),
            '视频描述': data.get('description', ''),
            '视频时长': data.get('duration', ''),
            '点赞数量': int(data.get('likes', 0)),
            '收藏数量': int(data.get('favorites', 0)),
            '评论数量': int(data.get('comments', 0)),
            '分享数量': int(data.get('shares', 0))
        }, data.get('analysis_focus'))

        return JsonResponse(result)
    else:
        return render(request, 'get_ai.html')


def changeInfo(request):
    uid = request.session.get('uid')
    userInfo = User.objects.get(id=uid)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        print(user_id)
        oldPwd = request.POST.get('oldPwd')
        newPwd = request.POST.get('newPwd')
        chkPwd = request.POST.get('chkPwd')
        user = User.objects.get(id=user_id)
        if newPwd != chkPwd:
            js_code = """
            <script>
            alert("两次输入密码不一致")
            window.location.href = "/home/changeInfo/";
            </script>
            """
            return HttpResponse(js_code)
        elif oldPwd != user.password:
            js_code = """
                        <script>
                        alert("原始密码错误")
                        window.location.href = "/home/changeInfo/";
                        </script>
                        """
            return HttpResponse(js_code)
        else:
            user.password = newPwd
            js_code = """
                                    <script>
                
                                    window.location.href = "/home/changeInfo/";
                                    </script>
                                    """
            return HttpResponse(js_code)
    else:
        return render(request, 'changeInfo.html', {'userInfo': userInfo})


def logout(request):
    request.session.clear()

    return redirect('login')
