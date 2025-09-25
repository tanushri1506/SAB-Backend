# urls.py
from django.urls import path
from .views import Contacts, Events,Council,Gallery,Workshops,PreviousWorkshops,Lectures,PreviousLectures,Pal,UgCouncil,PhdDPPC,PhdCPPC,PhdSPPC,LanguageTeam,LanguageCourses,BranchRepresentatives

urlpatterns = [
    path('api/contacts/', Contacts.as_view(), name='contacts-list'),
    path('api/events/', Events.as_view(), name='events-list'),
    path('api/council/', Council.as_view(), name='team-list'),
    path('api/gallery/', Gallery.as_view(), name='gallery-list'),
    path('api/workshops/', Workshops.as_view(), name='workshops-list'),
    path('api/previous-workshops/', PreviousWorkshops.as_view(), name='previous-workshops-list'),
    path('api/lectures/', Lectures.as_view(), name='lectures-list'),
    path('api/previous-lectures/', PreviousLectures.as_view(), name='previous-lectures-list'),
    path('api/pal/', Pal.as_view(), name='pal'),
    path('api/ug/', UgCouncil.as_view(), name='ug'),
    path('api/dppc/', PhdDPPC.as_view(), name='dppc'),
    path('api/cppc/', PhdCPPC.as_view(), name='cppc'),
    path('api/sppc/', PhdSPPC.as_view(), name='sppc'),
    path('api/language-team/', LanguageTeam.as_view(), name='language-team'),
    path('api/language-courses/', LanguageCourses.as_view(), name='language-courses'),
    path('api/branch-reps/', BranchRepresentatives.as_view(), name='branch-reps-list'),
    
]
