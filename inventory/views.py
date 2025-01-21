from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm # Add this line to import UserRegisterForm
from .models import InventoryItem, Category
from datetime import datetime, timedelta, date


# Create your views here.

def get_expiring_items(user):
    today = datetime.now().date()
    three_days_later = today + timedelta(days=3)
    return InventoryItem.objects.filter(user=user, expiry_date__range=[today, three_days_later])

class Index(TemplateView):
    template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        expiring_items = get_expiring_items(self.request.user)
        Expired = date.today()
        print(Expired)
        print(Expired)

        return render(request, 'inventory/dashboard.html', {'items': items, 'expiring_items': expiring_items, 'Expired': Expired})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')
        
        return render(request, 'inventory/signup.html', {'form': form})
    
class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = 'Category.objects.all()'
        return context
            
    def form_valid(self, form):
        new_category_name = form.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            form.instance.category = category
        else:
            form.instance.category = form.cleaned_data.get('category')
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/add_item.html'
    success_url = reverse_lazy('dashboard')
    
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'




