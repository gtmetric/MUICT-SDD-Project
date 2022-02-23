from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SciencePlan
import requests


@login_required
def home(request):
    group = request.user.groups.all()[0];

    if group.name == 'ASTRONOMER':
        context = eval(requests.get('http://localhost:8080/scienceplans').content)
        return render(request, 'astronomer/home.html', context=context)
    elif group.name == 'SCIENCE OBSERVER':
        return redirect('validate')
    
    return redirect('login')


@login_required
def create_success(request):
    return render(request, 'astronomer/create_success.html')


class SciencePlanCreateView(LoginRequiredMixin, CreateView):
    model = SciencePlan
    template_name = 'astronomer/create.html'
    fields = ['creator', 'submitter', 'funding', 'objectives', 'star_system', 'telescope_location',
        'start_date', 'end_date', 'file_type', 'file_quality', 'color_type', 'contrast', 'exposure',
        'brightness', 'saturation', 'luminance', 'hue', 'highlights', 'shadows', 'whites', 'blacks'
    ]

    def form_valid(self, form):
        data = {
            'creator': form.instance.creator,
            'submitter': form.instance.submitter,
            'fundingInUSD': form.instance.funding,
            'objectives': form.instance.objectives,
            'starSystem': form.instance.star_system,
            'telescopeLocation': form.instance.telescope_location,
            'startDate': form.instance.start_date.strftime("%d/%m/%Y %H:%M:%S"),
            'endDate': form.instance.end_date.strftime("%d/%m/%Y %H:%M:%S"),
            'fileType': form.instance.file_type,
            'fileQuality': form.instance.file_quality,
            'colorType': form.instance.color_type,
            'contrast': form.instance.contrast,
            'brightness': form.instance.brightness,
            'saturation': form.instance.saturation,
            'highlights': form.instance.highlights,
            'exposure': form.instance.exposure,
            'shadows': form.instance.shadows,
            'whites': form.instance.whites,
            'blacks': form.instance.blacks,
            'luminance': form.instance.luminance,
            'hue': form.instance.hue
        }
        response = requests.post('http://localhost:8080/scienceplan', data)

        form.instance.plan_no = response.json()['planNo']
        form.instance.status = 'SUBMITTED'

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('create-success')
    

class TestSciencePlanListView(LoginRequiredMixin, ListView):
    model = SciencePlan
    template_name = 'astronomer/test.html'
    context_object_name = 'sciencePlans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(sciencePlans=SciencePlan.objects.filter(status='SUBMITTED'))
        return context


class TestSciencePlanUpdateView(LoginRequiredMixin, UpdateView):
    model = SciencePlan
    template_name = 'astronomer/test_detail.html'
    fields = fields = ['creator', 'submitter', 'funding', 'objectives', 'star_system', 'telescope_location',
        'start_date', 'end_date', 'file_type', 'file_quality', 'color_type', 'contrast', 'exposure',
        'brightness', 'saturation', 'luminance', 'hue', 'highlights', 'shadows', 'whites', 'blacks'
    ]

    def form_valid(self, form):
        data = {
            'planNo': self.object.plan_no,
            'creator': form.instance.creator,
            'submitter': form.instance.submitter,
            'fundingInUSD': form.instance.funding,
            'objectives': form.instance.objectives,
            'starSystem': form.instance.star_system,
            'telescopeLocation': form.instance.telescope_location,
            'startDate': form.instance.start_date.strftime("%d/%m/%Y %H:%M:%S"),
            'endDate': form.instance.end_date.strftime("%d/%m/%Y %H:%M:%S"),
            'fileType': form.instance.file_type,
            'fileQuality': form.instance.file_quality,
            'colorType': form.instance.color_type,
            'contrast': form.instance.contrast,
            'brightness': form.instance.brightness,
            'saturation': form.instance.saturation,
            'highlights': form.instance.highlights,
            'exposure': form.instance.exposure,
            'shadows': form.instance.shadows,
            'whites': form.instance.whites,
            'blacks': form.instance.blacks,
            'luminance': form.instance.luminance,
            'hue': form.instance.hue
        }
        response = requests.post('http://localhost:8080/test', data)

        form.instance.status = response.json()['status']
        super().form_valid(form)

        results = response.json()['testResult'].split('\n')
        results.pop(0)
        results.pop(0)
        del results[-1]
        print(results)

        test_results = []
        for result in results:
            test, status = result.split(': ', 1)
            test_results.append({'test': test, 'status': status})

        print(test_results)

        return render(self.request, 'astronomer/test_result.html', {'test_results': test_results, 'status': form.instance.status})

    def get(self, request, *args, **kwargs):
        self.form = self.get_object()
        self.form.start_date = self.form.start_date.strftime("%Y-%m-%d %H:%M:%S")
        self.form.end_date = self.form.end_date.strftime("%Y-%m-%d %H:%M:%S")
        return super().get(request, *args, **kwargs)


class ValidateSciencePlanListView(LoginRequiredMixin, ListView):
    model = SciencePlan
    template_name = 'science_observer/validate.html'
    context_object_name = 'sciencePlans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(sciencePlans=SciencePlan.objects.filter(status='TESTED'))
        return context


class ValidateSciencePlanDetailView(LoginRequiredMixin, DetailView):
    model = SciencePlan
    template_name = 'science_observer/validate_detail.html'

    def get(self, request, *args, **kwargs):
        self.form = self.get_object()
        self.form.start_date = self.form.start_date.strftime("%Y-%m-%d %H:%M:%S")
        self.form.end_date = self.form.end_date.strftime("%Y-%m-%d %H:%M:%S")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        status = request.POST.get('status')
        object = self.get_object()
        object.status = status
        object.save()

        requests.post('http://localhost:8080/validate', {'planNo': object.plan_no, 'status': object.status})

        if status == 'VALIDATED':
            return render(request, 'science_observer/validate_pass.html')
        else:
            return render(request, 'science_observer/validate_fail.html')

