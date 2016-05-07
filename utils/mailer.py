import six
from django.core.mail import send_mail

from django.conf import settings


class BaseMailer(object):
    def __init__(self):
        self._slug = None
        self.no_replay_mail = 'no-replay@ungleich.ch'

        if not hasattr(self, '_to'):
            self._to = None

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, val):
        assert isinstance(val, six.string_types), "slug is not string: %r" % val
        self._slug = val

    @property
    def registration(self):
        return self.message

    @registration.setter
    def registration(self, val):
        msg = "registration is not dict with fields subject,message"
        assert type(val) is dict, msg
        assert val.get('subject') and val.get('message'), msg
        self._message, self._subject, self._from = (
            val.get('message'), val.get('subject'), val.get('from'))
        assert isinstance(self.slug, six.string_types), 'slug not set'

    def send_mail(self, to=None):
        if not to:
            to = self._to
        if not self.message:
            raise NotImplementedError
        send_mail(self._subject, self._message, self.no_replay_mail, [to])


class DigitalGlarusRegistrationMailer(BaseMailer):
    message = settings.REGISTRATION_MESSAGE

    def __init__(self, slug):
        self.slug = slug
        self.registration = self.message
        self._message = self._message.format(slug=self._slug)
        super().__init__()
