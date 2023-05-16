# from django.urls import path

# from . import views



# # é possivel nomear apps desta forma.
# # nao é preciso, mas no caso de da necessidade os links de html's devem mudar disto:

# # <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

# # para isto:

# # <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),

#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"), 
#     # path("specifics/<int:question_id>/", views.detail, name="detail"),

#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),

#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]