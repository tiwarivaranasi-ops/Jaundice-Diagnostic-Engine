from diagnosis import Diagnosis
from patient import Patient
from classifier import Classifier
from finding_manager import FindingManager

# Create a patient
patient = Patient()

# ----------------------------
# Enter patient data
# ----------------------------

patient.age = 25
patient.sex = "Male"

patient.total_bilirubin = 8.0
patient.direct_bilirubin = 4.0

patient.ast = 500
patient.alt = 500
patient.alp = 500

patient.prodromal_symptoms = True
patient.alcohol_history = True
patient.pruritus = True
patient.dark_urine = True
patient.pale_stools = True

# ----------------------------
# Run the classifier
# ----------------------------

classifier = Classifier()
classifier.classify(patient)
diagnosis = Diagnosis()
diagnosis.diagnose(patient)

# ----------------------------
# Display findings
# ----------------------------

FindingManager.display(patient)

print("\n===== PROVISIONAL DIAGNOSIS =====")
print(patient.provisional_diagnosis)
