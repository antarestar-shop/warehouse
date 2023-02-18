from django.shortcuts import render, redirect
from sortir.models import *
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required

def home(req):

    return render(req,'home.html')

@login_required(login_url='login')
def sortir(req):
    
    now = datetime.datetime.now()
    total = Sday.objects.count()
    double = Dday.objects.count()
    checked = Sday.objects.last()
    
    # scanner = Scanner.objects.all()
    angel = Sday.objects.filter(scanner='angel').count()
    latif = Sday.objects.filter(scanner='latif').count()
    windi = Sday.objects.filter(scanner='windi').count()
    antare = Sday.objects.filter(scanner='antarestar').count()

    

    if req.POST.get('reset'):
        Sday.objects.all().delete()
        Dday.objects.all().delete()
        return redirect('sortir')

    if now.hour == 0 and now.minute == 0:
        # Reset the model
        Sday.objects.all().delete()
        Dday.objects.all().delete()
        return redirect('sortir')


    if req.POST:
        sortir = Sortir()
        double = Double()
        sday = Sday()
        dday = Dday()

        barcode = req.POST.get('barcode')
        scanner = req.POST.get('scanner')


        if Sortir.objects.filter(barcode=barcode).exists():
            create = Sortir.objects.values_list('created_at', flat=True).get(barcode=barcode)
            create_string = create.strftime("%d %B, %Y ")
            output_string = "pada tanggal : " + create_string
            messages.warning(req, 'Barcode ini sudah pernah digunakan ' + output_string)
            double.barcode = barcode
            dday.jumlah = barcode
            double.scanner = scanner

            dday.save()
            double.save() 

            # test = { 'creat':creat }

            return redirect('sortir')
        else:

            sortir.barcode = barcode
            sday.jumlah = barcode
            sortir.scanner = scanner
            sday.scanner = scanner

            sday.save()
            sortir.save()

            return redirect('sortir')

    context = {
        'total':total,
        'double':double,
        'checked':checked,
        # 'scanner':scanner, 
        'angel':angel,
        'latif':latif,
        'windi':windi,
        'antare':antare,    
        
    }

    return render(req,'sortir.html',context)
