"""
Diagnosis Engine
"""

from finding_ids import F001, F002, F003, F004, F005
from diagnosis_ids import D101, D102, D103, D104

REFERRAL = "Refer for specialist evaluation"
DEADLOCK = "Biochemical Deadlock"



class Diagnosis:

    def diagnose(self, patient):
        

        patient.deadlock = False
        patient.referral = False

        if F004 in patient.findings and F005 in patient.findings:
                   patient.deadlock = True

        if F004 not in patient.findings and F005 not in patient.findings:
                       patient.deadlock = True
        
        if patient.deadlock:
            
            
            
                  
            
            if patient.hepatocellular_score > patient.cholestatic_score:
               patient.provisional_diagnosis = D101
            elif patient.cholestatic_score > patient.hepatocellular_score:
                 patient.provisional_diagnosis = D102
                 
            else:
                 patient.referral = True 
                 patient.provisional_diagnosis = REFERRAL
        
        
        

        

        
        if F004 in patient.findings:
           patient.provisional_diagnosis = D101
        if F005 in patient.findings:

            patient.provisional_diagnosis = D102
        if F001 in patient.findings:
            
            if F004 not in patient.findings:
                if F005 not in patient.findings:
                    patient.provisional_diagnosis = D103
                    print("Diagnosis set to D103")
        if F002 in patient.findings:
            if F003 in patient.findings:
                    patient.provisional_diagnosis = D104       