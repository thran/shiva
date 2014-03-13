import datetime
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
from django.views.generic import View
from faces.models import Face, Guess, Chat
from shiva import settings


class Faces(View):
    def get(self, request, selected_pk=None):
        faces = Face.objects.all().order_by("photo")
        faces_list = []
        for f in faces:
            face = {}
            faces_list.append(face)

            solved = f.is_solved()
            face["pk"] = f.pk
            if selected_pk and f.pk == int(selected_pk):
                face["guesses"] = list(f.guess_set.order_by("-pk").values())
            if solved:
                face["solved"] = True
                face["name"] = f.name
            face["photo"] = f.photo.url
            face["photo_thumb"] = settings.MEDIA_URL + f.photo_thumb
            face["hint"] = f.hint

        return HttpResponse(json.dumps(faces_list))

get_faces = Faces.as_view()


class Guesses(View):
    def get(self, request, face_pk):
        face = get_object_or_404(Face, pk=face_pk)
        guesses = face.guess_set.order_by("-pk").values()

        return HttpResponse(json.dumps(list(guesses)))

    def post(self, request, face_pk):
        face = get_object_or_404(Face, pk=face_pk)
        data = json.loads(request.body)

        print data
        Guess.objects.create(
            face=face,
            who=data["user"],
            text=data["guess"],
            correct=face.guess_name(data["guess"]),
        )

        return self.get(request, face_pk)

guess = Guesses.as_view()


class Chats(View):
    def get(self, request):
        chat = Chat.objects.all().order_by("-time")[:50].values()

        for ch in chat:
            ch ["time"] = ch["time"].strftime("%H:%M:%S")

        return HttpResponse(json.dumps(list(chat)))

    def post(self, request):
        data = json.loads(request.body)

        Chat.objects.create(
            who=data["user"],
            text=data["msg"],
        )

        return self.get(request)


chat = Chats.as_view()


def is_solved(request):
    if Face.objects.filter(guess__correct=True).count() == Face.objects.all().count():
        return HttpResponse("//www.youtube.com/embed/pNxldKs-NcI")
    return HttpResponse("")
