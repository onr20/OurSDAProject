from django.contrib import admin
from django.urls import path, include
from viewer.views import hello, MoviesView, MoviesViewTemplate,MoviesViewList,MovieCreateView, GenreCreateView , MovieDeleteView

from viewer.views import MovieUpdateView, MovieDeleteView, MovieDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<s0>/', hello, name="hello"),
    path('', MoviesViewList.as_view(), name="movies"),  # TEmplate Class based view-
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/new_genre/', GenreCreateView.as_view(), name='new_genre'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/detail/<pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('accounts/',include('accounts.urls', namespace= 'accounts')),
]
