import re

from django.http import HttpResponse , HttpResponseNotAllowed , HttpResponseBadRequest , HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

from API.Global_Data import CACHE , GET_AUTHORITY_PATH , POST_AUTHORITY_PATH


class Middleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'GET':
            if request.path in GET_AUTHORITY_PATH:
                token = request.GET.get('token')
                if CACHE.get(token):
                    pass
                else:
                    return HttpResponseBadRequest('用户未登陆')

        elif request.method == 'POST':
            for patten in POST_AUTHORITY_PATH:
                if re.match(patten, request.path):
                    token = request.POST.get('token')
                    if CACHE.get(token):
                        pass
                    else:
                        return HttpResponseBadRequest('用户未登陆')

    def process_response(self, request, response):
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_exception(self, request, exception):
        return HttpResponseForbidden(data={'message': '请求错误'})

    def process_template_response(self, request, response):
        return response
