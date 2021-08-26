from django.shortcuts import render
from .models import AnotationTrack
from django.core import serializers
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.validators import FileExtensionValidator

def upload(request):
    """Handle uploads of files that specify genomic regions"""
    # TODO: Handle uploads
    if request.method == 'GET': 
        return render(request, "genome/upload.html")
    if request.method == 'POST':
        print(request.FILES)
        form = AnotationTrack()
        file = request.FILES.get("bedFile").readlines()[1:]
        for row in file:
            #  TODO: add dynamic verification for valid genome .bed files not just by specified lenghts of 3 or 8...
            listValues = row.decode('utf-8').split('\t')
            # hacky way to dynamicall add the values.
            listLen = len(listValues)
            if listLen == 8: 
                newTrack = AnotationTrack(
                    chrom = listValues[0],
                    chromStart = listValues[1],
                    chromEnd = listValues[2],
                    name = listValues[3],
                    score = listValues[4],
                    strand = listValues[5],
                    thickStart = listValues[6],
                    thickEnd = listValues[7]
                )
                newTrack.save()
            if listLen == 3:
                newTrack = AnotationTrack(
                    chrom = listValues[0],
                    chromStart = listValues[1],
                    chromEnd = listValues[2],
                )
                newTrack.save()
        return render(request, "genome/upload.html")

def view(request):
    return render(request, "genome/view.html")    

def viewData(request):
    # Currenlty just retrives all the records that exists in the sqllite db. 
    if request.method == 'GET':
        dataQuery = AnotationTrack.objects.all()
        # Code to add pagination...
        # paginatedData = Paginator(dataQuery,"<<Add Requested record counts>>")
        # page = paginatedData.page(<<Add Page Number to get data from>>)
        # pageData = page.object_list <<This is the page data >>
        data = serializers.serialize('json', dataQuery)
        return HttpResponse(data, content_type='application/json')