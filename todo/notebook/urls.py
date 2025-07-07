from django.urls import path
from .views import home, index, delete_notebook, update_notebook,save_notebook, create_note
app_name = 'notebook'
urlpatterns = [
    path('', index, name='home'),
    path('notebook/delete', delete_notebook, name='delete-notebook'),
    path('notebook/update/<int:note_id>/', update_notebook, name='update-notebook'),
    path('notebook/save/<int:note_id>/', save_notebook, name='update-save'),
    path('create/', create_note, name='create-note'),

]
