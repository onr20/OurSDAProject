from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea,ModelForm
)

from datetime import date
from viewer.models import Genre, Movie
import re

  # This is a validator that checks if the value starts with a capital letter
  # If not, it throws an ValidationError Exception
def capitalized_validator(value):
    if value[0].islower():
      raise ValidationError('Value must be capitalized.')

class PastDateField(DateField):
    def validate(self, value):
      super().validate(value)
      if value >= date.today():
        raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
      result = super().clean(value)
      return date(year=result.year, month=result.month, day=1)

# class MovieForm(Form):
#     title = CharField(max_length=128)
#     genre = ModelChoiceField(queryset=Genre.objects)  # To choose a Genre from the model (table) Genre
#     rating = IntegerField(min_value=1, max_value=10)
#     released = PastDateField()
#     description = CharField(widget=Textarea, required=False)
#
#     def clean_description(self):
#         # Force each sentence of the description to be capitalized.
#         initial = self.cleaned_data['description']
#         sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
#         return '. '.join(sentence.capitalize() for sentence in sentences)
#
#     def clean(self):
#         result = super().clean()
#         if result['genre'].name == 'Comedy' and result['rating'] > 5:
#             self.add_error('genre', 'Comedy Genre')
#             self.add_error('rating', f'Rating:  {result["rating"]}')
#             raise ValidationError(
#                 "Comedies aren't so good to be rated over 5."
#             )
#         return result



class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"