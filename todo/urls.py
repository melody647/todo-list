from django.urls import path,include
from . import views as todo_view


urlpatterns = [
    path('', todo_view.CreateTodoView.as_view(),name='home'),
    path('todo/<int:pk>/update/', todo_view.TodoUpdateView.as_view(),name='todo_update'),
    path('todo/<int:pk>/delete/', todo_view.TodoDeleteView.as_view(),name='todo_delete'),
    path('mytodos/',todo_view.alltodos,name='alltodos'),
    
]