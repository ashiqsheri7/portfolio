from django.shortcuts import render, get_object_or_404, redirect
from .models import About, Experience, Education, Contact
from .forms import AboutForm, ExperienceForm, EducationForm,  ContactForm
# About Views
def about_list(request):
    about = About.objects.all()
    return render(request, 'portfolio/template/about_list.html', {'about': about})

def about_create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm()
    return render(request, 'portfolio/template/about_form.html', {'form': form})

def about_update(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm(instance=about)
    return render(request, 'portfolio/template/about_form.html', {'form': form})

def about_delete(request, pk):
    about = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        about.delete()
        return redirect('about_list')
    return render(request, 'portfolio/template/about_confirm_delete.html', {'about': about})


def experience_list(request):
    experience = Experience.objects.all()
    return render(request, 'portfolio/template/experience_list.html', {' experience':  experience})

def  experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = AboutForm()
    return render(request, 'portfolio/template/experience_form.html', {'form': form})

def experience_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form =ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'portfolio/template/experience_form.html', {'form': form})

def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        experience.delete()
        return redirect('experience_list')
    return render(request, 'portfolio/template/experience_confirm_delete.html', {'experience': experience})

def education_list(request):
    education = Education.objects.all()
    return render(request, 'portfolio/template/education_list.html', {'education': education})

def education_create(request):
    if request.method == 'POST':
        form =  EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('education_list')
    else:
        form = AboutForm()
    return render(request, 'portfolio/template/education_form.html', {'form': form})
def education_update(request, pk):
    education = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'portfolio/template/education_form.html', {'form': form})

def education_delete(request, pk):
    education = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        education.delete()
        return redirect('about_list')
    return render(request, 'portfolio/template/education_confirm_delete.html', {' education':  education})

def contact_list(request):
    contact = Contact.objects.all()
    return render(request, 'portfolio/template/contact_list.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'portfolio/template/contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'portfolio/template/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(About, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('about_list')
    return render(request, 'portfolio/template/contact_confirm_delete.html', {'contact': contact})
