import json
import re

from django.conf import settings
from django.contrib.auth import authenticate, login

from .models import LOT

uuidRegex = re.compile("^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$")


class LOTMiddleware(object):
    def process_request(self, request):
        lot_uuid = request.GET.get(settings.LOT_MIDDLEWARE_PARAM_NAME, None)
        if lot_uuid:
            if not uuidRegex.match(lot_uuid):
                return None

            try:
                lot = LOT.objects.get(uuid=lot_uuid)
            except LOT.DoesNotExist:
                return None

            if not lot.verify():
                if lot.delete_on_fail():
                    lot.delete()
                return None

            user = authenticate(lot_uuid=lot_uuid)
            login(request, user)

            try:
                session_data = json.loads(lot.session_data)
                request.session.update(session_data)
            except Exception:
                # If not correctly serialized not set the session_data
                pass

            if lot.is_one_time():
                lot.delete()


class LOTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        # Incorporate your existing authentication logic
        try:
            token = request.META['HTTP_X_AUTH_TOKEN']
        except KeyError:
            return None  # No token, continue without authentication

        if not uuidRegex.match(token):
            return None  # Invalid token format

        try:
            lot = LOT.objects.select_related('user').get(uuid=token)
        except LOT.DoesNotExist:
            return None  # Token doesn't match a valid LOT

        if not lot.verify():
            if lot.delete_on_fail():
                lot.delete()
            return None  # LOT verification failed

        request.user = lot.user  # Authenticate the user

        try:
            session_data = json.loads(lot.session_data)
            request.session.update(session_data)
        except json.JSONDecodeError:  # Handle potential errors
            pass  # Ignore if session_data is invalid

        if lot.is_one_time():
            lot.delete()

        # Pass the request on to the next middleware or the view
        response = self.get_response(request) 

        # You can optionally add response modification here:
        # ...

        return response  
