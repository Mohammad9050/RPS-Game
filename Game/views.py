from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Game.forms import ObjGameForm
from Home.models import Profile
import redis
from django.conf import settings
import random

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


def home_view(request):
    user = request.user
    try:
        profile = request.user.profile
        wins = Profile.objects.values_list('win_record', flat=True).filter(id=profile.id).first()
        lost = Profile.objects.values_list('lost_record', flat=True).filter(id=profile.id).first()
    except:
        profile = ''
        wins = None
        lost = None
    return render(request, 'Game/home.html', {'pro': profile, 'win': wins, 'lost': lost, 'user':user})


@login_required
def game_view(request, num):
    profile = request.user.profile
    form = ObjGameForm(request.GET)
    obj_pc = random.choice(['rock', 'paper', 'scissor'])
    if form.is_valid():
        obj = form.cleaned_data['opinion']
        r.incr(f'round:{profile.id}')
        if (obj == 'rock' and obj_pc == 'scissor') or (obj == 'paper' and obj_pc == 'rock') or (
                obj == 'scissor' and obj_pc == 'paper'):

            r.incr(profile.id)

        elif (obj_pc == 'rock' and obj == 'scissor') or (obj_pc == 'paper' and obj == 'rock') or (
                obj_pc == 'scissor' and obj == 'paper'):
            r.incr(f'pc:{profile.id}')
    try:
        my_point = int(r.get(profile.id))
        pc_point = int(r.get(f'pc:{profile.id}'))
        round_game = int(r.get(f'round:{profile.id}'))
    except:
        r.set(profile.id, 0)
        r.set(f'pc:{profile.id}', 0)
        r.set(f'round:{profile.id}', 0)
        my_point = int(r.get(profile.id))
        pc_point = int(r.get(f'pc:{profile.id}'))
        round_game = int(r.get('round'))
    if my_point >= 3 or pc_point >= 3:
        r.set(profile.id, 0)
        r.set(f'pc:{profile.id}', 0)
        r.set(f'round:{profile.id}', 0)
        request.session['res'] = 'win' if my_point >= 3 else 'lost'
        if my_point >= 3:
            profile.balance += num
            profile.win_record += 1
        else:
            profile.balance -= num
            profile.lost_record += 1
        profile.computing_record()
        profile.save()

        return HttpResponseRedirect(reverse('Game:result'))
    context = {'pro': profile,
               'num': num,
               'form': form,
               'my_point': my_point,
               'pc_point': pc_point,
               'obj_pc': obj_pc,
               'round_game': round_game
               }
    if profile.balance >= num:
        # profile.balance -= num
        return render(request, 'Game/game.html', context)
    else:
        return HttpResponseRedirect(reverse('Game:home'))


def result_view(request):
    user = request.user
    res = request.session.get('res')
    return render(request, 'Game/result.html', {'res': res, 'user': user})


def leave_game(request, num):
    profile = request.user.profile
    profile.balance -= num
    profile.lost_record += 1
    profile.save()
    r.set(profile.id, 0)
    r.set(f'pc:{profile.id}', 0)
    r.set(f'round:{profile.id}', 0)
    return HttpResponseRedirect(reverse('Game:home'))


def table_view(request):
    try:
        pro = request.user.profile
    except:
        pro = None
    users = Profile.objects.all().order_by('-percent_record')[:10]
    return render(request, 'Game/table.html', {'users': users, 'pro': pro})
