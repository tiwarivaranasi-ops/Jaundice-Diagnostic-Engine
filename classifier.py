"""
Classifier
Generates biochemical findings from laboratory data.
"""

from constants import *
from finding_ids import *
from finding_manager import FindingManager
from symptom_scorer import SymptomScorer


class Classifier:

    def classify(self, patient):

        self.classify_bilirubin(patient)
        self.classify_pattern(patient)

        SymptomScorer().score(patient)
        
        
        

    # -----------------------------------
    # C001
    # Direct / Indirect Hyperbilirubinemia
    # -----------------------------------

    def classify_bilirubin(self, patient):

        if patient.total_bilirubin is None:
            return

        if patient.direct_bilirubin is None:
            return

        direct_percent = (
            patient.direct_bilirubin /
            patient.total_bilirubin
        ) * 100

        if direct_percent > DIRECT_BILIRUBIN_PERCENT:

            FindingManager.add(patient, F001)

        else:

            FindingManager.add(patient, F002)

    # -----------------------------------
    # C002
    # Pattern Classification
    # -----------------------------------

    def classify_pattern(self, patient):

        if (
            patient.ast is None or
            patient.alt is None or
            patient.alp is None
        ):
            return

        # Cholestatic Pattern

        if patient.alp >= ALP_ULN * CHOLESTATIC_ALP_MULTIPLE:

            FindingManager.add(patient, F005)

            

        # Hepatocellular Pattern

        if (
            patient.ast >= AST_ULN * HEPATOCELLULAR_AST_MULTIPLE
            or
            patient.alt >= ALT_ULN * HEPATOCELLULAR_ALT_MULTIPLE
        
        ):

            FindingManager.add(patient, F004)

            return

        # Isolated Hyperbilirubinemia

        FindingManager.add(patient, F003)