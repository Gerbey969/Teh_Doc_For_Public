from landing.models import *
from meta.models import ModelMeta
from django.utils.translation import ugettext_lazy


class Category(ModelMeta, models.Model):
    name = models.CharField(ugettext_lazy('Name'), max_length=250, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Feedback(models.Model):
    name = models.CharField(help_text=ugettext_lazy('Name*'), max_length=250, blank=True, null=True)
    email = models.EmailField(help_text=ugettext_lazy('Email*'))
    phone = models.IntegerField(help_text=ugettext_lazy('Phone*'), blank=True, null=True)
    category = models.ForeignKey(Category, help_text=ugettext_lazy('Choose Category*'), blank=True, null=True,
                                 on_delete=models.CASCADE)
    country = models.ForeignKey(Documentation, help_text=ugettext_lazy("Choose Country*"), blank=True, null=True,
                                on_delete=models.CASCADE)
    ser_num = models.CharField(help_text=ugettext_lazy('Serial Number'), max_length=120)
    description = models.TextField(help_text=ugettext_lazy('Description'), max_length=1000)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Feedback %s %s" % (self.name, self.category)

    class Meta:
        verbose_name = 'Звернення'
        verbose_name_plural = 'Звернення'
