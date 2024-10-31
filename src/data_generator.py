import random

class DataGenerator:
    def generate_data(self):
        return {
            'engine_temperature': random.uniform(70, 120),
            'oil_level': random.uniform(0, 100),
            'engine_rpm': random.uniform(500, 7000),
            'battery_charge': random.uniform(0, 100),
            'battery_voltage': random.uniform(10, 14),
            'tire_pressure': random.uniform(25, 38),
            'tire_tread_depth': random.uniform(1, 10)
        }