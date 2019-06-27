from django.forms import DateInput, ModelForm, TimeInput
from django.forms.widgets import NumberInput

from .models import Map, Problem, Result


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = "__all__"


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = "__all__"
        widgets = {
            "epochs": NumberInput(attrs={"min": 50, "max": 10000}),
            "gamma": NumberInput(attrs={"min": 0.0, "max": 1.0, "step": ".01"}),
            "alpha": NumberInput(attrs={"min": 0.0, "max": 1.0, "step": ".01"}),
        }


class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = "__all__"
