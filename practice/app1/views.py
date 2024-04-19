from django.shortcuts import render, redirect
from .models import BranchOffice

def submit_form(request):
    if request.method == "POST":
        # Accessing data from the form
        branch_name = request.POST.get('branch_name')
        account_office_name = request.POST.get('account_office_name')
        head_office_name = request.POST.get('head_office_name')
        facility_id = request.POST.get('facility_id')
        establishment = request.POST.get('establishment')
        last_inspection = request.POST.get('last_inspection')
        subsequent_visits = request.POST.get('subsequent_visits')
        articles_in_deposit_comments = request.POST.get('articles_in_deposit_comments')
        articles_beyond_period = request.POST.get('articles_beyond_period')
        articles_beyond_period_comments = request.POST.get('articles_beyond_period_comments')
        article_condition = request.POST.get('article_condition')
        article_condition_comments = request.POST.get('article_condition_comments')
        compare_articles_comments = request.POST.get('compare_articles_comments')
        check_delivery_status = request.POST.get('check_delivery_status')
        check_delivery_status_comments = request.POST.get('check_delivery_status_comments')
        date_of_receipt = request.POST.get('date_of_receipt')
        date_of_delivery = request.POST.get('date_of_delivery')

        previous_inspection_pending = request.POST.get('previous_inspection_pending')
        previous_inspection_comments = request.POST.get('previous_inspection_comments')

        work_carried_out = request.POST.get('work_carried_out')
        work_carried_out_comments = request.POST.get('work_carried_out_comments')

        bo_signage = request.POST.get('bo_signage')
        signage_comments = request.POST.get('signage_comments')
        
        look_and_feel = request.POST.get('look_and_feel')
        look_and_feel_comments = request.POST.get('look_and_feel_comments')




        # Create BranchOffice object
        branch_office = BranchOffice.objects.create (
            branch_name=branch_name,
            account_office_name=account_office_name,
            head_office_name=head_office_name,
            facility_id=facility_id,
            establishment=establishment,
            last_inspection=last_inspection,
            subsequent_visits=subsequent_visits,
            articles_in_deposit_comments=articles_in_deposit_comments,
            articles_beyond_period=articles_beyond_period,
            articles_beyond_period_comments=articles_beyond_period_comments,
            article_condition=article_condition,
            article_condition_comments=article_condition_comments,
            compare_articles_comments=compare_articles_comments,
            check_delivery_status=check_delivery_status,
            check_delivery_status_comments=check_delivery_status_comments,
            date_of_receipt=date_of_receipt,
            date_of_delivery=date_of_delivery,
            previous_inspection_pending=previous_inspection_pending,
            previous_inspection_comments=previous_inspection_comments,
            work_carried_out=work_carried_out,
            work_carried_out_comments=work_carried_out_comments,
             look_and_feel=look_and_feel,
            look_and_feel_comments=look_and_feel_comments,
            bo_signage=bo_signage,
            signage_comments=signage_comments,
        )

        # Create InspectionReport object
        # inspection_report = InspectionReport.objects.create(
        #     previous_inspection_pending=previous_inspection_pending,
        #     previous_inspection_comments=previous_inspection_comments
        # )

        # # Create WorkCarriedOut object
        # work_carried_out = request.POST.get('work_carried_out')
        # work_carried_out_comments = request.POST.get('work_carried_out_comments')
        # work_carried_out = WorkCarriedOut.objects.create(
            # work_carried_out=work_carried_out,
            # work_carried_out_comments=work_carried_out_comments
        # )

        # # Create Signage object
        # bo_signage = request.POST.get('bo_signage')
        # signage_comments = request.POST.get('signage_comments')
        # signage = Signage.objects.create(
            # bo_signage=bo_signage,
            # signage_comments=signage_comments
        # )

        # # Create LookAndFeel object
        # look_and_feel = request.POST.get('look_and_feel')
        # look_and_feel_comments = request.POST.get('look_and_feel_comments')
        # lookandfeel = LookAndFeel.objects.create(
        #     look_and_feel=look_and_feel,
        #     look_and_feel_comments=look_and_feel_comments
        # )

        # Create MailOperations object
      

       # return redirect('success_page')  # Redirect to success page or any other page
    else:
        return render(request, 'main1.html') 
     # Render form template if request method is GET
    return render(request, 'main1.html')
