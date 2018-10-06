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
choice_limited = ['skmr', 'normal', 'limited', ['', 'Tue', 'Wed', 'Thu', 'Fri']]

def select_song(song_array):
    song = random.choice(song_array)
    return song

def pull_song_list(attribute=None, difficulty=None, level=None, limited=None, party=None):
    song_list = songs.objects.all()

    if difficulty is not None:
        if difficulty in choice_difficulty:
            after_song_list = []
            for song in song_list:
                if song.check_exist_difficulty(difficulty):
                    after_song_list.append(song)
            song_list = after_song_list

    if attribute is not None:
        if attribute in choice_attribute:
            after_song_list = []
            for song in song_list:
                if song.check_exist_attribute(attribute):
                    after_song_list.append(song)
            song_list = after_song_list

    if limited is not None:
        if 'list' in str(type(limited)):
                after_song_list = []
                for song in song_list:
                    for limit in limited:
                        if song.check_exist_limited(limit):
                            after_song_list.append(song)
                song_list = after_song_list

        elif limited in choice_limited:
            if limited == 'skmr':
                song_list = convert_today_list(song_list)
            elif limited == 'normal':
                after_song_list = []
                for song in song_list:
                    if song.check_exist_limited(None):
                        after_song_list.append(song)
                song_list = after_song_list

            elif limited == 'limited':
                after_song_list = []
                for song in song_list:
                    if not song.check_exist_limited(None):
                        after_song_list.append(song)
                song_list = after_song_list


    return song_list

def convert_today_list(song_array):
    today = datetime.datetime.today()
    today_weeks = today.weekday()
    today_list = []
    for song in song_array:
        # 制限がない通常曲
        if song.check_empty_limited():
            today_list.append(song)

        # 全曲開放している月、土、日曜日
        elif today_weeks == 0 or today_weeks == 5 or today_weeks == 6:
            today_list.append(song)

        # 曜日に応じた開放している曲
        elif song.check_exist_limited(day_of_the_week[today_weeks]):
            today_list.append(song)

    return today_list

class IndexView(generic.TemplateView):
    template_name = 'selector/index.html'

def selector(request):
    def check_limited_filter(limited_filter):
        if limited_filter in choice_limited[3]:
            return True
        else:
            return False

    try:
        if request.method == 'POST':
            if request.POST['difficulty'] in choice_difficulty:
                difficulty = request.POST['difficulty']
            else:
                difficulty = None


            if request.POST['attribute'] in choice_attribute:
                attribute = request.POST['attribute']
            else:
                attribute = None

            if request.POST['limited'] is not None:
                if request.POST['limited'] == 'filters' and request.POST.getlist('filters[]'):
                    if 'list' in str(type(request.POST.getlist('filters[]'))):
                        after_filter = request.POST.getlist('filters[]')
                        for limited_filter in request.POST.getlist('filters[]'):
                            if not check_limited_filter(limited_filter):
                                limited = None
                                break
                            elif limited_filter == '':
                                index = after_filter.index(limited_filter)
                                after_filter[index] = None
                        else:
                            limited = after_filter

                    else:
                        limited = None
                    
                elif request.POST['limited'] in choice_limited:
                    limited = request.POST['limited']

                else:
                    limited = None


        else:
            error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。条件を絞る場合はやり直してください。'

            if request.POST['action'] == 'song_list':
                return render(request, 'selector/song_list.html', {'song_list': song_list, 'error_message': error_message,})

            select = select_song(pull_song_list())
            return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

        infomation_message = ''
        song_list = pull_song_list(difficulty=difficulty, attribute=attribute, limited=limited)

        if not song_list or len(song_list) == 0:
            song_list = pull_song_list()
            infomation_message = '絞り込み結果が0件だったのですべての曲、難易度から選曲しています。'

        if request.POST['action'] == 'song_list':
            return render(request, 'selector/song_list.html', {'song_list': song_list, 'infomation_message': infomation_message,})

        select = select_song(song_list)
        return render(request, 'selector/results.html', {'song': select, 'infomation_message': infomation_message,})
    except:
        import traceback
        traceback.print_exc()
        error_message = 'エラーが発生したためすべての曲、難易度から選曲しています。条件を絞る場合はやり直してください。'

        if request.POST['action'] == 'song_list':
            return render(request, 'selector/song_list.html', {'song_list': song_list, 'error_message': error_message,})

        select = select_song(pull_song_list())
        return render(request, 'selector/results.html', {'song': select, 'error_message': error_message,})

def produce(request):
    return render(request, 'selector/produce.html')
