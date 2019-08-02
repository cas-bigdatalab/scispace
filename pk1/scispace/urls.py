# coding=utf-8

from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    re_path(r'^$', index, name="scispace_index"),

    re_path(r'^login/$',  auth_views.LoginView.as_view(template_name="accounts_login.html"), name="scispace_login"), 
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name="scispace_logout"),

    re_path(r'clusters/$', cluster_list, name="scispace_cluster_list"),
    re_path(r'clusters/add/$', cluster_add, name="scispace_cluster_add"),
    re_path(r'clusters/operate/$', cluster_operate_ajax, name="scispace_cluster_operate_ajax"),
    re_path(r'clusters/scales/engines_ajax/$', scale_engines_ajax, name="scispace_scale_engines_ajax"),
    path('clusters/<int:c_id>/', cluster_info, name="scispace_cluster_info"),
    path('clusters/<int:c_id>/instances/', cluster_instance_list, name="scispace_cluster_instance_list"),
    path('clusters/<int:c_id>/instances/operate/', cluster_instance_operate_ajax, name="scispace_cluster_instance_operate_ajax"),
    path('clusters/<int:c_id>/datasets/', dataset_list, name="scispace_dataset_list"),
    # path('clusters/<int:c_id>/datasets/<int:dt_id>/', dataset_info, name="scispace_dataset_info"),
    # path('clusters/<int:c_id>/datasets/<int:dt_id>/load/', dataset_info, name="scispace_dataset_load"),
    path('clusters/<int:c_id>/datainstances/', data_instance_list, name="scispace_data_instance_list"),
    path('clusters/<int:c_id>/datainstances/add/', data_instance_add, name="scispace_data_instance_add"),
    path('clusters/<int:c_id>/datainstances/delete/', data_instance_delete, name="scispace_data_instance_delete"),
    path('clusters/<int:c_id>/datainstances/query/', data_instance_query, name="scispace_data_instance_query"),
    path('clusters/<int:c_id>/data_pipeline/', data_pipeline, name="scispace_data_pipeline"),
    path('clusters/<int:c_id>/notebook/', notebook, name="scispace_notebook"),
    path('clusters/<int:c_id>/scispace_operations/', scispace_operation_list, name="scispace_op_list"),
    path('clusters/<int:c_id>/data_instance_operations/', data_instance_operation_list, name="scispace_datainstance_op_list"),
    path('clusters/<int:c_id>/data_engines_ajax/', get_data_engines_ajax, name="scispace_get_data_engines_ajax"),
    # path('space/<int:sid>/datasets/', datasets),
    # path('space/<int:sid>/datasets/<int:did>/', datasets),
]