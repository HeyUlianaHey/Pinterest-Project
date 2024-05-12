from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Введите почту!')
        if not username:
            raise ValueError('Введите имя пользователя!')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password) # hash raw password and set
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self.db)
        return self.create_user(email, username, password)
