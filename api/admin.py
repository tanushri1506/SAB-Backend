from django.contrib import admin
from .models import Contacts, Events,Council,Gallery,PreviousWorkshops,Workshops,Lectures,PreviousLectures,Pal,UgCouncil,PhdDPPC,PhdCPPC,PhdSPPC,LanguageTeam,LanguageCourses,BranchRepresentative
admin.site.register(Contacts)
admin.site.register(Events)
admin.site.register(Gallery)
admin.site.register(Workshops)
admin.site.register(PreviousWorkshops)
admin.site.register(Lectures)
admin.site.register(PreviousLectures)
admin.site.register(Pal)
admin.site.register(UgCouncil)
admin.site.register(PhdDPPC)
admin.site.register(PhdCPPC)
admin.site.register(PhdSPPC)
admin.site.register(LanguageTeam)
admin.site.register(LanguageCourses)

@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "tenure")
    list_filter = ("tenure",)        # allows filtering by tenure
    search_fields = ("name", "post") # search by name or post



@admin.register(BranchRepresentative)
class BranchRepresentativesAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "tenure")
    list_filter = ("tenure",)
    search_fields = ("name", "post")
