from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from core.forms import ContatoForm
from core.models import Funcionario, Servico


class Home(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('home')

    # sobreescrevendo o contexto da página
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('?').all()
        contexto['servicos'] = Servico.objects.filter(ativo=True)
        return contexto

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível enviar o e-mail!')
        return super().form_invalid(form)



class Teste(TemplateView):
    template_name = 'teste.html'