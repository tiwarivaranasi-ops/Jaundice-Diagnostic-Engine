from diagnosis import Diagnosis
import diagnosis
print(diagnosis.__file__)
from patient import Patient
from classifier import Classifier
from finding_manager import FindingManager
from clinical_guidance import ClinicalGuidance

# Create a patient
patient = Patient()

# ----------------------------
# Enter patient data
# ----------------------------

patient.age = 25
patient.sex = "Male"

patient.total_bilirubin = 5.0
patient.direct_bilirubin = 0.5

patient.ast = 40
patient.alt = 60
patient.alp = 60

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

guidance = ClinicalGuidance()
guidance.generate(patient)

# ----------------------------
# Display findings
# ----------------------------

FindingManager.display(patient)

print("\n===== PROVISIONAL DIAGNOSIS =====")
print(patient.findings)
print(type(patient.provisional_diagnosis))
print(repr(patient.provisional_diagnosis))
print("\n===== PROBABLE DISEASES =====")

for disease, test in patient.probable_diseases:
    print(f"- {disease}")
    print(f"  Clinching test: {test}")