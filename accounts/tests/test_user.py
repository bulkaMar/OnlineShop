import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestUserManager:
    def test_create_user_success(self):
        user = User.objects.create_user(email='test@example.com', full_name='Test User', password='password123')
        assert user.email == 'test@example.com'
        assert user.full_name == 'Test User'
        assert user.check_password('password123') is True

    def test_create_user_no_email(self):
        with pytest.raises(ValueError, match='Email is required!'):
            User.objects.create_user(email='', full_name='Test User', password='password123')

    def test_create_user_no_full_name(self):
        with pytest.raises(ValueError, match='full name is required!'):
            User.objects.create_user(email='test@example.com', full_name='', password='password123')

    def test_create_superuser_success(self):
        user = User.objects.create_superuser(email='admin@example.com', full_name='Admin User', password='admin123')
        assert user.email == 'admin@example.com'
        assert user.full_name == 'Admin User'
        assert user.check_password('admin123') is True
        assert user.is_admin is True
