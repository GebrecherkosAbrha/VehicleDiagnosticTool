from config import DIAGNOSTIC_THRESHOLDS


class Tire:
    def diagnose(self, data):
        issues = []
        if data['tire_pressure'] < DIAGNOSTIC_THRESHOLDS['tire_pressure']['min']:
            issues.append(
                f"Tire pressure is low ({data['tire_pressure']} PSI)")
        elif data['tire_pressure'] > DIAGNOSTIC_THRESHOLDS['tire_pressure']['max']:
            issues.append(f"Tire pressure is high ({
                          data['tire_pressure']} PSI)")

        if data['tire_tread_depth'] < DIAGNOSTIC_THRESHOLDS['tire_tread_depth']['min']:
            issues.append(f"Tire tread depth is low ({
                          data['tire_tread_depth']} mm)")
        return issues
