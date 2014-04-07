from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from principal.models import Editor, Libro
from django.utils import timezone

class EditorList(ListView):
	model = Editor
	context_object_name = 'lista_editores'

	def get_context_data(self, **kwargs):
		context = super(EditorList, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['lista_libros']=Libro.objects.all()
		return context


class EditorDetailView(DetailView):
    model = Editor


class EditorCreateView(CreateView):
	model = Editor
	success_url="/editores"

