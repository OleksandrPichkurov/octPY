from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.index_other, name='index'),
    path('question/', views.QuestionList.as_view(), name='list'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='details'),
    path('question/<int:question_id>/choice/', views.ChoiceList.as_view(), name='choice-list'),
]
