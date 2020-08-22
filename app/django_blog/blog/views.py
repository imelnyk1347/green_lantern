from django.shortcuts import render


def posts_list(request):
    n = ['Svitlana Melnyk', 'Ihor Melnyk', 'Melnyk Serhiy', 'Melnyk Bohdan', 'Melnyk Liydmyla']
    return render(request, 'blog/index.html', context={'names': n})
