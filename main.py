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

patient.total_bilirubin = 8.0
patient.direct_bilirubin = 2.0

patient.ast = 100
patient.alt = 100
patient.alp = 800

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

print(patient.provisional_diagnosis)

if patient.provisional_diagnosis is None:
    print("Hyperbilirubinemia absent. Investigate for other conditions.")
else:
    print("\n===== PROBABLE DISEASES =====")

    for disease, test in patient.probable_diseases:
     print(f"- {disease}")
     print(f"  Clinching test: {test}")