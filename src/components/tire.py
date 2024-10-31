class Tire:
    def __init__(self):
        self.pressure = 32
        self.tread_depth = 8

    def diagnose(self, data):
        self.pressure = data['tire_pressure']
        self.tread_depth = data['tire_tread_depth']
        
        issues = []
        if self.pressure < 28:
            issues.append(f"Tire pressure is low ({self.pressure} PSI)")
        elif self.pressure > 35:
            issues.append(f"Tire pressure is high ({self.pressure} PSI)")
        if self.tread_depth < 3:
            issues.append(f"Tire tread depth is low ({self.tread_depth} mm)")
        
        return issues