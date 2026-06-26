"""
Diagnosis Engine
"""

from finding_ids import F004
from diagnosis_ids import D101


class Diagnosis:

    def diagnose(self, patient):

        if F004 in patient.findings:

            patient.provisional_diagnosis = D101