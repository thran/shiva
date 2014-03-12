from django.shortcuts import render, render_to_response
from django.views.generic import View


class Home(View):
    def get(self, request):

        return render(request, "home.html", {
            
        })


home = Home.as_view()