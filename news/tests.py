from django.test import TestCase
from news.models import CustomUser, NewsPost
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your tests here.
class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='freddy@g.com', password = 'drovehomesave')
        self.assertEqual(user.email, 'freddy@g.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="drovehomesave")

    def test_create_superuser(self):
            User = get_user_model()
            admin_user = User.objects.create_superuser(email='wambua@g.com', password='thatsmycar')
            self.assertEqual(admin_user.email, 'wambua@g.com')
            self.assertTrue(admin_user.is_active)
            self.assertTrue(admin_user.is_staff)
            self.assertTrue(admin_user.is_superuser)
            try:
                # username is None for the AbstractUser option
                # username does not exist for the AbstractBaseUser option
                self.assertIsNone(admin_user.username)
            except AttributeError:
                pass
            with self.assertRaises(ValueError):
                User.objects.create_superuser(
                    email='wambua@g.com', password='thatsmycar', is_superuser=False)

class NewsPostTestClass(TestCase):
    def setUp(self):
        self.test_user_post = CustomUser(username='Master')
        self.test_user_post.save()
        self.post_test = NewsPost(title='Hood Meeting', post='You are all welcome for the hood meeting')

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, NewsPost))

    def test_save_post(self):
        self.post_test.save()
        posts = NewsPost.objects.all()
        self.assertTrue(len(posts)>0)

    def test_delete_post(self):
        self.post_test.delete()
        posts = NewsPost.objects.all()
        self.assertTrue(len(posts)<1)