import datetime, random

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Song as songs

# Create your views here.

day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
choice_difficulty = ['EASY', 'NORMAL', 'HARD', 'EXPERT']
choice_attribute = ['all', 'active', 'cool', 'pretty']

def select_song(song_array):
    count = len(song_array)
    index = random.randrange(0, count)
    return song_array[index]

# def pull_song_list(attribute=None, difficulty=None, level=None, limited=None, party=None):

#     # 難易度(difficulty)だけ指定
#     if attribute is None and difficulty is not None and level is None and limited is None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).order_by('id')

#     # 属性(attribute)と難易度(difficulty)指定
#     elif attribute is not None and difficulty is not None and level is None and limited is None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).filter(attribute=attribute).order_by('id')

#     # 属性(attribute)と難易度(difficulty)と限定(limited)指定
#     elif attribute is not None and difficulty is not None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).filter(attribute=attribute).filter(limited=limited).order_by('id')

#     # 難易度(difficulty)と限定(limited)指定
#     elif attribute is None and difficulty is not None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).filter(limited=limited).order_by('id')

#     # 属性(attribute)と限定(limited)指定
#     elif attribute is not None and difficulty is None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(attribute=attribute).filter(limited=limited).order_by('id')

#     # 属性(attribute)だけ指定
#     elif attribute is not None and difficulty is None and level is None and limited is None and party is None:
#         lists = songs.objects.filter(attribute=attribute).order_by('id')
#     # 属性(attribute)と難易度(difficulty)と限定(limited)指定
#     elif attribute is not None and difficulty is not None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).filter(attribute=attribute).filter(limited=limited).order_by('id')
#     # 属性(attribute)と限定(limited)指定
#     elif attribute is not None and difficulty is None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(attribute=attribute).filter(limited=limited).order_by('id')
#     # 難易度(difficulty)と限定(limited)指定
#     elif attribute is None and difficulty is not None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(difficulty=difficulty).filter(limited=limited).order_by('id')
#     # 限定(limited)だけ指定
#     elif attribute is None and difficulty is None and level is None and limited is not None and party is None:
#         lists = songs.objects.filter(limited=limited).order_by('id')
#     # 何も指定なし
#     elif attribute is None and difficulty is None and level is None and limited is None and party is None:
#         lists = songs.objects.all()

#     lists = convert_today_list(lists)
#     return lists

def pull_song_list(attribute=None, difficulty=None, level=None, limited=None, party=None):
    song_list = songs.objects.all()

    if difficulty is not None:
        if difficulty in choice_difficulty:
            after_song_list = []
            for song in song_list:
                if song.check_exist_difficulty(difficulty):
                    after_song_list.append(song)
            
            if after_song_list:
                song_list = after_song_list

    if attribute is not None:
        if attribute in choice_attribute:
            after_song_list = []
            for song in song_list:
                if song.check_exist_attribute(attribute):
                    after_song_list.append(song)

            if after_song_list:
                song_list = after_song_list

    # if limited is not None:
    #     if limited in choice_attribute:
    #         after_song_list = []
    #         for song in song_list:
    #             if song.check_exist_attribute(attribute):
    #                 after_song_list.append(song)

    #         if after_song_list:
    #             song_list = after_song_list

    return song_list

def convert_today_list(song_array):
    today = datetime.datetime.today()
    today_weeks = today.weekday()
    today_list = []
    for song in song_array:
        # 制限がない通常曲
        if song.empty_check_limited():
            today_list.append(song)

        # 全曲開放している月、土、日曜日
        elif today_weeks == 0 or today_weeks == 5 or today_weeks == 6:
            today_list.append(song)

        # 曜日に応じた開放している曲
        elif song.__limited == day_of_the_week[today_weeks]:
            today_list.append(song)

    return today_list

class IndexView(generic.TemplateView):
    template_name = 'selector/index.html'

def selector(request):
    try:
        if request.method == 'POST':
            if request.POST['difficulty'] == 'all':
                difficulty = None
            elif request.POST['difficulty'] in choice_difficulty:
                difficulty = request.POST['difficulty']
            else:
                difficulty = None


            if request.POST['attribute'] == 'none':
                attribute = None
            elif request.POST['attribute'] in choice_attribute:
                attribute = request.POST['attribute']
            else:
                attribute = None

            # if request.POST['limited'] is not None:
            #     print(request.POST['limited'])

        else:
            error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。条件を絞る場合はやり直してください。'

            select = select_song(pull_song_list())
            return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

        song_list = pull_song_list(difficulty=difficulty, attribute=attribute)

        if len(song_list) == 0:
            song_list = pull_song_list()

        select = select_song(song_list)
        return render(request, 'selector/results.html', {'song': select})
    except:
        error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。条件を絞る場合はやり直してください。'

        select = select_song(pull_song_list())
        return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

def produce(request):
    return render(request, 'selector/produce.html')
