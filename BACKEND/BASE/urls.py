from django.urls import path
from .views import prod,addProd,prodId,delId,updateId,get_PRODUCTION_id,get_producer

from .views import get_task_ids_by_production

urlpatterns = [
    #page accueil liste des productions existantes
    path('productions',prod),
    
    #liste les chargés de production disponible (
    #appelée pour créer une production : le formulaire pour en créer une doit permettre d'afficher
    # et sélectionner un ou plusieurs)  )
    path('producer/', get_producer),

    #affiche une production en particulier à partir de son ID
    path('production/<str:prod_id>/', prodId),
    
    #supprime une production à partir de son ID
    path('delete/<str:prod_id>/', delId),
    
    #met à jour les informations d'une production à partir de son ID
    path('update/<str:prod_id>/', updateId),
    
    #joute une productions
    path('change',addProd),
    
    
    path('get_prod_id/<int:task_id>/', get_PRODUCTION_id, name='get_production_id'),
    
    #obtient les tâches liées à une production à partir de son ID
    path('get_task_ids_by_production/<int:production_id>/', get_task_ids_by_production, name='get_task_ids_by_production'),

    
]






