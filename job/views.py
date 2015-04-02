from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from job.forms import EmailUserCreationForm, PlaceForm
from job.forms import JobApplicationForm
from job.models import JobPosition, HealthCareCompany
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def profile(request):
    return render(request, 'profile.html', )


def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})


def list(request):
    """
    Renders a list of available positions
    """
    positions = JobPosition.objects.all()

    return render_to_response("careers/list.html", {
        "positions": positions,
    }, context_instance=RequestContext(request))


def apply(request):
    """
    Renders an application form and handles it
    """
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("careers_apply_done"))
    else:
        form = JobApplicationForm()

    return render_to_response("careers/apply.html", {
        "form": form,
    }, context_instance=RequestContext(request))


def apply_done(request):
    """
    Renders a thank you page
    """
    return render_to_response("careers/apply_done.html", {

    }, context_instance=RequestContext(request))


def map(request):
    companies = HealthCareCompany.objects.all()
    data = {
        'companies': companies,
    }
    return render(request, "map.html", data)