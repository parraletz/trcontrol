from django.db import models

STATUS_CHOICE = (
    ('AC', 'Activo'),
    ('IN', 'Inactivo'),
    ('SL', 'Solucionado'),
    ('PR', 'En Produccion'),
    ('EP', 'En Desarrollo'),
    ('QA', 'En Pruebas'),

)

PRODUCTO_CHOICE = (
    ('TEA', 'Tralix Email Marketing'),
    ('XSA', 'Facturacion electronnica'),
    ('MFN', 'Mis Facturas'),
    ('PAC', 'PAC'),
)

TIPO_CHOICE = (
    ('HI', 'Historia'),
    ('BU', 'Bug'),
    ('SC', 'Sugerencia del cliente'),
    ('CT', 'Chore - Task '),
    ('RP', 'Requisicion de Proyecto'),
)

class Componente(models.Model):
    componente  = models.CharField(max_length=25, null=False, unique=True)
    version     = models.CharField(max_length=10)
    activo      = models.BooleanField(default=True)

    def __str__(self):
        return self.componente

    class Meta:
        verbose_name_plural = "Componentes"


class Bug(models.Model):
    numero = models.CharField(max_length=20, null=False, unique=True)
    liga = models.URLField(verbose_name="Jira")
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, null=False)
    componente = models.ForeignKey(Componente)
    producto    = models.CharField(choices=PRODUCTO_CHOICE, max_length=25, null=False)
    tipo = models.CharField(max_length=50,choices=TIPO_CHOICE)
    observaciones = models.TextField(max_length=1024)

    def __str__(self):
        return  self.numero

    class Meta:
        verbose_name_plural = "Listado de bugs"



