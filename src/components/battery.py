from config import DIAGNOSTIC_THRESHOLDS


class Battery:
    def diagnose(self, data):
        issues = []
        if data['battery_voltage'] < 12.0:
            issues.append(f"Battery voltage is low ({
                          data['battery_voltage']} V)")
        if data['battery_health'] < 70:
            issues.append(f"Battery health is poor ({
                          data['battery_health']}%)")
        return issues
