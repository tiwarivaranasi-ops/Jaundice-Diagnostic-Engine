"""
Diagnosis Engine
"""

from finding_ids import F004, F005
from diagnosis_ids import D101, D102


class Diagnosis:

    def diagnose(self, patient):

        if F004 in patient.findings:

            patient.provisional_diagnosis = D101
        if F005 in patient.findings:

            patient.provisional_diagnosis = D102