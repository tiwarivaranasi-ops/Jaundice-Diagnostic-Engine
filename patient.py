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

        self.prodromal_symptoms = False
        self.pruritus = False
        self.dark_urine = False
        self.pale_stools = False
        self.alcohol_history = False
        
        


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