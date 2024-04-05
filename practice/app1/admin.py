from django.contrib import admin
from .models import BranchOffice, InspectionReport, WorkCarriedOut, Signage, LookAndFeel, MailOperations, \
    LetterBoxes, FinanceAndAccounting, MoneyOrder, SavingsBank, PassbookStatus, SB26, SB28, MS87, Acquittance, \
    UnusedReceipts, ReferenceNumber, PassbookVerification, PassbookVerificationLog, SSAAccount, \
    IndiaPostPaymentBank, PostalLifeInsurance, Conclusion



admin.site.register(BranchOffice)
admin.site.register(InspectionReport)
admin.site.register(WorkCarriedOut)
admin.site.register(Signage)
admin.site.register(LookAndFeel)
admin.site.register(MailOperations)
admin.site.register(LetterBoxes)
admin.site.register(FinanceAndAccounting)
admin.site.register(MoneyOrder)
admin.site.register(SavingsBank)
admin.site.register(PassbookStatus)
admin.site.register(SB26)
admin.site.register(SB28)
admin.site.register(MS87)
admin.site.register(Acquittance)
admin.site.register(UnusedReceipts)
admin.site.register(ReferenceNumber)
admin.site.register(PassbookVerification)
admin.site.register(PassbookVerificationLog)
admin.site.register(SSAAccount)
admin.site.register(IndiaPostPaymentBank)
admin.site.register(PostalLifeInsurance)
admin.site.register(Conclusion)
