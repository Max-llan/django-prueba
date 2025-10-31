from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    q = request.GET.get('q','').strip()
    contacts = Contact.objects.all().order_by('-created_at')
    if q:
        contacts = contacts.filter(Q(nombre__icontains=q) | Q(email__icontains=q))
    context = {'contacts': contacts, 'q': q}
    return render(request, 'contactos/contact_list.html', context)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contactos/contact_form.html', {'form': form, 'action': 'Crear'})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contactos/contact_form.html', {'form': form, 'action': 'Editar'})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contactos/contact_confirm_delete.html', {'contact': contact})
