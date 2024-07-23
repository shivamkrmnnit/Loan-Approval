from django.shortcuts import render, HttpResponse
import pickle

model_file_path = 'static/model.pkl'
with open(model_file_path, 'rb') as f:
    model = pickle.load(f)

def home(request):
    if request.method == "POST":
        no_of_dependents = int(request.POST.get('no_of_dependents'))
        education = int(request.POST['education'])
        self_employed = int(request.POST['self_employed'])
        income_annum = int(request.POST['income_annum'])
        loan_amount = int(request.POST['loan_amount'])
        loan_term = int(request.POST['loan_term'])
        cibil_score = int(request.POST['cibil_score'])
        residential_assets_value = int(request.POST['residential_assets_value'])
        commercial_assets_value = int(request.POST['commercial_assets_value'])
        luxury_assets_value = int(request.POST['luxury_assets_value'])
        bank_asset_value = int(request.POST['bank_asset_value'])

        #print(no_of_dependents, education, self_employed, income_annum)
        pred = model.predict([[no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value]])[0]
        if pred == 0:
            prediction = "Approved"
        else:
            prediction = "Rejected"
        output = {
            "output" : prediction
        }

        return render(request, "index.html", output)

    else:
        return render(request, "index.html")
