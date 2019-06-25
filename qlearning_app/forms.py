from django.forms import ModelForm, DateInput, TimeInput
from .models import Map, Problem, Result


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = "__all__"


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = "__all__"


class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = "__all__"
