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

patient.total_bilirubin = 12.0
patient.direct_bilirubin = 8.0

patient.ast = 120
patient.alt = 140
patient.alp = 900

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
