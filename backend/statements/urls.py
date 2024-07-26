from django.urls import path
from . import views

urlpatterns = [
    path('statement/', views.StatementView.as_view({'post':'create'}), name='statement'),
    path('statement/<int:pk>/', views.StatementView.as_view({'get':'retrieve','patch':'partial_update','delete':'destroy'}), name='statement-ind'),
    path('statement/recent/',views.StatementView.as_view({'get':'get_recent_statements'}), name='statement-recent'),
    path('statement/print/', views.print_and_log_statement, name='save-statement'),
    path('statement/logs/', views.StatementLogsView.as_view({'get':'list'}), name='statement-logs'),
    path('statement/logs/<int:pk>/', views.StatementLogsView.as_view({'get':'retrieve','delete':'destroy'}), name='statement-logs-ind'),
    path('statement/logs/filter/', views.StatementLogsView.as_view({'get':'find_by_statement_id'}), name='statement-logs-filter'),


    path('woda/', views.WodaDocView.as_view({'post':'create'}), name='woda'),
    path('woda/<int:pk>/', views.WodaDocView.as_view({'get':'retrieve','patch':'partial_update', 'delete':'destroy'}), name='woda-doc-ind'),
    path('woda/recent/',views.WodaDocView.as_view({'get':'get_recent_wodadoc'}), name='woda-recent'),
    path('woda/print/', views.print_and_log_woda, name='save-woda'),
    path('woda/logs/', views.WodaLogsView.as_view({'get':'list'}), name='woda-logs'),
    path('woda/logs/<int:pk>/', views.WodaLogsView.as_view({'get':'retrieve','delete':'destroy'}), name='woda-logs-ind'),
    path('woda/logs/filter/', views.WodaLogsView.as_view({'get':'find_by_woda_id'}), name='woda-logs-filter'),

    path('signature/', views.SignatureView.as_view({'post':'create', 'get':'list'}), name='signature'),
    path('signature/<int:pk>/', views.SignatureView.as_view({'get':'retrieve','patch':'partial_update','delete':'destroy'}), name='signature-ind'),

    path('folder/', views.FolderView.as_view({'post':'create', 'get':'list'}), name='folder'),
    path('folder/<int:pk>/', views.FolderView.as_view({'get':'retrieve', 'patch':'partial_update','delete':'destroy'}), name='folder-ind'),

    path('search/statement/', views.SearchStatementView.as_view({'get':'search'}), name='statement-search'),
    path('search/wodadoc/', views.SearchWodaDocView.as_view({'get':'search'}), name='wodadoc-search'),
]