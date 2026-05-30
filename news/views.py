from django.shortcuts import render,redirect
from .models import News
# Create your views here.

def news_list(request):
    newz = News.objects.all().order_by('-id')
    context = {
        'newz': newz
    }
    return render(request, 'news_list.html', context)

def news_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        News.objects.create(title=title, content=content, image=image)

        return redirect('news-list')

    return render(request, 'news_create.html')

def news_detail(request, pk):
    new = News.objects.filter(pk=pk).first()

    context = {
        'new': new
    }

    return render(request, 'news_detail.html', context)


def news_update(request, pk):
    new = News.objects.filter(pk=pk).first()

    if request.method == 'POST':
        new.title = request.POST.get('title')
        new.content = request.POST.get('content')

        if request.FILES.get('image'):
            new.image = request.FILES.get('image')

        new.save()

        return redirect('news-detail', pk=new.pk)

    context = {
        'new': new
    }

    return render(request, 'news_update.html', context)

def news_delete(request, pk):
    new = News.objects.filter(pk=pk).first()

    if request.method == 'POST':
        new.delete()
        return redirect('news-list')

    context = {
        'new': new
    }
    return render(request, 'news_delete.html', context)
