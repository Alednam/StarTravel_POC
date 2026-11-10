from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theories/', views.theory_list, name='theory_list'),
    path('theories/<str:theory_name>/', views.theory_list, name='theory_detail'),
    path('gaps/', views.gap_analysis, name='gap_analysis'),
    path('oracle/', views.oracle_engine_view, name='oracle_engine'),
    path('knowledge-base/', views.knowledge_base, name='knowledge_base'),
    path('space-flight/', views.space_flight, name='space_flight'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('api/network-data/', views.network_data, name='network_data'),
]
    