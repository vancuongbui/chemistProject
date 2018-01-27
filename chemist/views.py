from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomePage(TemplateView):
    template_name = 'index.html'
    #redirect_field_name='thanks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        generateHTML = "<h1>This is the test of generating html by django"
        context['testGenerateHTML'] = generateHTML
        return context
    

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class TestPage(TemplateView):
    template_name = 'test.html'
    success_url = reverse_lazy('login') #redirect to login page#