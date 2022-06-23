from django.urls import path

from htmx_django.apps.core.views import views_exemplo1, views_exemplo2, views_exemplo3

app_name = 'core'

urlpatterns = [
    path('click_to_load/', views_exemplo1.example_click_load, name='click_to_load'),
    path('replace/', views_exemplo1.replace_example, name='replace'),
    path('filmes/', views_exemplo2.filme_view, name='filme'),
    path('criar_filme/', views_exemplo2.create_filme, name='create_filme'),
    path('render_update/<int:filme_id>/', views_exemplo2.render_update_filme, name='render_update_filme'),
    path('update/<int:filme_id>/', views_exemplo2.update_filme, name='update_filme'),
    path('delete/<int:filme_id>/', views_exemplo2.delete_filme, name='delete_filme'),
    path('search_filme_view/', views_exemplo3.search_filme_view, name='search_filme_view'),
    path('search_filme/', views_exemplo3.search_filme, name='search_films'),
]
