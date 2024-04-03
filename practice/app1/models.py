from django.db import models
from django import forms

# Create your models here.


class BranchOffice(models.Model):
    branch_name = models.CharField(max_length=100, verbose_name='Name of the Branch Office (BO)')
    account_office_name = models.CharField(max_length=100, verbose_name='Name of the Account Office (AO)')
    head_office_name = models.CharField(max_length=100, verbose_name='Name of the Head Office')
    facility_id = models.CharField(max_length=100, verbose_name='Facility ID of the BO Profit/Cost centre ID of the BO')
    establishment = models.CharField(max_length=100, verbose_name='Establishment of the BO')
    last_inspection = models.DateField(verbose_name='Date of Last Inspection (DLI) and by whom')
    subsequent_visits = models.DateField(verbose_name='Date of subsequent visits by Mail Overseer since DLI')
 


class InspectionReport(models.Model):
    previous_inspection_pending = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    previous_inspection_comments = models.TextField()

class WorkCarriedOut(models.Model):
    work_carried_out = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    work_carried_out_comments = models.TextField()

class Signage(models.Model):
    bo_signage = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    signage_comments = models.TextField()

class LookAndFeel(models.Model):
    look_and_feel = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    look_and_feel_comments = models.TextField()


class MailOperations(models.Model):
    articles_in_deposit_comments = models.TextField(verbose_name='No. of articles in deposit')
    articles_beyond_period = models.BooleanField(verbose_name='Whether articles beyond prescribed period')
    articles_beyond_period_comments = models.TextField(verbose_name='Comments on articles beyond prescribed period')
    article_condition = models.BooleanField(verbose_name='Whether article in deposit in good condition')
    article_condition_comments = models.TextField(verbose_name='Comments on article condition')
    compare_articles_comments = models.TextField(verbose_name='Compare the number of articles in deposit comments')
    check_delivery_status = models.BooleanField(verbose_name='Check delivery status')
    check_delivery_status_comments = models.TextField(verbose_name='Comments on delivery status')
    date_of_receipt = models.DateField(verbose_name='Date of receipt')
    date_of_delivery = models.DateField(verbose_name='Date of delivery')
class LetterBoxes(models.Model):
    no_of_letter_boxes = models.IntegerField(verbose_name='Apart from the office letter box, how many letter boxes are attached to the BO?')
    lb_condition = models.BooleanField(verbose_name='Whether LBs painted and in good condition?')
    lb_condition_comments = models.TextField(verbose_name='Comments on LB condition')
    lb_clearance = models.BooleanField(verbose_name='Are LBs cleared punctually? Are timings of clearance suitable?')
    lb_clearance_comments = models.TextField(verbose_name='Comments on LB clearance')

class FinanceAndAccounting(models.Model):
    last_acknowledged_balance = models.FloatField(verbose_name='Last acknowledged BO balance by Account Office through BO slip or DTR.')
    last_acknowledged_balance_date = models.DateField(verbose_name='Date of last acknowledged balance')
    last_acknowledged_balance_comments = models.TextField(verbose_name='Comments on last acknowledged balance')
    cash_value = models.FloatField(verbose_name='Cash value')
    stamp_value = models.FloatField(verbose_name='Stamp value')
    details_in_stock_comments = models.TextField(verbose_name='Comments on details of cash, stamp, forms in stock')
    cash_balance_correct = models.BooleanField(verbose_name='Whether cash balance is correct?')
    cash_balance_comments = models.TextField(verbose_name='Comments on cash balance')
    wallet_balance = models.FloatField(verbose_name='Wallet balance')
    wallet_balance_date = models.DateField(verbose_name='Date of wallet balance')
    physical_balance = models.FloatField(verbose_name='Physical balance')
    physical_balance_date = models.DateField(verbose_name='Date of physical balance')
    invoice_stamp = models.CharField(max_length=100, verbose_name='Stamp received through CSI and duly acknowledged? Check invoices received and whether inventory updated.')
    inventory = models.TextField(verbose_name='Comments on inventory')
    postage_due = models.BooleanField(verbose_name='Examine the Postage Due and amount realized towards unpaid articles and record results.')
    postage_due_comments = models.TextField(verbose_name='Comments on postage due')
    date_of_account = models.DateField(verbose_name='Date of BO account')
    bo_slip = models.IntegerField(verbose_name='BO SLIP')
    bo_account = models.IntegerField(verbose_name='BO ACCOUNT')
    question_9 = models.TextField(verbose_name='Examine the BO Accounts since the last visit to see that the BPM has not unnecessarily retained excess cash. Examine whether the arrangements for exchange of cash with the Account Office are satisfactory and record instances of delay in payment of Money Orders, Savings Bank withdrawals etc. for want of funds. Whether the norms for remittances have been followed as mentioned in the Directorate letter No.24- 3/2012/PO dated 01/10/2018. Educate the BPM on the procedure to be followed if the amount exceeds the prescribed limit.')

class MoneyOrder(models.Model):
    number_of_mo_issued = models.IntegerField(verbose_name='No of MO issued since last visit')
    number_of_mo_received = models.IntegerField(verbose_name='No. of MOs received for payment and whether paid promptly. Check promptness with atleast 5 payees. (Mention MO and payee details)')
    payee_details1 = models.CharField(max_length=100, verbose_name='Payee details 1')
    payee_details2 = models.CharField(max_length=100, verbose_name='Payee details 2')
    payee_details3 = models.CharField(max_length=100, verbose_name='Payee details 3')
    payee_details4 = models.CharField(max_length=100, verbose_name='Payee details 4')
    payee_details5 = models.CharField(max_length=100, verbose_name='Payee details 5')
    article_number = models.IntegerField(verbose_name='No. of VP/COD articles delivered (one day in each month since DLI/DLV)')
    article_issued_date = models.DateField(verbose_name='Article Issued DATE')
    article_received_date = models.DateField(verbose_name='Article received DATE')
    article_delivered_date = models.DateField(verbose_name='Article Delivered DATE')
    VPMO_issued_date = models.DateField(verbose_name='VPMO isssued DATE')
    VPMO_issued_comments = models.BooleanField(verbose_name='Whether VPMO issued immediately?')
    demurrage_fees_comments = models.TextField(verbose_name='Comments on whether demurrage fees charged and noted in VP receipt (RP- 55)')
    list_of_mo_received = models.BooleanField(verbose_name='Whether List of MO received for payment is pasted in BO journal and those issued to ABPM (MD) is pasted in Postman Book. Check the same for other accountable articles.')
    list_of_mo_received_comments = models.TextField(verbose_name='Comments on List of MO received for payment')
    eMO_payment_limit = models.BooleanField(verbose_name='Test check whether the BPM has given the cash to ABPM (MD) for eMO payment beyond the prescribed limit as mentioned in Directorate letter No.24-3/2012-PO dated 01.10. 2018. Educate the BPM on the procedure to be followed if the amount exceeds the prescribed limit.')
    eMO_payment_limit_comments = models.TextField(verbose_name='Comments on eMO payment limit')


class SavingsBank(models.Model):
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

class PassbookStatus(models.Model):
    account_number_ao = models.IntegerField(verbose_name='Account number for annual interest posting')
    all_schemes = models.CharField(max_length=10, choices=(('scheme1', 'scheme1'), ('scheme2', 'scheme2')), verbose_name='All schemes for annual interest posting')


class SB26(models.Model):
    book_no = models.CharField(max_length=100, verbose_name='Book No')
    receipt_no_from = models.CharField(max_length=100, verbose_name='Receipt No (From)')
    date_from = models.DateField(verbose_name='Date (From)')
    amount_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (From)')
    receipt_no_to = models.CharField(max_length=100, verbose_name='Receipt No (To)')
    date_to = models.DateField(verbose_name='Date (To)')
    amount_to = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (To)')
    blank_receipt = models.CharField(max_length=100, verbose_name='Blank Receipt')

class SB28(models.Model):
    book_no = models.CharField(max_length=100, verbose_name='Book No')
    receipt_no_from = models.CharField(max_length=100, verbose_name='Receipt No (From)')
    date_from = models.DateField(verbose_name='Date (From)')
    amount_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (From)')
    receipt_no_to = models.CharField(max_length=100, verbose_name='Receipt No (To)')
    date_to = models.DateField(verbose_name='Date (To)')
    amount_to = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (To)')
    blank_receipt = models.CharField(max_length=100, verbose_name='Blank Receipt')

class MS87(models.Model):
    book_no = models.CharField(max_length=100, verbose_name='Book No')
    receipt_no_from = models.CharField(max_length=100, verbose_name='Receipt No (From)')
    date_from = models.DateField(verbose_name='Date (From)')
    amount_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (From)')
    receipt_no_to = models.CharField(max_length=100, verbose_name='Receipt No (To)')
    date_to = models.DateField(verbose_name='Date (To)')
    amount_to = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount (To)')
    blank_receipt = models.CharField(max_length=100, verbose_name='Blank Receipt')

class Acquittance(models.Model):
    comments = models.TextField(verbose_name='Comments')

class UnusedReceipts(models.Model):
    comments = models.TextField(verbose_name='Comments')

class ReferenceNumber(models.Model):
    comments = models.TextField(verbose_name='Comments')


class PassbookVerification(models.Model):
    sl_no = models.IntegerField(verbose_name='SL. No.')
    account_no = models.CharField(max_length=100, verbose_name='Account No.')
    scheme_type = models.CharField(max_length=100, verbose_name='Scheme Type')
    last_transaction_date = models.DateField(verbose_name='Date of Last Transaction')
    deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Deposit')
    withdrawal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Withdrawal')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Balance')
    sms_alert = models.CharField(max_length=100, verbose_name='SMS Alert (Y/N)')
    system_receipt = models.BooleanField(verbose_name='System Generated Receipt Provided')
    new_passbook_entry = models.BooleanField(verbose_name='1st Page Entry of New Passbook (Y/N)')

class PassbookVerificationLog(models.Model):
    discrepancy_comments = models.TextField(verbose_name='Discrepancy Comments')
    passbook_verified = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], verbose_name='Passbook Verified')
    passbook_verified_comments = models.TextField(verbose_name='Passbook Verified Comments')
class SSAAccount(models.Model):
    account_details = models.CharField(max_length=100, verbose_name='Account Details')






class IndiaPostPaymentBank(models.Model):
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

class PostalLifeInsurance(models.Model):
    pli_rpli_policy_number = models.IntegerField()
    dlt = models.IntegerField()
    account_number = models.IntegerField()
    pli_rpli_transactions_type = models.CharField(max_length=4, choices=[("PLI", "PLI"), ("RPLI", "RPLI")])
    pli_rpli_proposals = models.IntegerField()
    pli_rpli_proposal_type = models.CharField(max_length=4, choices=[("PLI", "PLI"), ("RPLI", "RPLI")])
    dispatched_to_account_office = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    pli_rpli_publicity_material = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    pli_rpli_publicity_comments = models.TextField()

class Conclusion(models.Model):
    feedback_comments = models.TextField()
