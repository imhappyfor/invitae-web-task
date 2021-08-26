from django.db import models

# Create your models here.
class AnotationTrack(models.Model):
    chrom = models.CharField(max_length=10)
    chromStart = models.IntegerField()
    chromEnd = models.IntegerField()
    name = models.CharField(max_length=50 , blank=True, null=True)
    score = models.IntegerField(blank=True,null=True)
    strand = models.CharField(max_length=1,blank=True,null=True)
    thickStart = models.IntegerField(blank=True,null=True)
    thickEnd = models.IntegerField(blank=True,null=True)

    class Meta:
        ordering = ('chrom',)