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

patient.total_bilirubin = 8.5
patient.direct_bilirubin = 5.6

patient.ast = 950
patient.alt = 1100
patient.alp = 140

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
