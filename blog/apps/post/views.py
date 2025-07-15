from django.views.generic import TemplateView


class UserProfileView(TemplateView):
    template_name = 'post/post_detail.html'