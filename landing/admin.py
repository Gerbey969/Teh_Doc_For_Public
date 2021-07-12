from django.contrib import admin
from .models import *


class DocumentationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Documentation._meta.fields]

    class Meta:
        model = Documentation


admin.site.register(Documentation, DocumentationAdmin)


class QRCodeGeneratorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QRCodeGenerator._meta.fields]

    class Meta:
        model = QRCodeGenerator


admin.site.register(QRCodeGenerator, QRCodeGeneratorAdmin)


class TitleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Titles._meta.fields]

    class Meta:
        model = Recuperator


admin.site.register(Titles, TitleAdmin)


class DownloadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Download._meta.fields]

    class Meta:
        model = Download


admin.site.register(Download, DownloadAdmin)


class RecuperatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recuperator._meta.fields]

    class Meta:
        model = Recuperator


admin.site.register(Recuperator, RecuperatorAdmin)


class DocumentFilesAdm(admin.ModelAdmin):
    list_display = [field.name for field in DocumentFiles._meta.fields]

    class Meta:
        model = DocumentFiles


admin.site.register(DocumentFiles, DocumentFilesAdm)


class DocumentFilesAdmin(admin.TabularInline):
    model = DocumentFiles


class YouTubeInlineAdmin(admin.TabularInline):
    model = YouTube


class RevisionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Revision._meta.fields]
    inlines = [DocumentFilesAdmin, YouTubeInlineAdmin]


admin.site.register(Revision, RevisionAdmin)


class DodatkoveAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dodatkove._meta.fields]

    class Meta:
        model = Dodatkove


admin.site.register(Dodatkove, DodatkoveAdmin)


class YouTubeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in YouTube._meta.fields]

    class Meta:
        model = YouTube


admin.site.register(YouTube, YouTubeAdmin)


class GarantiyaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Garantiya._meta.fields]

    class Meta:
        model = Garantiya


admin.site.register(Garantiya, GarantiyaAdmin)
