class Battery:
    def __init__(self):
        self.charge = 100
        self.voltage = 12

    def diagnose(self, data):
        self.charge = data['battery_charge']
        self.voltage = data['battery_voltage']
        
        issues = []
        if self.charge < 25:
            issues.append(f"Battery charge is low ({self.charge}%)")
        if self.voltage < 11.5:
            issues.append(f"Battery voltage is low ({self.voltage}V)")
        
        return issues