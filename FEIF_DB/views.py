from collections import defaultdict

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Character, WeaponCategory, Item, Skill,Job
from django.http import HttpResponse, Http404
# Create your views here.
def index(request):
    # 你的主页逻辑
    return render(request, 'index.html')

def character_list(request):
    selected_storyline = request.GET.get('storyline', 'A')
    storylines=Character.STORYLINES
    characters = Character.objects.filter(storyline=selected_storyline)
    rend=render(request, 'character_list.html', { 'characters': characters,
        'selected_storyline': selected_storyline,'storylines': storylines})
    return HttpResponse(rend)
def weapon_list(request):
    categories = WeaponCategory.objects.prefetch_related('weapons').all()
    return render(request, 'weapon_list.html', {'categories': categories})
def item_list(request):
    items = Item.objects.all()
    rend=render(request, 'item_list.html', {'items':items})
    return HttpResponse(rend)
def skill_list(request):
    skills = Skill.objects.all()
    rend= render(request,"skills.html",{'skills':skills})
    return HttpResponse(rend)
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    storyline_map = dict(Character.STORYLINES)  # 从模型里取故事线映射
    storyline_name = storyline_map.get(character.storyline, "Unknown")  # 根据角色的storyline字段找名字
    return render(request, 'character_detail.html', {'character': character,'storyline_name': storyline_name,})
def class_list(request):
    classes = Job.objects.all().order_by('Allegiance', 'title')

    rend = render(request, 'class_list.html', {'classes': classes})
    return HttpResponse(rend)
def class_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    rend = render(request, 'class_detail.html', {'job': job})
    return HttpResponse(rend)