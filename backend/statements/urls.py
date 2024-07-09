from django.urls import path
from . import views

urlpatterns = [
    path('statement/', views.StatementView.as_view({'post':'create','get':'list'}), name='statement'),
    path('statement/<int:pk>/', views.StatementView.as_view({'get':'retrieve','patch':'partial_update','delete':'destroy'}), name='statement-ind'),
    path('statement/folder/', views.StatementView.as_view({'get':'get_distinct_folder'}), name='statement-folder'),
    path('statement/folder/inner/', views.StatementView.as_view({'get':'get_distinct_folder2'}), name='statement-folder2'),
    path('statement/file/', views.StatementView.as_view({'get':'get_file_names_for_folder'}), name='statement-file'),
    path('statement/recent/',views.StatementView.as_view({'get':'get_recent_statements'}), name='statement-recent'),
    path('statement/print/', views.print_and_log_statement, name='save-statement'),


    path('woda/', views.WodaDocView.as_view({'post':'create','get':'list'}), name='woda'),
    path('woda/<int:pk>/', views.WodaDocView.as_view({'get':'retrieve','patch':'partial_update', 'delete':'destroy'}), name='woda-doc-ind'),
    path('woda/folder/', views.WodaDocView.as_view({'get':'get_distinct_folder'}), name='woda-folder'),
    path('woda/folder/inner/', views.WodaDocView.as_view({'get':'get_distinct_folder2'}), name='woda-folder2'),
    path('woda/file/', views.WodaDocView.as_view({'get':'get_file_names_for_folder'}), name='woda-file'),
    path('woda/recent/',views.WodaDocView.as_view({'get':'get_recent_wodadoc'}), name='woda-recent'),
    path('woda/print/', views.print_and_log_woda, name='save-woda'),
]