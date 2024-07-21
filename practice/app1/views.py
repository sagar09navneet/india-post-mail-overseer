from django.shortcuts import render, redirect
from .models import BranchOffice
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse


def submit_form(request):
    if request.method == "POST":
        print(request.POST)
        # Accessing data from the form
        branch_name = request.POST.get('branch_name')
        account_office_name = request.POST.get('account_office_name')
        head_office_name = request.POST.get('head_office_name')
        facility_id = request.POST.get('facility_id')
        establishment = request.POST.get('establishment')
        last_inspection = request.POST.get('last_inspection')
        subsequent_visits = request.POST.get('subsequent_visits')

        articles_in_deposit_comments_acc = request.POST.get('articles_in_deposit_comments_acc')
        articles_beyond_period_acc = request.POST.get('articles_beyond_period_acc')
        articles_beyond_period_comments_acc = request.POST.get('articles_beyond_period_comments_acc')
        article_condition_acc = request.POST.get('article_condition_acc')
        article_condition_comments_acc = request.POST.get('article_condition_comments_acc')
        compare_articles_comments_acc = request.POST.get('compare_articles_comments_acc')

        articles_in_deposit_comments_ord = request.POST.get('articles_in_deposit_comments_ord')
        articles_beyond_period_ord = request.POST.get('articles_beyond_period_ord')
        articles_beyond_period_comments_ord = request.POST.get('articles_beyond_period_comments_ord')
        article_condition_ord = request.POST.get('article_condition_ord')
        article_condition_comments_ord = request.POST.get('article_condition_comments_ord')
        compare_articles_comments_ord = request.POST.get('compare_articles_comments_ord')


        previous_inspection_pending = request.POST.get('previous_inspection_pending')
        previous_inspection_comments = request.POST.get('previous_inspection_comments')

        work_carried_out = request.POST.get('work_carried_out')
        work_carried_out_comments = request.POST.get('work_carried_out_comments')

        bo_signage = request.POST.get('bo_signage')
        signage_comments = request.POST.get('signage_comments')
        
        look_and_feel = request.POST.get('look_and_feel')
        look_and_feel_comments = request.POST.get('look_and_feel_comments')


        check_delivery_status_acc = []
        for key in request.POST:
            if key.startswith('check_delivery_status_acc'):
                check_delivery_status_acc.append(request.POST[key])

        check_delivery_status_comments_acc = []
        for key in request.POST:
            if key.startswith('check_delivery_status_comments_acc'):
                check_delivery_status_comments_acc.append(request.POST[key])

        date_of_receipt_acc = []
        for key in request.POST:
            if key.startswith('date_of_receipt_acc'):
                date_of_receipt_acc.append(request.POST[key])

        date_of_delivery_acc = []
        for key in request.POST:
            if key.startswith('date_of_delivery_acc'):
                date_of_delivery_acc.append(request.POST[key])


        check_delivery_status_ord = []
        for key in request.POST:
            if key.startswith('check_delivery_status_ord'):
                check_delivery_status_ord.append(request.POST[key])

        check_delivery_status_comments_ord = []
        for key in request.POST:
            if key.startswith('check_delivery_status_comments_ord'):
                check_delivery_status_comments_ord.append(request.POST[key])

        date_of_receipt_ord = []
        for key in request.POST:
            if key.startswith('date_of_receipt_ord'):
                date_of_receipt_ord.append(request.POST[key])

        date_of_delivery_ord = []
        for key in request.POST:
            if key.startswith('date_of_delivery_ord'):
                date_of_delivery_ord.append(request.POST[key])


        no_of_letter_boxes = request.POST.get('no_of_letter_boxes')
        lb_condition = request.POST.get('lb_condition')
        lb_condition_comments = request.POST.get('lb_condition_comments')
        lb_clearance = request.POST.get('lb_clearance')
        lb_clearance_comments = request.POST.get('lb_clearance_comments')

        last_acknowledged_balance = request.POST.get('last_acknowledged_balance')
        last_acknowledged_balance_date = request.POST.get('last_acknowledged_balance_date')
        last_acknowledged_balance_comments = request.POST.get('last_acknowledged_balance_comments')
        cash_value = request.POST.get('cash_value')
        stamp_value = request.POST.get('stamp_value')
        details_in_stock_comments = request.POST.get('details_in_stock_comments')
        cash_balance_correct = request.POST.get('cash_balance_correct')
        cash_balance_comments = request.POST.get('cash_balance_comments')
        wallet_balance = request.POST.get('wallet_balance')
        wallet_balance_date = request.POST.get('wallet_balance_date')
        physical_balance = request.POST.get('physical_balance')
        physical_balance_date = request.POST.get('physical_balance_date')


        invoice_stamp = []
        for key in request.POST:
            if key.startswith('invoice_stamp'):
                invoice_stamp.append(request.POST[key])

        inventory = []
        for key in request.POST:
            if key.startswith('inventory'):
                inventory.append(request.POST[key])


        postage_due=request.POST.get('postage_due')
        postage_due_comments=request.POST.get('postage_due_comments')


        date_of_account = []
        for key in request.POST:
            if key.startswith('date_of_account'):
                date_of_account.append(request.POST[key])

        bo_slip = []
        for key in request.POST:
            if key.startswith('bo_slip'):
                bo_slip.append(request.POST[key])

        bo_account = []
        for key in request.POST:
            if key.startswith('bo_account'):
                bo_account.append(request.POST[key])

        question_9= request.POST.get('question_9')



        number_of_mo_issued = request.POST.get('number_of_mo_issued')
        number_of_mo_received = request.POST.get('number_of_mo_received')
        payee_details1 = request.POST.get('payee_details1')
        payee_details2 = request.POST.get('payee_details2')
        payee_details3 = request.POST.get('payee_details3')
        payee_details4 = request.POST.get('payee_details4')
        payee_details5 = request.POST.get('payee_details5')


        article_number = []
        for key in request.POST:
            if key.startswith('article_number'):
                article_number.append(request.POST[key])

        article_issued_date = []
        for key in request.POST:
            if key.startswith('article_issued_date'):
                article_issued_date.append(request.POST[key])

        article_received_date = []
        for key in request.POST:
            if key.startswith('article_received_date'):
                article_received_date.append(request.POST[key])


        article_delivered_date = []
        for key in request.POST:
            if key.startswith('article_delivered_date'):
                article_delivered_date.append(request.POST[key])

        VPMO_issued_date = []
        for key in request.POST:
            if key.startswith('VPMO_issued_date'):
                VPMO_issued_date.append(request.POST[key])

        VPMO_issued_comments = []
        for key in request.POST:
            if key.startswith('VPMO_issued_comments'):
                VPMO_issued_comments.append(request.POST[key])



        demurrage_fees_comments = request.POST.get('demurrage_fees_comments')
        list_of_mo_received =  request.POST.get('list_of_mo_received')
        list_of_mo_received_comments =  request.POST.get('list_of_mo_received_comments')
        eMO_payment_limit = request.POST.get('eMO_payment_limit')
        eMO_payment_limit_comments = request.POST.get('eMO_payment_limit_comments')


        BO_journals = request.POST.get('BO_journals')
        BO_journals_comments = request.POST.get('BO_journals_comments')
        entries_comparison =  request.POST.get('entries_comparison')
        entries_comparison_comments = request.POST.get('entries_comparison_comments')
        cheques_received = request.POST.get('cheques_received')
        cheques_received_comments = request.POST.get('cheques_received_comments')
        passbook_collection_register = request.POST.get('passbook_collection_register')
        passbook_collection_register_comments = request.POST.get('passbook_collection_register_comments')
        number_of_passbooks_deposit =  request.POST.get('number_of_passbooks_deposit')
        number_of_passbooks_deposit_comments = request.POST.get('number_of_passbooks_deposit_comments')


        account_number_ao = []
        for key in request.POST:
            if key.startswith('account_number_ao'):
                account_number_ao.append(request.POST[key])

        all_schemes = []
        for key in request.POST:
            if key.startswith('all_schemes'):
                all_schemes.append(request.POST[key])




        book_no_SB26 = []
        for key in request.POST:
            if key.startswith('book_no_SB26'):
                book_no_SB26.append(request.POST[key])

        receipt_no_from_SB26 = []
        for key in request.POST:
            if key.startswith('receipt_no_from_SB26'):
                receipt_no_from_SB26.append(request.POST[key])

        date_from_SB26 = []
        for key in request.POST:
            if key.startswith('date_from_SB26'):
                date_from_SB26.append(request.POST[key])
        amount_from_SB26 = []
        for key in request.POST:
            if key.startswith('amount_from_SB26'):
                amount_from_SB26.append(request.POST[key])

        receipt_no_to_SB26 = []
        for key in request.POST:
            if key.startswith('receipt_no_to_SB26'):
                receipt_no_to_SB26.append(request.POST[key])

        date_to_SB26 = []
        for key in request.POST:
            if key.startswith('date_to_SB26'):
                date_to_SB26.append(request.POST[key])



        amount_to_SB26 = []
        for key in request.POST:
            if key.startswith('amount_to_SB26'):
                amount_to_SB26.append(request.POST[key])

        blank_receipt_SB26 = []
        for key in request.POST:
            if key.startswith('blank_receipt_SB26'):
                blank_receipt_SB26.append(request.POST[key])



        acquittance_comments = []
        for key in request.POST:
            if key.startswith('acquittance_comments'):
                acquittance_comments.append(request.POST[key])


        unused_receipts_comments = []
        for key in request.POST:
            if key.startswith('unused_receipts_comments'):
                unused_receipts_comments.append(request.POST[key])



        reference_number_comments = []
        for key in request.POST:
            if key.startswith('reference_number_comments'):
                reference_number_comments.append(request.POST[key])




        book_no_SB28 = []
        for key in request.POST:
            if key.startswith('book_no_SB28'):
                book_no_SB28.append(request.POST[key])

        receipt_no_from_SB28 = []
        for key in request.POST:
            if key.startswith('receipt_no_from_SB28'):
                receipt_no_from_SB28.append(request.POST[key])

        date_from_SB28 = []
        for key in request.POST:
            if key.startswith('date_from_SB28'):
                date_from_SB28.append(request.POST[key])
        amount_from_SB28 = []
        for key in request.POST:
            if key.startswith('amount_from_SB28'):
                amount_from_SB28.append(request.POST[key])

        receipt_no_to_SB28 = []
        for key in request.POST:
            if key.startswith('receipt_no_to_SB28'):
                receipt_no_to_SB28.append(request.POST[key])

        date_to_SB28 = []
        for key in request.POST:
            if key.startswith('date_to_SB28'):
                date_to_SB28.append(request.POST[key])



        amount_to_SB28 = []
        for key in request.POST:
            if key.startswith('amount_to_SB28'):
                amount_to_SB28.append(request.POST[key])

        blank_receipt_SB28 = []
        for key in request.POST:
            if key.startswith('blank_receipt_SB28'):
                blank_receipt_SB28.append(request.POST[key])











        book_no_MS87 = []
        for key in request.POST:
            if key.startswith('book_no_MS87'):
                book_no_MS87.append(request.POST[key])

        receipt_no_from_MS87 = []
        for key in request.POST:
            if key.startswith('receipt_no_from_MS87'):
                receipt_no_from_MS87.append(request.POST[key])

        date_from_MS87 = []
        for key in request.POST:
            if key.startswith('date_from_MS87'):
                date_from_MS87.append(request.POST[key])
        amount_from_MS87 = []
        for key in request.POST:
            if key.startswith('amount_from_MS87'):
                amount_from_MS87.append(request.POST[key])

        receipt_no_to_MS87 = []
        for key in request.POST:
            if key.startswith('receipt_no_to_MS87'):
                receipt_no_to_MS87.append(request.POST[key])

        date_to_MS87 = []
        for key in request.POST:
            if key.startswith('date_to_MS87'):
                date_to_MS87.append(request.POST[key])

        amount_to_MS87 = []
        for key in request.POST:
            if key.startswith('amount_to_MS87'):
                amount_to_MS87.append(request.POST[key])

        blank_receipt_MS87 = []
        for key in request.POST:
            if key.startswith('blank_receipt_MS87'):
                blank_receipt_MS87.append(request.POST[key])






        account_no_1 = []
        for key in request.POST:
            if key.startswith('account_no_1'):
                account_no_1.append(request.POST[key])


        scheme_type_1 = []
        for key in request.POST:
            if key.startswith('scheme_type_1'):
                scheme_type_1.append(request.POST[key])


        last_transaction_date_1 = []
        for key in request.POST:
            if key.startswith('last_transaction_date_1'):
                last_transaction_date_1.append(request.POST[key])


        deposit_1 = []
        for key in request.POST:
            if key.startswith('deposit_1'):
                deposit_1.append(request.POST[key])


        withdrawal_1 = []
        for key in request.POST:
            if key.startswith('withdrawal_1'):
                withdrawal_1.append(request.POST[key])
        balance_1 = []
        for key in request.POST:
            if key.startswith('balance_1'):
                balance_1.append(request.POST[key])

        sms_alert_1= []
        for key in request.POST:
            if key.startswith('sms_alert_1'):
                sms_alert_1.append(request.POST[key])


        system_receipt_1= []
        for key in request.POST:
            if key.startswith('system_receipt_1'):
                system_receipt_1.append(request.POST[key])

        new_passbook_entry_1= []
        for key in request.POST:
            if key.startswith('new_passbook_entry_1'):
                new_passbook_entry_1.append(request.POST[key])





        account_no_2 = []
        for key in request.POST:
            if key.startswith('account_no_2'):
                account_no_2.append(request.POST[key])


        scheme_type_2 = []
        for key in request.POST:
            if key.startswith('scheme_type_2'):
                scheme_type_2.append(request.POST[key])


        last_transaction_date_2 = []
        for key in request.POST:
            if key.startswith('last_transaction_date_2'):
                last_transaction_date_2.append(request.POST[key])


        deposit_2 = []
        for key in request.POST:
            if key.startswith('deposit_2'):
                deposit_2.append(request.POST[key])


        withdrawal_2 = []
        for key in request.POST:
            if key.startswith('withdrawal_2'):
                withdrawal_2.append(request.POST[key])
        balance_2 = []
        for key in request.POST:
            if key.startswith('balance_2'):
                balance_2.append(request.POST[key])

        sms_alert_2 = []
        for key in request.POST:
            if key.startswith('sms_alert_2'):
                sms_alert_2.append(request.POST[key])


        system_receipt_2= []
        for key in request.POST:
            if key.startswith('system_receipt_2'):
                system_receipt_2.append(request.POST[key])

        new_passbook_entry_2= []
        for key in request.POST:
            if key.startswith('new_passbook_entry_2'):
                new_passbook_entry_2.append(request.POST[key])







        account_no_2 = []
        for key in request.POST:
            if key.startswith('account_no_2'):
                account_no_2.append(request.POST[key])


        scheme_type_2 = []
        for key in request.POST:
            if key.startswith('scheme_type_2'):
                scheme_type_2.append(request.POST[key])


        last_transaction_date_2 = []
        for key in request.POST:
            if key.startswith('last_transaction_date_2'):
                last_transaction_date_2.append(request.POST[key])


        deposit_2 = []
        for key in request.POST:
            if key.startswith('deposit_2'):
                deposit_2.append(request.POST[key])


        withdrawal_2 = []
        for key in request.POST:
            if key.startswith('withdrawal_2'):
                withdrawal_2.append(request.POST[key])
        balance_2 = []
        for key in request.POST:
            if key.startswith('balance_2'):
                balance_2.append(request.POST[key])

        sms_alert_2 = []
        for key in request.POST:
            if key.startswith('sms_alert_2'):
                sms_alert_2.append(request.POST[key])


        system_receipt_2= []
        for key in request.POST:
            if key.startswith('system_receipt_2'):
                system_receipt_2.append(request.POST[key])

        new_passbook_entry_2= []
        for key in request.POST:
            if key.startswith('new_passbook_entry_2'):
                new_passbook_entry_2.append(request.POST[key])


































        discrepancy_comments = request.POST.get('discrepancy_comments')
        passbook_verified = request.POST.get('passbook_verified')
        passbook_verified_comments = request.POST.get('passbook_verified_comments')


        account_details_1 = request.POST.get('account_details_1')
        account_details_2 = request.POST.get('account_details_2')
        account_details_3 =request.POST.get('account_details_3')
        account_details_4 = request.POST.get('account_details_4')
        account_details_5 = request.POST.get('account_details_5')




        authorization_forms_available = request.POST.get('authorization_forms_available')
        authorization_forms_comments = request.POST.get('authorization_forms_comments')
        inventory_levels_maintained = request.POST.get('inventory_levels_maintained')
        inventory_comments =request.POST.get('inventory_comments')
        doorstep_service_requests = request.POST.get('doorstep_service_requests')
        doorstep_service_comments = request.POST.get('doorstep_service_comments')
        applications_received = request.POST.get('applications_received')
        applications_received_comments = request.POST.get('applications_received_comments')
        help_desk_maintained = request.POST.get('help_desk_maintained')
        help_desk_comments =request.POST.get('help_desk_comments')
        qr_displayed = request.POST.get('qr_displayed')
        qr_comments = request.POST.get('qr_comments')

        pli_rpli_policy_number_1 =request.POST.get('pli_rpli_policy_number_1')
        dlt_1 = request.POST.get('dlt_1')
        account_number_1 = request.POST.get('account_number_1')
        pli_rpli_transactions_type_1 = request.POST.get('pli_rpli_transactions_type_1')

        pli_rpli_policy_number_2 = request.POST.get('pli_rpli_policy_number_2')
        dlt_2 =request.POST.get('dlt_2')
        account_number_2 = request.POST.get('account_number_2')
        pli_rpli_transactions_type_2 = request.POST.get('pli_rpli_transactions_type_2')
        pli_rpli_proposals = request.POST.get('pli_rpli_proposals')
        dispatched_to_account_office = request.POST.get('dispatched_to_account_office')

        pli_rpli_publicity_material = request.POST.get('pli_rpli_publicity_material')
        pli_rpli_publicity_comments = request.POST.get('pli_rpli_publicity_comments')


        feedback_comments = request.POST.get('feedback_comments')






















        # Create BranchOffice object
        branch_office = BranchOffice.objects.create (
            branch_name=branch_name,
            account_office_name=account_office_name,
            head_office_name=head_office_name,
            facility_id=facility_id,
            establishment=establishment,
            last_inspection=last_inspection,
            subsequent_visits=subsequent_visits,

            articles_in_deposit_comments_acc=articles_in_deposit_comments_acc,
            articles_beyond_period_acc=articles_beyond_period_acc,
            articles_beyond_period_comments_acc=articles_beyond_period_comments_acc,
            article_condition_acc=article_condition_acc,
            article_condition_comments_acc=article_condition_comments_acc,
            compare_articles_comments_acc=compare_articles_comments_acc,

            articles_in_deposit_comments_ord=articles_in_deposit_comments_ord,
            articles_beyond_period_ord=articles_beyond_period_ord,
            articles_beyond_period_comments_ord=articles_beyond_period_comments_ord,
            article_condition_ord=article_condition_ord,
            article_condition_comments_ord=article_condition_comments_ord,
            compare_articles_comments_ord=compare_articles_comments_ord,



            check_delivery_status_acc=check_delivery_status_acc,
            check_delivery_status_comments_acc=check_delivery_status_comments_acc,
            date_of_receipt_acc=date_of_receipt_acc,
            date_of_delivery_acc=date_of_delivery_acc,

            check_delivery_status_ord=check_delivery_status_ord,
            check_delivery_status_comments_ord=check_delivery_status_comments_ord,
            date_of_receipt_ord=date_of_receipt_ord,
            date_of_delivery_ord=date_of_delivery_ord,

            previous_inspection_pending=previous_inspection_pending,
            previous_inspection_comments=previous_inspection_comments,
            work_carried_out=work_carried_out,
            work_carried_out_comments=work_carried_out_comments,
            look_and_feel=look_and_feel,
            look_and_feel_comments=look_and_feel_comments,
            bo_signage=bo_signage,
            signage_comments=signage_comments,
            

            no_of_letter_boxes=no_of_letter_boxes,
            lb_condition=lb_condition,
            lb_condition_comments=lb_condition_comments,
            lb_clearance=lb_clearance,
            lb_clearance_comments=lb_clearance_comments,



            last_acknowledged_balance = last_acknowledged_balance,
            last_acknowledged_balance_date = last_acknowledged_balance_date,
            last_acknowledged_balance_comments = last_acknowledged_balance_comments,
            cash_value =cash_value,
            stamp_value = stamp_value,
            details_in_stock_comments = details_in_stock_comments,
            cash_balance_correct =cash_balance_correct,
            cash_balance_comments = cash_balance_comments,
            wallet_balance = wallet_balance,
            wallet_balance_date = wallet_balance_date,
            physical_balance = physical_balance,
            physical_balance_date = physical_balance_date,
            invoice_stamp=invoice_stamp,
            inventory=inventory,


            postage_due=postage_due,
            postage_due_comments=postage_due_comments,
            date_of_account=date_of_account,
            bo_slip=bo_slip,
            bo_account=bo_account,
            question_9 = question_9,


            number_of_mo_issued = number_of_mo_issued,
            number_of_mo_received =number_of_mo_received,
            payee_details1 =payee_details1,
            payee_details2 = payee_details2,
            payee_details3 =payee_details3,
            payee_details4 = payee_details4,
            payee_details5 = payee_details5,

            article_number =article_number,
            article_issued_date = article_issued_date,
            article_received_date =article_received_date,
            article_delivered_date = article_delivered_date,
            VPMO_issued_date =VPMO_issued_date,
            VPMO_issued_comments = VPMO_issued_comments,

            demurrage_fees_comments =demurrage_fees_comments ,
            list_of_mo_received = list_of_mo_received ,
            list_of_mo_received_comments =  list_of_mo_received_comments,
            eMO_payment_limit = eMO_payment_limit,
            eMO_payment_limit_comments = eMO_payment_limit_comments,



            BO_journals = BO_journals,
            BO_journals_comments = BO_journals_comments,
            entries_comparison =  entries_comparison,
            entries_comparison_comments = entries_comparison_comments,
            cheques_received =cheques_received,
            cheques_received_comments = cheques_received_comments,
            passbook_collection_register = passbook_collection_register,
            passbook_collection_register_comments = passbook_collection_register_comments,
            number_of_passbooks_deposit =number_of_passbooks_deposit,
            number_of_passbooks_deposit_comments = number_of_passbooks_deposit_comments,


            
            account_number_ao=account_number_ao,
            all_schemes=all_schemes,

            book_no_SB26=book_no_SB26,
            receipt_no_from_SB26 =receipt_no_from_SB26,
            date_from_SB26 = date_from_SB26,
            amount_from_SB26 = amount_from_SB26,
            receipt_no_to_SB26 = receipt_no_to_SB26,
            date_to_SB26 =date_to_SB26,
            amount_to_SB26 = amount_to_SB26,
            blank_receipt_SB26 =blank_receipt_SB26,


            acquittance_comments=acquittance_comments,
            unused_receipts_comments=unused_receipts_comments,
            reference_number_comments=reference_number_comments,

            book_no_SB28=book_no_SB28,
            receipt_no_from_SB28 =receipt_no_from_SB28,
            date_from_SB28 = date_from_SB28,
            amount_from_SB28 = amount_from_SB28,
            receipt_no_to_SB28 = receipt_no_to_SB28,
            date_to_SB28 =date_to_SB28,
            amount_to_SB28 = amount_to_SB28,
            blank_receipt_SB28 =blank_receipt_SB28,



            book_no_MS87=book_no_MS87,
            receipt_no_from_MS87 =receipt_no_from_MS87,
            date_from_MS87 = date_from_MS87,
            amount_from_MS87 = amount_from_MS87,
            receipt_no_to_MS87 = receipt_no_to_MS87,
            date_to_MS87 =date_to_MS87,
            amount_to_MS87 = amount_to_MS87,
            blank_receipt_MS87 =blank_receipt_MS87,
            
            # account_no =account_no,
            # scheme_type = scheme_type,
            # last_transaction_date =last_transaction_date,
            # deposit = deposit,
            # withdrawal = withdrawal,
            # balance = balance,
            # sms_alert = sms_alert,
            # system_receipt = system_receipt,
            # new_passbook_entry = new_passbook_entry,




            discrepancy_comments =discrepancy_comments,
            passbook_verified = passbook_verified,
            passbook_verified_comments = passbook_verified_comments,


            account_details_1 = account_details_1,
            account_details_2 = account_details_2,
            account_details_3 =account_details_3,
            account_details_4 = account_details_4,
            account_details_5 = account_details_5,




            authorization_forms_available = authorization_forms_available,
            authorization_forms_comments = authorization_forms_comments,
            inventory_levels_maintained =inventory_levels_maintained,
            inventory_comments =inventory_comments,
            doorstep_service_requests = doorstep_service_requests,
            doorstep_service_comments = doorstep_service_comments,
            applications_received = applications_received,
            applications_received_comments = applications_received_comments,
            help_desk_maintained = help_desk_maintained,
            help_desk_comments =help_desk_comments,
            qr_displayed = qr_displayed,
            qr_comments = qr_comments,

            pli_rpli_policy_number_1 =pli_rpli_policy_number_1,
            dlt_1 = dlt_1,
            account_number_1 = account_number_1,
            pli_rpli_transactions_type_1 = pli_rpli_transactions_type_1,

            pli_rpli_policy_number_2 = pli_rpli_policy_number_2,
            dlt_2 =dlt_2,
            account_number_2 = account_number_2,
            pli_rpli_transactions_type_2 = pli_rpli_transactions_type_2,
            pli_rpli_proposals = pli_rpli_proposals,
            dispatched_to_account_office = dispatched_to_account_office,

            pli_rpli_publicity_material = pli_rpli_publicity_material,
            pli_rpli_publicity_comments = pli_rpli_publicity_comments,


            feedback_comments = feedback_comments,






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



def home(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('submit_form')
        else:
            messages.error(request,'Invalid username or password!')
            return render(request,"index.html")
        
    else:
        return render(request,"index.html")

