class SymptomScorer:

    def score(self, patient):
        patient.hepatocellular_score = 0
        patient.cholestatic_score = 0
        
        if patient.prodromal_symptoms:
           patient.hepatocellular_score += 1

        if patient.alcohol_history:
           patient.hepatocellular_score += 1
        
        if patient.pruritus:
           patient.cholestatic_score += 1
        
        if patient.dark_urine:
           patient.cholestatic_score += 1
        
        if patient.pale_stools:
           patient.cholestatic_score += 1


        

        