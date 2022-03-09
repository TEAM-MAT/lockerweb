from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class KickedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        kicked = request.session.pop('kicked', None)
        if kicked:
            messages.info(request, '중복로그인이 감지되어 로그아웃됩니다.')
            auth_logout(request)
            return redirect(settings.LOGIN_URL)