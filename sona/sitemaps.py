from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Entrepreneurship,Finance

class EntrepreneurshipSitemap(Sitemap):
    def items(self):
        return Entrepreneurship.objects.all()

    def lastmod(self, obj):
        return obj.Create_at

class FinanceSitemap(Sitemap):
    def items(self):
        return Finance.objects.all()

    def lastmod(self, obj):
        return obj.Create_at