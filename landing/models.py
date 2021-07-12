import uuid
from django.db import models
from django.urls import reverse
from tinymce import models as tinymc
from meta.models import ModelMeta
from django.utils.text import slugify
from io import BytesIO
import qrcode
import qrcode.image.svg
from django.core.files import File
from PIL import ImageDraw, Image
from django.utils.translation import ugettext_lazy


class Documentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='images/', default='images/prana.jpg', blank=True, null=True)
    slug = models.SlugField(max_length=255, default=None)
    extra = models.CharField(max_length=155, default='u', null=True)
    is_active = models.BooleanField(default=True)

    _metadata = {
        'title': 'name',
        'url': 'get_absolute_url',
    }

    def save(self, *args, **kwargs):
        for i in self.extra:
            self.i = i[0]
        self.slug = slugify(self.name)
        super(Documentation, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('country', args=[str(self.id)])

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'


class Titles(models.Model):
    teh_har = models.CharField(max_length=200, default='Технічна документація')
    garantiya = models.CharField(max_length=200, default='Гарантія та допомога')
    country = models.ForeignKey(Documentation, on_delete=models.CASCADE, default=None)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Загаловок'
        verbose_name_plural = "Заголовки"


class QRCodeGenerator(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='images/', blank=True)
    svg = models.ImageField(upload_to='images', blank=True)
    url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        factory = qrcode.image.svg.SvgImage
        svg_m = qrcode.make(self.qr_code, image_factory=factory)
        fname = f'qr-code-{self.name}.png'
        svgname = f'qr-code-{self.name}.svg'
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        svg_m.save(buffer, 'SVG')
        self.qr_code.save(fname, File(buffer), save=False)
        self.svg.save(svgname, File(buffer), save=False)
        img.close()
        super().save(*args, **kwargs)


class Recuperator(models.Model):
    name = models.CharField(max_length=255, default=None)
    image = models.ImageField(upload_to='images/', default='images/prana.jpg', blank=True, null=True)
    country = models.ForeignKey(Documentation, default=None, on_delete=models.CASCADE)
    not_for_zavod = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.country.name)

    class Meta:
        verbose_name = "Рекуператор"
        verbose_name_plural = "Рекуператори"


class Revision(models.Model):
    name = models.CharField(max_length=200, default="Rev_")
    date = models.DateField(default=None, blank=False)
    recuperator = models.ForeignKey(Recuperator, on_delete=models.CASCADE, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s %s" % (self.name, self.recuperator)

    class Meta:
        verbose_name = "Ревізія"
        verbose_name_plural = "Ревізія"


class Download(models.Model):
    title = models.CharField(max_length=255, default=None)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    inactive = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = "Посилання на скачку"
        verbose_name_plural = "Посилання на скачку"


class Garantiya(models.Model):
    country = models.ForeignKey(Documentation, on_delete=models.CASCADE, default=None)
    text = tinymc.HTMLField()

    def __str__(self):
        return "%s" % self.country

    class Meta:
        verbose_name = 'Гарантія'
        verbose_name_plural = 'Гарантії'


class DocumentFiles(models.Model):
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    revision = models.ForeignKey(Revision, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='images/prana.jpg', blank=True, null=True)
    document = models.FileField(default=None, upload_to='documents/', blank=True, null=True)
    for_zavod = models.BooleanField(default=False)
    for_people = models.BooleanField(default=False)
    for_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.document

    class Meta:
        verbose_name = 'Документація'
        verbose_name_plural = 'Документація'


class YouTube(models.Model):
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    url = models.URLField(max_length=500)
    model = models.ForeignKey(Revision, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.model

    class Meta:
        verbose_name = 'YouTube Відео'
        verbose_name_plural = 'YouTube Відео'


class Dodatkove(models.Model):
    name = models.CharField(max_length=9999, default=None)
    doc = models.FileField(default=None, upload_to='documents/', blank=True, null=True)
    model = models.ManyToManyField(Recuperator, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Додаткове'
        verbose_name_plural = 'Додаткове'
