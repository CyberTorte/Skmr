import datetime, random

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import song as songs

# Create your views here.

day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def select_song(song_array):
    count = len(song_array)
    index = random.randrange(0, count)
    return song_array[index]

def pull_song_list(attribute=None, difficulty=None, level=None, limited=None, party=None):
    # 難易度(difficulty)だけ指定
    if attribute is None and difficulty is not None and level is None and limited is None and party is None:
        lists = songs.objects.filter(difficulty=difficulty).order_by('id')
    # 属性(attribute)と難易度(difficulty)指定
    elif attribute is not None and difficulty is not None and level is None and limited is None and party is None:
        lists = songs.objects.filter(difficulty=difficulty).filter(attribute=attribute).order_by('id')
    # 属性(attribute)と難易度(difficulty)と限定(limited)指定
    elif attribute is not None and difficulty is not None and level is None and limited is not None and party is None:
        pass
    # 何も指定なし
    elif attribute is None and difficulty is None and level is None and limited is None and party is None:
        lists = songs.objects.all()

    lists = convert_today_list(lists)
    return lists

def convert_today_list(song_array):
    today = datetime.datetime.today()
    today_weeks = today.weekday()
    today_list = []
    for song in song_array:
        if check_not_date_limited(song):

            # 制限がない通常曲
            if song.empty_check_limited():
                today_list.append(song)

            # 全曲開放している月、土、日曜日
            elif today_weeks == 0 or today_weeks == 5 or today_weeks == 6:
                today_list.append(song)

            # 曜日に応じた開放している曲
            elif song.limited == day_of_the_week[today_weeks]:
                today_list.append(song)

        # イベント曲の場合
        else :
            try:
                # 期限が過ぎていない場合
                if today < datetime.datetime.strptime(song.limited, "%Y/%m/%d %H:%M:%S"):
                    today_list.append(song)
            except ValueError:
                pass
    return today_list

def check_not_date_limited(limited):
    if limited.empty_check_limited():
        return True
    else:
        for week in day_of_the_week:
            if limited.limited == week:
                return True

    return False

class IndexView(generic.TemplateView):
    template_name = 'selector/index.html'

def selector(request):
    try:
        if request.method == 'POST':
            if request.POST['difficulty'] == 'all':
                difficulty = None
            else:
                difficulty = request.POST['difficulty']

            if request.POST['attribute'] == 'none':
                attribute = None
            else:
                attribute = request.POST['attribute']

        else:
            difficulty = None
            attribute = None
            error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。<br> 条件を絞る場合はやり直してください。'

            select = select_song(pull_song_list(difficulty=difficulty, attribute=attribute))
            return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

        select = select_song(pull_song_list(difficulty=difficulty, attribute=attribute))
        return render(request, 'selector/results.html', {'song': select})
    except:
        difficulty = None
        attribute = None
        error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。<br> 条件を絞る場合はやり直してください。'

        select = select_song(pull_song_list(difficulty=difficulty, attribute=attribute))
        return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

def produce(request):
    return render(request, 'selector/produce.html')
