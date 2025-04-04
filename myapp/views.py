from django.shortcuts import render

# render возвращает шаблон html на запрос пользователя
def main(request):
    return render(request, 'main.html')
 
def author(request):
    return render(request, 'author.html')

def fishshop(request):
    return render(request, 'fishshop.html')

