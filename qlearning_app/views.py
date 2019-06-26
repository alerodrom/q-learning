import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from aux.numpy_encoder import NumpyEncoder
from qlearning.qlearning import Qlearning

from .forms import MapForm, ProblemForm
from .models import Result


class HomePageView(TemplateView):
    template_name = "app/home.html"


class CreateMap(CreateView):
    template_name = "app/create_map.html"
    form_class = MapForm
    success_url = "/create-problem/"
    # TODO comprobar que pos_init y pos_end sean tuplas y este dentro de los límites.


class CreateProblem(CreateView):
    template_name = "app/create_problem.html"
    form_class = ProblemForm
    success_url = "/"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()

        aux_map = self.object.map_related.path.split(',')
        base_map = [aux_map[k : k + 10] for k in range(0, len(aux_map), 10)]
        pos_init = (self.object.map_related.pos_init_y, self.object.map_related.pos_init_x)
        pos_end = (self.object.map_related.pos_end_y, self.object.map_related.pos_end_x)

        ql = Qlearning(
            init_zeros=self.object.np_zeros,
            print_steps=False,
            epochs=self.object.epochs,
            gamma=self.object.gamma,
            alpha=self.object.alpha,
            base_map=base_map,
            pos_init=pos_init,
            pos_end=pos_end
        )
        res = ql.call()
        maps = json.dumps(res["maps"], cls=NumpyEncoder)
        path = json.dumps(res["result"]["path"], cls=NumpyEncoder)
        result = Result.objects.create(
            problem=self.object,
            maps=maps,
            steps=res["result"]["steps"],
            reward=res["result"]["reward"],
            path=path,
        )
        return super().form_valid(form)

    def get_success_url(self):
        super().get_success_url()
        return reverse("result-detail", args=[self.object.result.id])


class ResultDetailView(DetailView):
    template_name = "app/result.html"

    model = Result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maps"] = json.loads(self.object.maps)
        context["path"] = json.loads(self.object.path)
        return context
