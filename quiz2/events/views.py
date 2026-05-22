from django.shortcuts import render
from django.views import View

from .forms import EventRegistrationForm


class EventRegistrationView(View):
    template_name = 'events/register.html'
    form_class = EventRegistrationForm
    success_message = 'Registration submitted successfully.'

    def get(self, request):
        return self.render_form(request, self.form_class())

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return self.render_form(
                request,
                self.form_class(),
                success_message=self.success_message,
            )
        return self.render_form(request, form)

    def render_form(self, request, form, **extra_context):
        context = {'form': form}
        context.update(extra_context)
        return render(request, self.template_name, context)


register_event = EventRegistrationView.as_view()
