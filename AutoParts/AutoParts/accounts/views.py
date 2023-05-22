from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from AutoParts.accounts.forms import ProfileForm
from AutoParts.accounts.models import Profile
from django_cleanup.signals import cleanup_pre_delete


class ProfileDetailsView(FormView):
    template_name = 'pages/profile-details.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(pk=self.request.user.id)

        return context


def change_profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'pages/change-profile-details.html', context)
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')
    return render(request, 'pages/change-profile-details.html', {'form': form})
