from django import forms
from .models import Conclusion




# class BranchOfficeForm(forms.ModelForm):
#     establishment = forms.DateField(
#         widget=forms.DateInput(format='%d%m%Y'),
#         input_formats=['%d%m%Y']
#     )
#     last_inspection = forms.DateField(
#         widget=forms.DateInput(format='%d%m%Y'),
#         input_formats=['%d%m%Y']
#     )
#     subsequent_visits = forms.DateField(
#         widget=forms.DateInput(format='%d%m%Y'),
#         input_formats=['%d%m%Y']
#     )

#     class Meta:
#         model = BranchOffice
#         fields = '__all__'


# class InspectionReportForm(forms.ModelForm):
#     class Meta:
#         model = InspectionReport
#         fields = '__all__'

# class WorkCarriedOutForm(forms.ModelForm):
#     class Meta:
#         model = WorkCarriedOut
#         fields = '__all__'

# class SignageForm(forms.ModelForm):
#     class Meta:
#         model = Signage
#         fields = '__all__'

# class LookAndFeelForm(forms.ModelForm):
#     class Meta:
#         model = LookAndFeel
#         fields = '__all__'

# class MailOperationsForm(forms.ModelForm):
#     class Meta:
#         model = MailOperations
#         fields = '__all__'

# class LetterBoxesForm(forms.ModelForm):
#     class Meta:
#         model = LetterBoxes
#         fields = '__all__'

# class FinanceAndAccountingForm(forms.ModelForm):
#     class Meta:
#         model = FinanceAndAccounting
#         fields = '__all__'
# class MoneyOrderForm(forms.ModelForm):
#     class Meta:
#         model = MoneyOrder
#         fields = '__all__'
# class  SavingsBankForm(forms.ModelForm):
#     class Meta:
#         model = SavingsBank
#         fields = '__all__'                
# class  PassbookStatusForm(forms.ModelForm):
#     class Meta:
#         model = PassbookStatus
#         fields = '__all__'                
# class SB26Form(forms.ModelForm):
#     class Meta:
#         model = SB26
#         fields = '__all__'                
# class SB28Form(forms.ModelForm):
#     class Meta:
#         model = SB28
#         fields = '__all__'                
# class  MS87Form(forms.ModelForm):
#     class Meta:
#         model = MS87
#         fields = '__all__'                

# class  AcquittanceForm(forms.ModelForm):
#     class Meta:
#         model = Acquittance
#         fields = '__all__'                
# class  UnusedReceiptsForm(forms.ModelForm):
#     class Meta:
#         model = UnusedReceipts
#         fields = '__all__'                

# class ReferenceNumberForm(forms.ModelForm):
#     class Meta:
#         model = ReferenceNumber
#         fields = '__all__'                

# class  PassbookVerificationForm(forms.ModelForm):
#     class Meta:
#         model = PassbookVerification
#         fields = '__all__'                

# class  PassbookVerificationLogForm(forms.ModelForm):
#     class Meta:
#         model = PassbookVerificationLog
#         fields = '__all__'  
# class SSAAccountForm(forms.ModelForm):
#     class Meta:
#         model = SSAAccount
#         fields = ['account_details']              

# class IndiaPostPaymentBankForm(forms.ModelForm):
#     class Meta:
#         model = IndiaPostPaymentBank
#         fields = '__all__'                

# class  PostalLifeInsuranceForm(forms.ModelForm):
#     class Meta:
#         model = PostalLifeInsurance
#         fields = '__all__'                

class  ConclusionForm(forms.ModelForm):
    class Meta:
        model = Conclusion
        fields = ['feedback_comments']                