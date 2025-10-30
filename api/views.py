from rest_framework.generics import ListAPIView
from .models import Contacts, Events,Council,Gallery,Workshops,PreviousWorkshops,Lectures,PreviousLectures,Pal,PhdDPPC,PhdCPPC,PhdSPPC,UgCouncil,LanguageTeam,LanguageCourses,BranchRepresentative, Carousel
from .serializers import ContactsSerializer, EventsSerializer, CouncilSerializer, GallerySerializer,WorkshopsSerializer,PreviousWorkshopsSerializer,LecturesSerializer,PreviousLecturesSerializer,PalSerializer,UgCouncilSerializer,PhdCPPCSerializer,PhdDPPCSerializer,PhdSPPCSerializer,LanguageTeamSerializer,LanguageCoursesSerializer,BranchRepresentativesSerializer, CarouselSerializer

class Contacts(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class Events(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class CouncilListView(ListAPIView):
    serializer_class = CouncilSerializer

    def get_queryset(self):
        tenure = self.request.GET.get("tenure")

        if tenure == "all":
            # Return all council entries for dropdown (including current year if you want)
            return Council.objects.all().order_by("-tenure")
        elif tenure:
            return Council.objects.filter(tenure=tenure)
        # Default: current tenure
        return Council.objects.filter(tenure="2025-26")


class Gallery(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class Workshops(ListAPIView):
    queryset = Workshops.objects.all()
    serializer_class = WorkshopsSerializer

class PreviousWorkshops(ListAPIView):
    queryset = PreviousWorkshops.objects.all()
    serializer_class = PreviousWorkshopsSerializer

class Lectures(ListAPIView):
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializer

class PreviousLectures(ListAPIView):
    queryset = PreviousLectures.objects.all()
    serializer_class = PreviousLecturesSerializer

class Pal(ListAPIView):
    queryset = Pal.objects.all()
    serializer_class = PalSerializer

class UgCouncil(ListAPIView):
    queryset = UgCouncil.objects.all()
    serializer_class = UgCouncilSerializer

class PhdDPPC(ListAPIView):
    queryset = PhdDPPC.objects.all()
    serializer_class = PhdDPPCSerializer

class PhdCPPC(ListAPIView):
    queryset = PhdCPPC.objects.all()
    serializer_class = PhdCPPCSerializer

class PhdSPPC(ListAPIView):
    queryset = PhdSPPC.objects.all()
    serializer_class = PhdSPPCSerializer

class LanguageTeam(ListAPIView):
    queryset = LanguageTeam.objects.all()
    serializer_class = LanguageTeamSerializer

class LanguageCourses(ListAPIView):
    queryset = LanguageCourses.objects.all()
    serializer_class = LanguageCoursesSerializer

class BranchRepresentatives(ListAPIView):
    serializer_class = BranchRepresentativesSerializer

    def get_queryset(self):
        tenure = self.request.GET.get("tenure", "2024-28") 
        return BranchRepresentative.objects.filter(tenure=tenure)


class CarouselListView(ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer