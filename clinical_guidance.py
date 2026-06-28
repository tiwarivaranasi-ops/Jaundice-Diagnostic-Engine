from diagnosis_ids import D101, D102, D103, D104, D105


class ClinicalGuidance:

    def generate(self, patient):

        if patient.provisional_diagnosis == D101:

            patient.probable_diseases = [
                ("Acute Hepatitis A", "HAV IgM"),
                ("Acute Hepatitis B", "HBsAg + Anti-HBc IgM"),
                ("Acute Hepatitis E", "HEV IgM"),
                ("Drug-induced Liver Injury", "Detailed Drug History"),
                ("Autoimmune Hepatitis", "ANA + Serum IgG")
            ]
        elif patient.provisional_diagnosis == D102:

             patient.probable_diseases = [
                ("Choledocholithiasis", "Ultrasound Abdomen"),
                ("Carcinoma Head of Pancreas", "CECT Abdomen"),
                ("Cholangiocarcinoma", "MRCP")
    ]   
             
        elif patient.provisional_diagnosis == D103:

             patient.probable_diseases = [
             ("Drug-induced Liver Injury", "Detailed Drug History"),
             ("Alcoholic Hepatitis", "Detailed Alcohol History"),
             ("Acute Hepatitis A", "HAV IgM"),
             ("Acute Hepatitis E", "HEV IgM"),
             ("Primary Sclerosing Cholangitis", "MRCP"),
             ("Autoimmune Hepatitis / PBC Overlap", "ANA + AMA")
    ]
          
        elif patient.provisional_diagnosis == D104:
             patient.probable_diseases = [
             ("Dubin-Johnson Syndrome", "Urinary Coproporphyrin Analysis"),
             ("Rotor Syndrome", "Urinary Coproporphyrin Analysis")
]
          
        elif patient.provisional_diagnosis == D105:
             patient.probable_diseases = [
             ("Gilbert Syndrome", "UGT1A1 Genetic Test"),
             ("Hemolytic Anemia", "Peripheral Blood Smear + Reticulocyte Count"),
             ("Crigler-Najjar Syndrome", "UGT1A1 Genetic Test")
]
          