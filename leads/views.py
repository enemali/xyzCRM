from django.core.mail import send_mail
from django.shortcuts import render , redirect , reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic 
from .models import Lead
from .models import Agent
from .forms import LeadForm
from .forms import LeadModelForm , CustomUserCreationForm

class signupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    def get_success_url (self):
        return reverse('login')

class landingPageView(generic.TemplateView):
    template_name = "landing.html"

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # send email to agent
        send_mail(
            subject="A lead has been created" ,
            message="go to the site to see the new lead" ,
            from_email="test@test.com" ,
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_Update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# def landning_page(request):
#     return render(request, "landing.html")

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {'leads': leads}
#     return render(request, "leads/lead_list.html",context)

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {'lead': lead}
#     return render(request, "leads/lead_detail.html",context)

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {'form': form}
#     return render(request, "leads/lead_create.html",context)

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST,instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     lead = Lead.objects.get(id=pk)
#     context = {'form': form,'lead': lead}
#     return render(request, "leads/lead_update.html",context)

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads')




# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
    
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             message = form.cleaned_data['message']
#             source = form.cleaned_data['source']

#             agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.email = email
#             lead.phone = phone
#             lead.message = message
#             lead.source = source
#             lead.agent = agent
#             lead.save()

#             return redirect('/leads')

#     context = {'form': form,'lead': lead}
#     return render(request, "leads/lead_update.html",context)

    #------------------------------------------------------------------------------
# def lead_create(request):
    # form = LeadForm()
    # if request.method == "POST":
    #     form = LeadForm(request.POST)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         email = form.cleaned_data['email']
    #         phone = form.cleaned_data['phone']
    #         message = form.cleaned_data['message']
    #         source = form.cleaned_data['source']
    #         agent = Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             email=email,
    #             phone=phone,
    #             source=source,
    #             message=message,
    #             agent=agent
    #         )
    #        # return redirect('/leads')
    # context = {
    #     'form': form
    # }
#     return render(request, "leads/lead_create.html",context)



    
