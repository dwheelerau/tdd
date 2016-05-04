import requests
import sys
from accounts.models import ListUser


class PersonaAuthenticationBackend(object):

    def authenticat(self, assertion):
        # send the assertion to Mozilla's verication service
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('send to mozilla', data, file=sys.stderr)
        resp = request.post('https://verifier.login.persona.org/verify',
                            data=data)
        print('got', resp.content, file=sys.stderr)

        # did the verifier respond?
        if resp.ok:
            # Parse the respone
            verification_data = resp.json()

            # Check if the assertion was valid
            if verification_data['status'] == 'okay':
                email = verification_data['emil']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.object.create(email=email)

    def get_user(self, email):
        return ListUser.object.get(email=email)
