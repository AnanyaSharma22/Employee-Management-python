'''
utitlity for all the apps
'''
from django.utils import timezone
from django.conf import settings
from oauth2_provider.models import Application, AccessToken, RefreshToken
from oauthlib.oauth2.rfc6749.tokens import random_token_generator

class UserAccessToken(object):
    ''' UserAccessToken '''

    def __init__(self, request, user, app_name):
        self.request = request
        self.user = user
        self.app_name = app_name

    def create_oauth_token(self):
        '''
        Create Outh token by user_id and application name
        '''
        scopes = 'read write'
        application = Application.objects.get(name=self.app_name)
        expires = timezone.now() + timezone.timedelta(days=settings.USER_TOKEN_EXPIRES)
        access_token = AccessToken.objects.create(
            user=self.user,
            token=random_token_generator(self.request),
            application=application,
            expires=expires,
            scope=scopes)

        RefreshToken.objects.create(
            user=self.user,
            token=random_token_generator(self.request),
            access_token=access_token,
            application=application
        )
        return access_token