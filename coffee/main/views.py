from datetime import datetime

from django.http import HttpRequest, JsonResponse
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views import View

from .models import Product, WorkSchedule


class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['heading'] = _('О нас')
        context['subheading'] = _('Наш кофе')
        return context


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'main/products.html'
    context_object_name = 'products'
    model = Product
    login_url = '/signin/'

    def get_queryset(self):
        from itertools import zip_longest
        objs = Product.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))


class WorkScheduleListView(ListView):
    template_name = 'main/store.html'
    context_object_name = 'week'
    model = WorkSchedule

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['weekday'] = datetime.today().isoweekday() + 6
        return context


class ProductApiView(View):
    model = Product

    def get(self, request: HttpRequest):
        objs = self.model.objects.filter(is_published=True).order_by('id')
        products = {'products': []}
        for product in objs:
            products['products'].append(
                {
                    'id': product.id,
                    'name': product.name,
                    'descr': product.descr,
                    'image': product.image.url
                }
            )
        return JsonResponse(products, status=200)

    def post(self, request: HttpRequest):
        product = self.model(request.POST)
        try:
            product.save()
        except Exception as e:
            return JsonResponse({'error': e}, status=404)
        return JsonResponse(product.__dict__, status=201)