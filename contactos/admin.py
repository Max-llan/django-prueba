from django.contrib import admin
from .models import Contact
from django.http import HttpResponse
import csv
from .models import Contact

@admin.action(description="Exportar contactos seleccionados a CSV")
def export_contacts_to_csv(modeladmin, request, queryset):
    """
    Exporta los objetos seleccionados (queryset) a un CSV descargable.
    Compatible con Excel (usa utf-8-sig).
    """
    # Nombre del archivo con fecha-hora opcional
    filename = "contactos_export.csv"

    # Crear respuesta HTTP con tipo CSV y codificación para Excel
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Usar utf-8-sig para que Excel reconozca bien la codificación
    writer = csv.writer(response, dialect='excel')
    # Escribir cabecera (títulos de columnas)
    writer.writerow(['ID', 'Nombre', 'Email', 'Teléfono', 'Dirección', 'Creado en'])

    # Escribir filas con los campos que quieras exportar
    for contact in queryset:
        writer.writerow([
            contact.pk,
            contact.nombre,
            contact.email,
            contact.telefono,
            contact.direccion,
            contact.created_at.isoformat() if hasattr(contact, 'created_at') else ''
        ])

    return response

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','telefono','direccion')
    search_fields = ('nombre','email')
    list_filter = ('created_at',)         
    actions = [export_contacts_to_csv]    
