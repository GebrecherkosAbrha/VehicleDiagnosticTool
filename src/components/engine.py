from config import DIAGNOSTIC_THRESHOLDS


class Engine:
    def diagnose(self, data):
        issues = []
        if data['engine_temperature'] > DIAGNOSTIC_THRESHOLDS['engine_temperature']['max']:
            issues.append(f"Engine temperature is too high ({
                          data['engine_temperature']}°C)")
        if data['oil_level'] < DIAGNOSTIC_THRESHOLDS['oil_level']['min']:
            issues.append(f"Oil level is low ({data['oil_level']}%)")
        return issues
