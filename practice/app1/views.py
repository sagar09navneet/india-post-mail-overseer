from django.shortcuts import redirect, render
from .models import BranchOffice
from django.urls import reverse

def submit_form(request):
    if request.method == "POST":
        # Accessing data and creating a new object
        branch_name = request.POST.get('branch_name')
        account_office_name = request.POST.get('account_office_name')
        head_office_name = request.POST.get('head_office_name')
        facility_id = request.POST.get('facility_id')
        establishment = request.POST.get('establishment')
        last_inspection = request.POST.get('last_inspection')
        subsequent_visits = request.POST.get('subsequent_visits')
        #print(request.POST.get())
        
        # Create BranchOffice object with the retrieved data
        branch_office = BranchOffice.objects.create(
            branch_name=branch_name,
            account_office_name=account_office_name,
            head_office_name=head_office_name,
            facility_id=facility_id,
            establishment=establishment,
            last_inspection=last_inspection,
            subsequent_visits=subsequent_visits
        )
        
        # Redirect to a success page or perform any other actions as needed
        return redirect('success_page')
    
    # If the request method is not POST, render the form template
    return render(request, 'main1.html')
