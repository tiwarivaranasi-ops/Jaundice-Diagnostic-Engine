class RValueCalculator:

    @staticmethod
    def calculate(patient):

        if patient.alt is None or patient.alp is None:
            return None

        if patient.alp == 0:
            return None

        # NEW CHECK
        if patient.alt <= 50 and patient.alp <= 180:
            return None

        alt_ratio = patient.alt / 50
        alp_ratio = patient.alp / 180

        r_value = alt_ratio / alp_ratio
        return r_value