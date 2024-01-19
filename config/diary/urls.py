from django.urls import path
from .views import DiaryList, DiaryDetail, DiaryCreate, DiaryUpdate, DiaryDelete, DiarySearchView

app_name = 'diary'

urlpatterns = [
    path('', DiaryList.as_view(), name='diary_list'),
    # path('diary_list/', DiaryList.as_view(), name='diary_list'),
    path('diary_detail/<int:pk>/', DiaryDetail.as_view(), name='diary_detail'), 
    path('diary_create/', DiaryCreate.as_view(), name='diary_create'),
    path('diary_update/<int:pk>/', DiaryUpdate.as_view(), name='diary_update'),
    path('diary_delete/<int:pk>/', DiaryDelete.as_view(), name='diary_delete'),
    path('diary_search/', DiarySearchView.as_view(), name='diary_search'),
]

