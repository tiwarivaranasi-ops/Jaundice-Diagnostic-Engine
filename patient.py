"""
Patient Class
Stores all information entered for one patient.
"""


class Patient:

    def __init__(self):

        # -------------------------
        # Demographics
        # -------------------------

        self.age = None
        self.sex = None


        # -------------------------
        # History
        # -------------------------

        self.fever = False
        self.abdominal_pain = False
        self.pruritus = False
        self.dark_urine = False
        self.pale_stools = False
        self.nausea = False
        self.vomiting = False
        self.alcohol_history = False
        self.drug_history = False
        self.weight_loss = False
        self.family_history = False


        # -------------------------
        # Examination
        # -------------------------

        self.pallor = False
        self.hepatomegaly = False
        self.tender_hepatomegaly = False
        self.splenomegaly = False


        # -------------------------
        # Laboratory
        # -------------------------

        self.hb = None
        self.pbs = None

        self.total_bilirubin = None
        self.direct_bilirubin = None

        self.ast = None
        self.alt = None
        self.alp = None
        self.ggt = None


        # -------------------------
        # Imaging
        # -------------------------

        self.usg = None


        # -------------------------
        # Engine Output
        # -------------------------

        self.findings = set()

        self.provisional_diagnosis = None

        self.differential_diagnosis = []