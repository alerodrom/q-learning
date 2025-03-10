"""qlearning_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from .views import CreateMap, CreateProblem, HomePageView, ResultDetailView, ResultListView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("create-map/", CreateMap.as_view(), name="create_map"),
    path("create-problem/", CreateProblem.as_view(), name="create_problem"),
    path("results/", ResultListView.as_view(), name="results-list"),
    path("result/<int:pk>/", ResultDetailView.as_view(), name="result-detail"),
]
