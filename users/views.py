from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from users.models import UserImage


class ImagesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/images.html'

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        for key, value in request.FILES.items():
            UserImage.objects.create(user=request.user, photo=value)
        return super().get(request, *args, **kwargs)
