"""
Diagnosis Engine
"""

from finding_ids import F001, F002, F003, F004, F005, F006, F007
from diagnosis_ids import D101, D102, D103, D104, D105
from clinical_guidance import ClinicalGuidance

REFERRAL = "Refer for specialist evaluation"
DEADLOCK = "Biochemical Deadlock"


print("THIS IS MY DIAGNOSIS.PY")
class Diagnosis:

    def diagnose(self, patient):
        print("DIAGNOSE FUNCTION RUNNING")
        print(patient.findings)
        print(F002)
        print(F002 in patient.findings)
        print(F004)
        print(F004 in patient.findings)

        patient.deadlock = False
        patient.referral = False

        if F004 in patient.findings and F005 in patient.findings:
                   patient.deadlock = True

        if F004 not in patient.findings and F005 not in patient.findings:
                       patient.deadlock = True

        if F001 in patient.findings:

        
         if F004 in patient.findings:
          patient.provisional_diagnosis = D101
          print("Assigned:", patient.provisional_diagnosis)
         if F005 in patient.findings:
          patient.provisional_diagnosis = D102
          
         if F006 in patient.findings:
          patient.provisional_diagnosis = D103
         
         if F003 in patient.findings:
          patient.provisional_diagnosis = D104 
          print(F002)
          print(patient.findings)
          print(F002 in patient.findings)
        if F002 in patient.findings:
             
            

             if F004 in patient.findings:
              patient.provisional_diagnosis = D101
             if F006 in patient.findings:
              patient.provisional_diagnosis = D103
             if F007 in patient.findings:
              patient.provisional_diagnosis = D105
              print("Assigned:", patient.provisional_diagnosis)
        
        
        