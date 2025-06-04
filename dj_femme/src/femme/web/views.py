

from django.shortcuts import render
from web.models import AboutClass, RegistrationClass, IssuesClass, WhyfemmeClass, TextClass
from django.http.response import HttpResponse
from web.forms import RegistrationForm
from web.functions import generate_form_errors
import json
from django.urls import reverse


def index(request):
    # all()  -- return -- queryset
    # filter() -- return -- queryset
    # exclude() -- return -- queryset
    # get() -- return -- object

    _about_instances = AboutClass.objects.all()
    _issue_instances = IssuesClass.objects.all()
    _whyfemme_instances = WhyfemmeClass.objects.all()
    _text_instances = TextClass.objects.all()
    _form = RegistrationForm
    context = {
        "app_title": "Home",
        "about_instances": _about_instances,
        "issue_instances": _issue_instances,
        "whyfemme_instances": _whyfemme_instances,
        "text_instances": _text_instances,
        "form": _form,
        "is_home": True,
    }
    return render(request, 'web/index.html', context);


def about(request):
    _about_instances = AboutClass.objects.all()
    context = {
        "app_title": "About",
        "about_instances": _about_instances,
        "is_about": True,
    }
    return render(request, 'web/about.html', context);


def registration(request):
    if request.method == "POST":
        '''    HTML FORM SUBMISSION
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _education = request.POST.get('education')
        _dob = request.POST.get('dob')
        _message = request.POST.get('message')
        RegistrationClass.objects.create(
            name=_name, email=_email, phone=_phone, education=_education, dob=_dob, message=_message
        )
        '''
        '''   DJANGO FORM SUBMISSION   '''
        _form = RegistrationForm(request.POST)
        if _form.is_valid():
            _form.save()
            response_data = {
                'status': "true",
                'title': "Successfully submitted",
                'message': "message successfully submitted",
            }
        else:
            message = generate_form_errors(_form, formset=False)
            response_data = {
                'status': "false",
                'stable': "true",
                'title': "Form validation error",
                'message': message,
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponse("invalid request!")


def issues(request):
    _issue_instances = IssuesClass.objects.all()
    context = {
        "app_title": "issues",
        "issues_instances": _issue_instances,
        "is_about": True,
    }

    return render(request, 'web/issues.html', context);


def whyfemme(request):
    _whyfemme_instances = WhyfemmeClass.objects.all()
    context = {
        "app_title": "whyfemme",
        "whyfemme_instances": _whyfemme_instances,
        "is_about": True,
    }

    return render(request, 'web/whyfemme.html', context);

def text(request):
    _text_instances = TextClass.objects.all()
    context = {
        "app_title": "text",
        "text_instances": _text_instances,
        "is_about": True,
    }

    return render(request, 'web/text.html', context);
