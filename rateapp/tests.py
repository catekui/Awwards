from django.test import TestCase
from .models import Profile, Project, Review

# Create your tests here.


class ProfileTestClass(TestCase):

  # Set up method
  def setUp(self):
    self.prof= Profile(bio = 'Titl1', prof_pic = 'profpic.png' )

  # Testing  instance
  def test_instance(self):
    self.assertTrue(isinstance(self.prof,Profile))

  # Testing String representation Method
  def test_string_representation(self):
    profile = Profile(bio="sometext")
    self.assertEqual(str(profile), 'sometext')

class ReviewTestClass(TestCase):

  # Set up method
  def setUp(self):
    self.rev= Review(bio = 'Titl1', prof_pic = 'profpic.png' )

  # Testing  instance
  def test_instance(self):
    self.assertTrue(isinstance(self.prof,Profile))

  # Testing String representation Method
  def test_string_representation(self):
    profile = Profile(bio="sometext")
    self.assertEqual(str(profile), 'sometext')