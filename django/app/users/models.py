from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def set_full_name(self, input):
        split = input.split(' ')
        self.first_name = split[0]
        if len(split) >= 2:
            self.last_name = ' '.join(split[1:])

    full_name = property(get_full_name, set_full_name)

    def get_joined(self):
        return self.date_joined

    def set_joined(self, input):
        self.date_joined = input

    joined = property(get_joined, set_joined)
