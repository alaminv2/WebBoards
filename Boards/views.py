from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse, reverse, HttpResponseRedirect, get_object_or_404
from .models import Boards, Topics, Posts
from .forms import BoardForm, TopicForm
from django.http import Http404

# Create your views here.

def homeView(request):
    boards = Boards.objects.all()
    return render(request, 'home.html', context = {'boards' : boards})


def newBoardView(request):
    pass


def boardFormView(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_boards:home'))
    return render(request, 'board_form.html', {'form': form})



def boardTopicsView(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)

    # topic_list = board.topics.all()
    return render(request, 'board_topics.html', {'board': board})
    


def topicFormView(request, board_id):
    board = Boards.objects.get(pk = board_id)
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.starter = request.user
            obj.board_id = board
            obj.save()
            return HttpResponseRedirect(reverse('app_boards:home'))
    return render(request, 'topics_form.html', {'form': form})


def newTopicView(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)
    usr = User.objects.first()
    print('user = ',usr)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board_id = board
            topic.starter = usr
            topic.save()

            Posts.objects.create(topic=topic, message=form.cleaned_data.get('message'), created_by=usr)
            return redirect('app_boards:board_topics', board_id=board.id)
    else:
        form = TopicForm()
    return render(request, 'new_topic.html', {'board' : board, 'form' : form})