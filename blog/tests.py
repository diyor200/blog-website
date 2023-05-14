from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User


class PostListTest(TestCase):
    def setUp(self):
        self.author = User.objects.create(username="testuser")
        self.post = Post.objects.create(title="Test Post",
                                        slug="test-post",
                                        author=self.author,
                                        body="This is a test post",
                                        status=Post.Status.PUBLISHED)

    def test_post_list_view(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        url = reverse('blog:post_detail', args=[self.post.publish.year, self.post.publish.month, self.post.publish.day, self.post.slug])
        response = self.client.get(url)
        print(url)

        # self.assertEqual(response.status_code, 200)
        self.assertEqual(url, self.post.get_absolute_url())

    def test_post_comment_view(self):
        url = reverse('blog:post_comment', args=[self.post.id])
        response = self.client.get(url)
        print(url)
        print(response)

        # self.assertEqual(response.status_code, 200)

