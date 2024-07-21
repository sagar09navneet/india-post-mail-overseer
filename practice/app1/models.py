from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class BranchOffice(models.Model):

   #   user = models.ForeignKey(User, on_delete=models.CASCADE)
   #   filled_at = models.DateTimeField(default=timezone.now)

     branch_name = models.CharField(max_length=100, verbose_name='Name of the Branch Office (BO)')
     account_office_name = models.CharField(max_length=100, verbose_name='Name of the Account Office (AO)')
     head_office_name = models.CharField(max_length=100, verbose_name='Name of the Head Office')
     facility_id = models.IntegerField( verbose_name='Facility ID of the BO Profit/Cost centre ID of the BO')
     establishment = models.DateField( verbose_name='Establishment of the BO')
     last_inspection = models.DateField(verbose_name='Date of Last Inspection (DLI) and by whom')
     subsequent_visits = models.DateField(verbose_name='Date of subsequent visits by Mail Overseer since DLI' )



     previous_inspection_pending = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     previous_inspection_comments = models.TextField()

     work_carried_out = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     work_carried_out_comments = models.TextField()

     bo_signage = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     signage_comments = models.TextField()

     look_and_feel = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     look_and_feel_comments = models.TextField()

     articles_in_deposit_comments_acc = models.TextField(verbose_name='No. of articles in deposit' , default='adn')
     articles_beyond_period_acc = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     articles_beyond_period_comments_acc = models.TextField(verbose_name='Comments on articles beyond prescribed period' , default='adn')
     article_condition_acc =  models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     article_condition_comments_acc = models.TextField(verbose_name='Comments on article condition' , default='adn')
     compare_articles_comments_acc = models.TextField(verbose_name='Compare the number of articles in deposit comments' , default='adn')

     articles_in_deposit_comments_ord = models.TextField(verbose_name='No. of articles in deposit' , default='adn')
     articles_beyond_period_ord = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     articles_beyond_period_comments_ord = models.TextField(verbose_name='Comments on articles beyond prescribed period' , default='adn')
     article_condition_ord =  models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     article_condition_comments_ord = models.TextField(verbose_name='Comments on article condition' , default='adn')
     compare_articles_comments_ord = models.TextField(verbose_name='Compare the number of articles in deposit comments' , default='adn')

     check_delivery_status_acc = models.JSONField(blank=True, null=True, default=dict)
     check_delivery_status_comments_acc = models.JSONField(verbose_name='Comments on delivery status', blank=True, null=True, default=dict)
     date_of_receipt_acc = models.JSONField(verbose_name='Date of receipt', blank=True, null=True, default=dict)
     date_of_delivery_acc = models.JSONField(verbose_name='Date of delivery', blank=True, null=True, default=dict)

     check_delivery_status_ord = models.JSONField(blank=True, null=True, default=dict)
     check_delivery_status_comments_ord = models.JSONField(verbose_name='Comments on delivery status', blank=True, null=True, default=dict)
     date_of_receipt_ord = models.JSONField(verbose_name='Date of receipt', blank=True, null=True, default=dict)
     date_of_delivery_ord = models.JSONField(verbose_name='Date of delivery', blank=True, null=True, default=dict) 


     no_of_letter_boxes = models.IntegerField(verbose_name='Apart from the office letter box, how many letter boxes are attached to the BO?')
     lb_condition = models.CharField(verbose_name='Whether LBs painted and in good condition?',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     lb_condition_comments = models.TextField(verbose_name='Comments on LB condition')
     lb_clearance = models.CharField(verbose_name='Are LBs cleared punctually? Are timings of clearance suitable?',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     lb_clearance_comments = models.TextField(verbose_name='Comments on LB clearance')


     last_acknowledged_balance = models.FloatField(verbose_name='Last acknowledged BO balance by Account Office through BO slip or DTR.')
     last_acknowledged_balance_date = models.DateField(verbose_name='Date of last acknowledged balance')
     last_acknowledged_balance_comments = models.TextField(verbose_name='Comments on last acknowledged balance')
     cash_value = models.FloatField(verbose_name='Cash value')
     stamp_value = models.FloatField(verbose_name='Stamp value')
     details_in_stock_comments = models.TextField(verbose_name='Comments on details of cash, stamp, forms in stock')
     cash_balance_correct = models.CharField(verbose_name='Whether cash balance is correct?',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     cash_balance_comments = models.TextField(verbose_name='Comments on cash balance')
     wallet_balance = models.FloatField(verbose_name='Wallet balance')
     wallet_balance_date = models.DateField(verbose_name='Date of wallet balance')
     physical_balance = models.FloatField(verbose_name='Physical balance')
     physical_balance_date = models.DateField(verbose_name='Date of physical balance')

     invoice_stamp = models.JSONField(verbose_name='Stamp received through CSI and duly acknowledged? Check invoices received and whether inventory updated.', blank=True, null=True, default=dict)     
     inventory = models.JSONField(verbose_name='Comments on inventory', blank=True, null=True, default=dict) 
     
     postage_due = models.CharField(verbose_name='Examine the Postage Due and amount realized towards unpaid articles and record results.',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     postage_due_comments = models.TextField(verbose_name='Comments on postage due')
     

     date_of_account = models.JSONField(verbose_name='Date of BO account', blank=True, null=True, default=dict)
     bo_slip = models.JSONField(verbose_name='BO SLIP', blank=True, null=True, default=dict)
     bo_account = models.JSONField(verbose_name='BO ACCOUNT', blank=True, null=True, default=dict)
     question_9 = models.TextField(verbose_name='Examine the BO Accounts since the last visit to see that the BPM has not unnecessarily retained excess cash. Examine whether the arrangements for exchange of cash with the Account Office are satisfactory and record instances of delay in payment of Money Orders, Savings Bank withdrawals etc. for want of funds. Whether the norms for remittances have been followed as mentioned in the Directorate letter No.24- 3/2012/PO dated 01/10/2018. Educate the BPM on the procedure to be followed if the amount exceeds the prescribed limit.', blank=True, null=True, default=dict)


     number_of_mo_issued = models.IntegerField(verbose_name='No of MO issued since last visit')
     number_of_mo_received = models.IntegerField(verbose_name='No. of MOs received for payment and whether paid promptly. Check promptness with atleast 5 payees. (Mention MO and payee details)')
     payee_details1 = models.CharField(max_length=100, verbose_name='Payee details 1')
     payee_details2 = models.CharField(max_length=100, verbose_name='Payee details 2')
     payee_details3 = models.CharField(max_length=100, verbose_name='Payee details 3')
     payee_details4 = models.CharField(max_length=100, verbose_name='Payee details 4')
     payee_details5 = models.CharField(max_length=100, verbose_name='Payee details 5')

     article_number = models.JSONField(verbose_name='No. of VP/COD articles delivered (one day in each month since DLI/DLV)(Article No)', blank=True, null=True, default=dict)
     article_issued_date = models.JSONField(verbose_name='Article Issued DATE')
     article_received_date = models.JSONField(verbose_name='Article received DATE', blank=True, null=True, default=dict)
     article_delivered_date = models.JSONField(verbose_name='Article Delivered DATE', blank=True, null=True, default=dict)
     VPMO_issued_date = models.JSONField(verbose_name='VPMO isssued DATE', blank=True, null=True, default=dict)
     VPMO_issued_comments = models.JSONField(verbose_name='Whether VPMO issued immediately?', blank=True, null=True, default=dict)

     demurrage_fees_comments = models.TextField(verbose_name='Comments on whether demurrage fees charged and noted in VP receipt (RP- 55)',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     list_of_mo_received = models.CharField(verbose_name='Whether List of MO received for payment is pasted in BO journal and those issued to ABPM (MD) is pasted in Postman Book. Check the same for other accountable articles.',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     list_of_mo_received_comments = models.TextField(verbose_name='Comments on List of MO received for payment')
     eMO_payment_limit = models.CharField(verbose_name='Test check whether the BPM has given the cash to ABPM (MD) for eMO payment beyond the prescribed limit as mentioned in Directorate letter No.24-3/2012-PO dated 01.10. 2018. Educate the BPM on the procedure to be followed if the amount exceeds the prescribed limit.',max_length=3, choices=[("Yes", "Yes"), ("No", "No")], blank=True, null=True , default='adn')
     eMO_payment_limit_comments = models.TextField(verbose_name='Comments on eMO payment limit')



     BO_journals = models.CharField(max_length=3, choices=(('Yes', 'Yes'), ('No', 'No')), verbose_name='Whether BO journals and Specimen Signature Book of all POSB Schemes maintained and updated with complete KYC')
     BO_journals_comments = models.TextField(verbose_name='Comments on BO journals')
     entries_comparison = models.CharField(max_length=3, choices=(('Yes', 'Yes'), ('No', 'No')), verbose_name='Compare the entries made in SB/RD/TD/SSA journals with the corresponding entries made in BO account book')
     entries_comparison_comments = models.TextField(verbose_name='Comments on entries comparison')
     cheques_received = models.CharField(max_length=3, choices=(('Yes', 'Yes'), ('No', 'No')), verbose_name='Whether cheques received in BO entered in cheque register and submitted to account office')
     cheques_received_comments = models.TextField(verbose_name='Comments on cheques received')
     passbook_collection_register = models.CharField(max_length=3, choices=(('Yes', 'Yes'), ('No', 'No')), verbose_name='Check that register for collection of passbooks of SB/PPF/SSA is maintained in Branch Post Office')
     passbook_collection_register_comments = models.TextField(verbose_name='Comments on passbook collection register')
     number_of_passbooks_deposit = models.IntegerField(verbose_name='Number of passbooks in deposit')
     number_of_passbooks_deposit_comments = models.TextField(verbose_name='Comments on number of passbooks in deposit')



     account_number_ao = models.JSONField(verbose_name='Account number for annual interest posting', blank=True, null=True, default=dict)
     all_schemes = models.JSONField(verbose_name='All schemes for annual interest posting', blank=True, null=True, default=dict)




     book_no_SB26= models.JSONField(verbose_name='Book No_SB26', blank=True, null=True, default=dict)
     receipt_no_from_SB26 = models.JSONField(verbose_name='Receipt No (From)_SB26', blank=True, null=True, default=dict)
     date_from_SB26 = models.JSONField(verbose_name='Date (From)_SB26', blank=True, null=True, default=dict)
     amount_from_SB26 = models.JSONField(verbose_name='Amount (From)_SB26', blank=True, null=True, default=dict)
     receipt_no_to_SB26 = models.JSONField(verbose_name='Receipt No (To)_SB26', blank=True, null=True, default=dict)
     date_to_SB26 = models.JSONField(verbose_name='Date (To)_SB26', blank=True, null=True, default=dict)
     amount_to_SB26 = models.JSONField(verbose_name='Amount (To)_SB26', blank=True, null=True, default=dict)
     blank_receipt_SB26 = models.JSONField(verbose_name='Blank Receipt_SB26', blank=True, null=True, default=dict)


     acquittance_comments = models.TextField(verbose_name='acquittance comments')
     unused_receipts_comments = models.TextField(verbose_name='unused receipts comments')
     reference_number_comments = models.TextField(verbose_name='reference number comments')



     book_no_SB28 = models.JSONField(verbose_name='Book No_SB28', blank=True, null=True, default=dict)
     receipt_no_from_SB28 = models.JSONField(verbose_name='Receipt No (From)_SB28', blank=True, null=True, default=dict)
     date_from_SB28 = models.JSONField(verbose_name='Date (From)_SB28', blank=True, null=True, default=dict)
     amount_from_SB28 = models.JSONField(verbose_name='Amount (From)_SB28', blank=True, null=True, default=dict)
     receipt_no_to_SB28 = models.JSONField(verbose_name='Receipt No (To)_SB28', blank=True, null=True, default=dict)
     date_to_SB28 = models.JSONField(verbose_name='Date (To)_SB28', blank=True, null=True, default=dict)
     amount_to_SB28 = models.JSONField(verbose_name='Amount (To)_SB28', blank=True, null=True, default=dict)
     blank_receipt_SB28 = models.JSONField(verbose_name='Blank Receipt_SB28', blank=True, null=True, default=dict)


     book_no_MS87= models.JSONField(verbose_name='Book No_MS87', blank=True, null=True, default=dict)
     receipt_no_from_MS87 = models.JSONField(verbose_name='Receipt No (From)_MS87', blank=True, null=True, default=dict)
     date_from_MS87 = models.JSONField(verbose_name='Date (From)_MS87', blank=True, null=True, default=dict)
     amount_from_MS87 = models.JSONField(verbose_name='Amount (From)_MS87', blank=True, null=True, default=dict)
     receipt_no_to_MS87 = models.JSONField(verbose_name='Receipt No (To)_MS87', blank=True, null=True, default=dict)
     date_to_MS87 = models.JSONField(verbose_name='Date (To)_MS87', blank=True, null=True, default=dict)
     amount_to_MS87 = models.JSONField(verbose_name='Amount (To)_MS87', blank=True, null=True, default=dict)
     blank_receipt_MS87 = models.JSONField(verbose_name='Blank Receipt_MS87', blank=True, null=True, default=dict)



 
     account_no_1 = models.JSONField(verbose_name='Account No.', blank=True, null=True, default=dict)
     scheme_type_1 = models.JSONField(verbose_name='Scheme Type', blank=True, null=True, default=dict)
     last_transaction_date_1 = models.JSONField(verbose_name='Date of Last Transaction', blank=True, null=True, default=dict)
     deposit_1 = models.JSONField(verbose_name='Deposit', blank=True, null=True, default=dict)
     withdrawal_1 = models.JSONField(verbose_name='Withdrawal', blank=True, null=True, default=dict)
     balance_1 = models.JSONField(verbose_name='Balance', blank=True, null=True, default=dict)
     sms_alert_1 = models.JSONField(verbose_name='SMS Alert (Y/N)', blank=True, null=True, default=dict)
     system_receipt_1 = models.JSONField(verbose_name='System Generated Receipt Provided', blank=True, null=True, default=dict)
     new_passbook_entry_1 = models.JSONField(verbose_name='1st Page Entry of New Passbook (Y/N)', blank=True, null=True, default=dict)
     
     account_no_2 = models.JSONField(verbose_name='Account No.', blank=True, null=True, default=dict)
     scheme_type_2 = models.JSONField(verbose_name='Scheme Type', blank=True, null=True, default=dict)
     last_transaction_date_2 = models.JSONField(verbose_name='Date of Last Transaction', blank=True, null=True, default=dict)
     deposit_2 = models.JSONField(verbose_name='Deposit', blank=True, null=True, default=dict)
     withdrawal_2 = models.JSONField(verbose_name='Withdrawal', blank=True, null=True, default=dict)
     balance_2 = models.JSONField(verbose_name='Balance', blank=True, null=True, default=dict)
     sms_alert_2 = models.JSONField(verbose_name='SMS Alert (Y/N)', blank=True, null=True, default=dict)
     system_receipt_2 = models.JSONField(verbose_name='System Generated Receipt Provided', blank=True, null=True, default=dict)
     new_passbook_entry_2 = models.JSONField(verbose_name='1st Page Entry of New Passbook (Y/N)', blank=True, null=True, default=dict)

     account_no_3 = models.JSONField(verbose_name='Account No.', blank=True, null=True, default=dict)
     scheme_type_3 = models.JSONField(verbose_name='Scheme Type', blank=True, null=True, default=dict)
     last_transaction_date_3 = models.JSONField(verbose_name='Date of Last Transaction', blank=True, null=True, default=dict)
     deposit_3 = models.JSONField(verbose_name='Deposit', blank=True, null=True, default=dict)
     withdrawal_3 = models.JSONField(verbose_name='Withdrawal', blank=True, null=True, default=dict)
     balance_3 = models.JSONField(verbose_name='Balance', blank=True, null=True, default=dict)
     sms_alert_3 = models.JSONField(verbose_name='SMS Alert (Y/N)', blank=True, null=True, default=dict)
     system_receipt_3 = models.JSONField(verbose_name='System Generated Receipt Provided', blank=True, null=True, default=dict)
     new_passbook_entry_3 = models.JSONField(verbose_name='1st Page Entry of New Passbook (Y/N)', blank=True, null=True, default=dict)

     discrepancy_comments = models.TextField(verbose_name='Discrepancy Comments')
     passbook_verified = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], verbose_name='Passbook Verified')
     passbook_verified_comments = models.TextField(verbose_name='Passbook Verified Comments')


     account_details_1 = models.CharField(max_length=100, verbose_name='Account Details 1')
     account_details_2 = models.CharField(max_length=100, verbose_name='Account Details 2')
     account_details_3 = models.CharField(max_length=100, verbose_name='Account Details 3')
     account_details_4 = models.CharField(max_length=100, verbose_name='Account Details 4')
     account_details_5 = models.CharField(max_length=100, verbose_name='Account Details 5')







     authorization_forms_available = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     authorization_forms_comments = models.TextField()
     inventory_levels_maintained = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     inventory_comments = models.TextField()
     doorstep_service_requests = models.IntegerField()
     doorstep_service_comments = models.TextField()
     applications_received = models.IntegerField()
     applications_received_comments = models.TextField()
     help_desk_maintained = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     help_desk_comments = models.TextField()
     qr_displayed = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     qr_comments = models.TextField()

     pli_rpli_policy_number_1 = models.IntegerField()
     dlt_1 = models.IntegerField()
     account_number_1 = models.IntegerField()
     pli_rpli_transactions_type_1 = models.CharField(max_length=4, choices=[("PLI", "PLI"), ("RPLI", "RPLI")])

     pli_rpli_policy_number_2 = models.IntegerField()
     dlt_2 = models.IntegerField()
     account_number_2 = models.IntegerField()
     pli_rpli_proposals = models.IntegerField()
     pli_rpli_transactions_type_2 = models.CharField(max_length=4, choices=[("PLI", "PLI"), ("RPLI", "RPLI")])
     pli_rpli_proposal_type_2 = models.CharField(max_length=4, choices=[("PLI", "PLI"), ("RPLI", "RPLI")])
     dispatched_to_account_office = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])

     pli_rpli_publicity_material = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
     pli_rpli_publicity_comments = models.TextField()


     feedback_comments = models.TextField()
     
     def __str__(self):
        return f"{self.user.username} - {self.filled_at}"