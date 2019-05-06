from django import forms
from django.contrib import messages

class predictionForm(forms.Form):
    NORM_recoveries = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Recovery'}))
    NORM_last_pymnt_amnt = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'last payment'}))
    NORM_int_rate = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'interest rate'}))
    NORM_loan_amnt = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'loan amount'}))
    NORM_dti = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'debt to income'}))
    NORM_total_rec_late_fee  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'late fees recieved'}))
    NORM_num_actv_rev_tl = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'active revolving trades'}))
    NORM_total_rec_int = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total received interest'}))
    NORM_revol_util = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Revolving line utilization rate'}))
    NORM_installment  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monthly installment'}))
    NORM_earliest_credit_line   = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Month of earliest credit line '}))
    NORM_total_pymnt = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Payment Received'}))
    NORM_total_rec_late_fee = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Last Payment amount'}))
    NORM_pct_tl_nvr_dlq  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '% of trades never delinquent'}))
    NORM_total_pumnt_inv   = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'amnt for portion funded by investors'}))
    NORM_open_acc    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'open credit lines'}))
    NORM_mths_since_recent_inq  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Months since latest inq.'}))
    NORM_mo_sin_old_il_acct  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Months since oldest installment account opened'}))
    NORM_total_acc  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of credit lines'}))
    NORM_mort_acc   = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of mortgage accounts'}))
    NORM_funded_amnt_inv    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total amount committed by investors'}))
    mths_since_recent_revol_delinq  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mnths since latest rev. delinq.'}))
    NORM_delinq2Yrs  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of 30+ days incidents of delinquency in last 2 years.'}))
    NORM_annual_inc  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Annual Income'}))
    NORM_mo_sin_old_rev_tl_op = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mnth since oldest revolving account'}))
    NORM_last_pymnt_d = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Last month payment was received'}))
    issue_d = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'month of funding'}))
    NORM_bc_util  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'bal/credit limit ratio'}))
    NORM_num_rev_accts  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of revolving accounts'}))
    term = forms.ChoiceField((('0','36'), ('1','60')), widget=forms.Select(attrs = {'class': 'form-control'}))
    mths_since_last_delinq = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Months since delinq.'}))
    mths_since_last_record  = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'mnth. since last public record'}))
    mths_since_recent_bc_dlq   = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mnth. since bankcard delinq.'}))
    NORM_pct_tl_nvr_dlq    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '% of trades never delinquent'}))
    NORM_acc_open_past_24mths    = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'trades opened past 24 months'}))

    # def form_invalid(self, form):
    #     response = super(predictionForm, self).form_valid(form)
    #     messages.info(request, "invalid")
    #     return response


    # def form_valid(self, form):
    #  	response = super(predictionForm, self).form_valid(form)
    #  	messages.info(request, "submitted")
    #  	return response

	
