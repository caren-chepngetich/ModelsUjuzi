
# from django.urls import path
# from .views import KicdListView
# from .views import ModuleListView
# from .views import MarkingSchemeListView
# from.views import KicdDetailView
# from.views import ModuleDetailView
# from.views import MarkingSchemeDetailView



# urlpatterns =[
   
#     path("Kicd/", KicdListView.as_view(),name="Kicd_list_view"),
#     path('Kicd/<int:id>/', KicdDetailView.as_view(), name="Kicd_detail_view"),
#     path("module", ModuleListView.as_view(),name="module_list_view"),
#     path('module/<int:id>/', ModuleDetailView.as_view(),name="module_detail_view"),
#     path("markingscheme/", MarkingSchemeListView.as_view(),name="markingscheme_list_view"),
#     path('markingscheme/<int:id>/', MarkingSchemeDetailView.as_view(),name="markingscheme_detail_view"),

# ]
from django.urls import path
from .views import (
    KicdListView,
    ModuleListView,
    MarkingSchemeListView,
    KicdDetailView,
    ModuleDetailView,
    MarkingSchemeDetailView,
)

urlpatterns = [
    path("kicd/", KicdListView.as_view(), name="kicd_list_view"),
    path('kicd/<int:id>/', KicdDetailView.as_view(), name="kicd_detail_view"),
    path("module/", ModuleListView.as_view(), name="module_list_view"),
    path('module/<int:id>/', ModuleDetailView.as_view(), name="module_detail_view"),
    path("markingscheme/", MarkingSchemeListView.as_view(), name="markingscheme_list_view"),
    path('markingscheme/<int:id>/', MarkingSchemeDetailView.as_view(), name="markingscheme_detail_view"),
]
