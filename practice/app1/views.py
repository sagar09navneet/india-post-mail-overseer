from django.shortcuts import render, redirect
from .forms import (
    BranchOfficeForm, InspectionReportForm, WorkCarriedOutForm, SignageForm,
    LookAndFeelForm, MailOperationsForm, LetterBoxesForm, FinanceAndAccountingForm,
    MoneyOrderForm, SavingsBankForm, PassbookStatusForm, SB26Form, SB28Form,
    MS87Form, AcquittanceForm, UnusedReceiptsForm, ReferenceNumberForm,
    PassbookVerificationForm, PassbookVerificationLogForm, SSAAccountForm,
    IndiaPostPaymentBankForm, PostalLifeInsuranceForm, ConclusionForm
)

def submit_form(request):
    if request.method == 'POST':
        branch_office_form = BranchOfficeForm(request.POST)
        inspection_report_form = InspectionReportForm(request.POST)
        work_carried_out_form = WorkCarriedOutForm(request.POST)
        signage_form = SignageForm(request.POST)
        look_and_feel_form = LookAndFeelForm(request.POST)
        mail_operations_form = MailOperationsForm(request.POST)
        letter_boxes_form = LetterBoxesForm(request.POST)
        finance_and_accounting_form = FinanceAndAccountingForm(request.POST)
        money_order_form = MoneyOrderForm(request.POST)
        savings_bank_form = SavingsBankForm(request.POST)
        passbook_status_form = PassbookStatusForm(request.POST)
        sb26_form = SB26Form(request.POST)
        sb28_form = SB28Form(request.POST)
        ms87_form = MS87Form(request.POST)
        acquittance_form = AcquittanceForm(request.POST)
        unused_receipts_form = UnusedReceiptsForm(request.POST)
        reference_number_form = ReferenceNumberForm(request.POST)
        passbook_verification_form = PassbookVerificationForm(request.POST)
        passbook_verification_log_form = PassbookVerificationLogForm(request.POST)
        ssa_account_form = SSAAccountForm(request.POST)
        india_post_payment_bank_form = IndiaPostPaymentBankForm(request.POST)
        postal_life_insurance_form = PostalLifeInsuranceForm(request.POST)
        conclusion_form = ConclusionForm(request.POST)

        if all([
            branch_office_form.is_valid(), inspection_report_form.is_valid(),
            work_carried_out_form.is_valid(), signage_form.is_valid(),
            look_and_feel_form.is_valid(), mail_operations_form.is_valid(),
            letter_boxes_form.is_valid(), finance_and_accounting_form.is_valid(),
            money_order_form.is_valid(), savings_bank_form.is_valid(),
            passbook_status_form.is_valid(), sb26_form.is_valid(),
            sb28_form.is_valid(), ms87_form.is_valid(), acquittance_form.is_valid(),
            unused_receipts_form.is_valid(), reference_number_form.is_valid(),
            passbook_verification_form.is_valid(), passbook_verification_log_form.is_valid(),
            ssa_account_form.is_valid(), india_post_payment_bank_form.is_valid(),
            postal_life_insurance_form.is_valid(), conclusion_form.is_valid()
        ]):
            branch_office = branch_office_form.save
            inspection_report = inspection_report_form.save
            work_carried_out = work_carried_out_form.save
            signage = signage_form.save
            look_and_feel = look_and_feel_form.save
            mail_operations = mail_operations_form.save
            letter_boxes = letter_boxes_form.save
            finance_and_accounting = finance_and_accounting_form.save
            money_order = money_order_form.save
            savings_bank = savings_bank_form.save
            passbook_status = passbook_status_form.save
            sb26 = sb26_form.save
            sb28 = sb28_form.save
            ms87 = ms87_form.save
            acquittance = acquittance_form.save
            unused_receipts = unused_receipts_form.save
            reference_number = reference_number_form.save
            passbook_verification = passbook_verification_form.save
            passbook_verification_log = passbook_verification_log_form.save
            ssa_account = ssa_account_form.save
            india_post_payment_bank = india_post_payment_bank_form.save
            postal_life_insurance = postal_life_insurance_form.save
            conclusion = conclusion_form.save

            # Save all objects in series
            branch_office.save()
            inspection_report.branch_office = branch_office
            inspection_report.save()
            work_carried_out.inspection_report = inspection_report
            work_carried_out.save()
            signage.work_carried_out = work_carried_out
            signage.save()
            look_and_feel.signage = signage
            look_and_feel.save()
            mail_operations.look_and_feel = look_and_feel
            mail_operations.save()
            letter_boxes.mail_operations = mail_operations
            letter_boxes.save()
            finance_and_accounting.letter_boxes = letter_boxes
            finance_and_accounting.save()
            money_order.finance_and_accounting = finance_and_accounting
            money_order.save()
            savings_bank.money_order = money_order
            savings_bank.save()
            passbook_status.savings_bank = savings_bank
            passbook_status.save()
            sb26.passbook_status = passbook_status
            sb26.save()
            sb28.sb26 = sb26
            sb28.save()
            ms87.sb28 = sb28
            ms87.save()
            acquittance.ms87 = ms87
            acquittance.save()
            unused_receipts.acquittance = acquittance
            unused_receipts.save()
            reference_number.unused_receipts = unused_receipts
            reference_number.save()
            passbook_verification.reference_number = reference_number
            passbook_verification.save()
            passbook_verification_log.passbook_verification = passbook_verification
            passbook_verification_log.save()
            ssa_account.passbook_verification_log = passbook_verification_log
            ssa_account.save()
            india_post_payment_bank.ssa_account = ssa_account
            india_post_payment_bank.save()
            postal_life_insurance.india_post_payment_bank = india_post_payment_bank
            postal_life_insurance.save()
            conclusion.postal_life_insurance = postal_life_insurance
            conclusion.save()
            
             

            # Repeat the process for other related objects

            return redirect('success_page')  # Redirect to success page upon successful form submission
    else:
        branch_office_form = BranchOfficeForm()
        inspection_report_form = InspectionReportForm()
        work_carried_out_form = WorkCarriedOutForm()
        signage_form = SignageForm()
        look_and_feel_form = LookAndFeelForm()
        mail_operations_form = MailOperationsForm()
        letter_boxes_form = LetterBoxesForm()
        finance_and_accounting_form = FinanceAndAccountingForm()
        money_order_form = MoneyOrderForm()
        savings_bank_form = SavingsBankForm()
        passbook_status_form = PassbookStatusForm()
        sb26_form = SB26Form()
        sb28_form = SB28Form()
        ms87_form = MS87Form()
        acquittance_form = AcquittanceForm()
        unused_receipts_form = UnusedReceiptsForm()
        reference_number_form = ReferenceNumberForm()
        passbook_verification_form = PassbookVerificationForm()
        passbook_verification_log_form = PassbookVerificationLogForm()
        ssa_account_form = SSAAccountForm()
        india_post_payment_bank_form = IndiaPostPaymentBankForm()
        postal_life_insurance_form = PostalLifeInsuranceForm()
        conclusion_form = ConclusionForm()

    return render(request, 'main1.html', {
        'branch_office_form': branch_office_form, 'inspection_report_form': inspection_report_form,
        'work_carried_out_form': work_carried_out_form, 'signage_form': signage_form,
        'look_and_feel_form': look_and_feel_form, 'mail_operations_form': mail_operations_form,
        'letter_boxes_form': letter_boxes_form, 'finance_and_accounting_form': finance_and_accounting_form,
        'money_order_form': money_order_form, 'savings_bank_form': savings_bank_form,
        'passbook_status_form': passbook_status_form, 'sb26_form': sb26_form,
        'sb28_form': sb28_form, 'ms87_form': ms87_form, 'acquittance_form': acquittance_form,
        'unused_receipts_form': unused_receipts_form, 'reference_number_form': reference_number_form,
        'passbook_verification_form': passbook_verification_form, 'passbook_verification_log_form': passbook_verification_log_form,
        'ssa_account_form': ssa_account_form, 'india_post_payment_bank_form': india_post_payment_bank_form,
        'postal_life_insurance_form': postal_life_insurance_form, 'conclusion_form': conclusion_form
    })
