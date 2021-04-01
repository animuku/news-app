from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(LoginRequiredMixin,ListView):
    template_name='app/home.html'
    model = Article
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.profile.sources:
            list_of_sources = self.request.user.profile.sources.split(",")
            return Article.objects.filter(source__in= list_of_sources).order_by('-date_posted')
        # print(list_of_sources)
        else:
            return Article.objects.all()
def about(request):
    return render(request,"app/about.html",{"title":"About"})