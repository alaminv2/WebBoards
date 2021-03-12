from django.shortcuts import render, HttpResponse, reverse, HttpResponseRedirect, get_object_or_404
from .models import Boards, Topics, Posts
from .forms import BoardForm, TopicForm
from django.http import Http404

# Create your views here.

def homeView(request):
    boards = Boards.objects.all()
    return render(request, 'home.html', context = {'boards' : boards})



def boardFormView(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_boards:home'))
    return render(request, 'board_form.html', {'form': form})



def topicsOfBoardView(request, board_id):
    board = get_object_or_404(Boards, pk=board_id)


    topic_list = board.topics.all()
    return render(request, 'topic_list_in_board.html', {'board': board, 'topics': topic_list})
    


def topicFormView(request):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_boards:home'))
    return render(request, 'topics_form.html', {'form': form})