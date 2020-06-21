from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "rest_tournament_manager_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
