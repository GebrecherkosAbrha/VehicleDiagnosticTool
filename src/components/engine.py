class Engine:
    def __init__(self):
        self.temperature = 0
        self.oil_level = 100
        self.rpm = 0

    def diagnose(self, data):
        self.temperature = data['engine_temperature']
        self.oil_level = data['oil_level']
        self.rpm = data['engine_rpm']
        
        issues = []
        if self.temperature > 100:
            issues.append(f"Engine temperature is too high ({self.temperature}°C)")
        if self.oil_level < 20:
            issues.append(f"Oil level is low ({self.oil_level}%)")
        if self.rpm > 6000:
            issues.append(f"Engine RPM is too high ({self.rpm})")
        
        return issues