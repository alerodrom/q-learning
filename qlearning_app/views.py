from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView

from qlearning.qlearning import Qlearning


class HomePageView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        ql = Qlearning(init_zeros=False, print_steps=False)
        result = ql.call()
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["maps"] = result["maps"]
        context["result"] = result["result"]
        messages.info(
            self.request,
            "Realizado en {} pasos con recompensa de {}".format(
                result["result"]["steps"], result["result"]["reward"]
            ),
        )
        return context
