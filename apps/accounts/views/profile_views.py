# apps/accounts/views/profile_views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages

# Import the new forms
from apps.accounts.forms.auth_forms import UserUpdateForm, UserProfileForm
from apps.accounts.models import UserProfile

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class ProfileEditView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure profile exists
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)

        # Populate forms if not already in context (from a failed POST)
        if 'user_form' not in context:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        if 'profile_form' not in context:
            context['profile_form'] = UserProfileForm(instance=profile)

        return context

    def post(self, request, *args, **kwargs):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect(reverse_lazy("accounts:profile"))
        else:
            # If forms are invalid, re-render the page with the forms containing errors
            context = self.get_context_data(user_form=user_form, profile_form=profile_form)
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return self.render_to_response(context)

class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("accounts:profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        # mantém o usuário logado após trocar a senha
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Sua senha foi alterada com sucesso!')
        return super().form_valid(form)
