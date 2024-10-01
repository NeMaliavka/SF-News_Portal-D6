from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    post_news = Post.objects.filter(post_type=Post.NEWS).order_by('created_at')
    template_name = 'news_list.html'
    return render(request, 'news_list.html', {'news': post_news})

def news_detail(request, pk):
    article = get_object_or_404(Post, id=pk)
    return render(request, 'news_detail.html', {'article': article})
# Create your views here.



# from datetime import datetime
#
# from django.views.generic import ListView, DetailView
# from .models import Product
#
#
# class ProductsList(ListView):
#     model = Product
#     ordering = 'name'
#     template_name = 'products.html'
#     context_object_name = 'products'
#
#     # Метод get_context_data позволяет нам изменить набор данных,
#     # который будет передан в шаблон.
#     def get_context_data(self, **kwargs):
#         # С помощью super() мы обращаемся к родительским классам
#         # и вызываем у них метод get_context_data с теми же аргументами,
#         # что и были переданы нам.
#         # В ответе мы должны получить словарь.
#         context = super().get_context_data(**kwargs)
#         # К словарю добавим текущую дату в ключ 'time_now'.
#         #context['time_now'] = datetime.now()
#         # Добавим ещё одну пустую переменную,
#         # чтобы на её примере рассмотреть работу ещё одного фильтра.
#         context['next_sale'] = "Распродажа в среду!"
#         return context
#
#
# class ProductDetail(DetailView):
#     model = Product
#     news = 'product.html'
#     context_object_name = 'product'