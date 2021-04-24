from django.shortcuts import render
from .models import Movie
from django.views import View
from django.views.generic import TemplateView, ListView,FormView, CreateView, UpdateView, DeleteView , DetailView
from .forms import MovieForm, GenreForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from logging import getLogger
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
LOGGER = getLogger()
from django.http import HttpResponse


# Create your views here.
def hello(request, s0):
    s1 = request.GET.get('s1', '')  # Get the variable s1 from the URL encoder
    return render(
        request, template_name='viewer/hello.html',  # Template is the file you want to load
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']} # context are the variable you send to the template
    )
# Function view to show movies
def movie_list(request):
    movie_list = Movie.objects.all()
    return render(
        request,
        template_name="viewer/movies.html",
        context={'movies': movie_list}
    )
# Class based view to show movies
class MoviesView(View):
    def get(self, request):
        movie_list = Movie.objects.all()
        return render(
            request,
            template_name="viewer/movies.html",
            context={'movies': movie_list}
        )

# Template View class
class MoviesViewTemplate(TemplateView):
    template_name = "viewer/movies.html"
    extra_context = {'movies': Movie.objects.all()}

class MoviesViewList(ListView):
  template_name = 'viewer/movies.html'
  model = Movie



# class MovieCreateView(FormView):
#     template_name = "viewer/movie_form.html"
#     form_class = MovieForm
#     success_url = reverse_lazy("movies")
#     def form_valid(self, form):
#         result = super().form_valid(form) # Validate the form
#         cleaned_data = form.cleaned_data # Get me the data from the form
#         Movie.objects.create(
#             title=cleaned_data['title'],
#             genre=cleaned_data['genre'],
#             rating=cleaned_data['rating'],
#             released=cleaned_data['released'],
#             description=cleaned_data['description']
#         )
#         return result
#     def form_invalid(self, form):
#         LOGGER.warning('User provided invalid data.')
#         return super().form_invalid(form)

class StaffRequiredMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_staff



class MovieListView(ListView):
  template_name = 'movie_list.html'





class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = 'viewer/movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy("movies")
    permission_required = 'viewer.add_movie'



    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class GenreCreateView(CreateView):
    template_name = 'viewer/form.html'
    form_class = GenreForm
    success_url = reverse_lazy("new_genre")


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView, StaffRequiredMixin):

  template_name = 'viewer/form.html'
  model = Movie
  form_class = MovieForm
  success_url = reverse_lazy('movies')
  permission_required = 'viewer.change_movie'

  def form_invalid(self, form):
    LOGGER.warning('User provided invalid data while updating a movie.')
    return super().form_invalid(form)

class MovieDeleteView(LoginRequiredMixin, PermissionRequiredMixin, StaffRequiredMixin,  DeleteView):
    template_name = 'viewer/delete_form.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


class MovieDetailView(DetailView):
    template_name = 'viewer/movie_detail.html'
    model = Movie
    success_url = reverse_lazy('movies')










