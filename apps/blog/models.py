from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.models import TagBase, GenericTaggedItemBase
from taggit.managers import TaggableManager

from core.models import TimeStampedModel


class BlogTag(TagBase):
    description = models.TextField(blank=True, null=True, help_text="Provide a description for this tag")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return f"{self.name} - {self.description[:50]}"


class TaggedBlogPost(GenericTaggedItemBase):
    tag = models.ForeignKey(BlogTag, on_delete=models.CASCADE, related_name="tagged_items")


class PublishedManager(models.Manager):
    """
    Retrieves all posts that have a status of PUBLISHED
    """
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(TimeStampedModel):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    subhead = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    tags = TaggableManager(through=TaggedBlogPost, verbose_name="Tags", blank=True)
    objects = models.Manager()
    published = PublishedManager()

    class meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])
    