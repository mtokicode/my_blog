from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Diary    

class DiaryList(ListView):
    model = Diary
    template_name = 'diary_list.html'
    search_result = Diary.objects.filter(content__icontains="ベース")
    print(search_result) 
     
class DiaryDetail(DetailView):
    model =  Diary
    template_name = 'diary_detail.html'

class DiaryCreate(CreateView):
    model = Diary
    template_name = 'diary_create.html'
    fields = ['title', 'content']
    fields = ['title', 'content']
    success_url = reverse_lazy('diary:diary_list')

class DiaryUpdate(UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    fields = ['title', 'content',]
    success_url = reverse_lazy('diary:diary_list')

class DiaryDelete(DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

class DiarySearchView(View):

    def get(self, request):
        
        keyword = request.GET.get('k', None)
        # keyword = "test"
        search_result = Diary.objects.filter(title__icontains=keyword)
        print(search_result)
        params = {'keyword': keyword,
                  'search_result': search_result}
        return render(request, 'diary_search.html', params)
