from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Todo
from django.views.generic import CreateView,DeleteView,UpdateView

# Create your views here.

class CreateTodoView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ['title', 'description']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

def alltodos(request):
    mytodos = Todo.objects.filter(author=request.user).all()
    return render(request,'todo/index.html',{'mytodos':mytodos})


class TodoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Todo
    template_name = 'todo/todo_update.html'
    fields = ['title','description']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False


class TodoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    fields = ['title','description']
    success_url = '/'
    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False
