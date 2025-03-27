import joblib
import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Prediction

# Load the trained RandomForest model
model_path = model_path = "A:\\AI-Disease-Prediction\\disease_prediction\\predictor\\random_forest.pkl"
 # Replace with actual path
rf_model = joblib.load(model_path)

# Define symptom-to-index mapping (must match what the model expects)
symptom_index = {
    "fever": 0, "cough": 1, "fatigue": 2, "headache": 3, "nausea": 4,
    "dizziness": 5, "sore_throat": 6, "body_pain": 7, "runny_nose": 8
}

def predict_view(request):
    if request.method == "POST":
        symptom1 = request.POST.get("Symptom_1", "")
        symptom2 = request.POST.get("Symptom_2", "")
        symptom3 = request.POST.get("Symptom_3", "")

        if not all([symptom1, symptom2, symptom3]):
            return JsonResponse({"error": "Please select all three symptoms."})

        # Convert symptoms to model input format (e.g., numerical encoding)
        symptoms_vector = [0] * len(symptom_index)
        symptoms_vector[symptom_index[symptom1]] = 1
        symptoms_vector[symptom_index[symptom2]] = 1
        symptoms_vector[symptom_index[symptom3]] = 1

        # Predict the disease
        predicted_disease = rf_model.predict([symptoms_vector])[0]

        # Save prediction to database
        Prediction.objects.create(symptoms=f"{symptom1}, {symptom2}, {symptom3}", predicted_disease=predicted_disease)

        return JsonResponse({"disease": predicted_disease})

    return render(request, "predict.html")

from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    user_predictions = Prediction.objects.filter(user=request.user)
    return render(request, "patientdashboard.html", {"predictions": user_predictions})
