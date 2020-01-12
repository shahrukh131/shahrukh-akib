from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Corey Ms',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 11,2020'
    },
    {
        'author': 'Shahrukh akib',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 12,2020'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
