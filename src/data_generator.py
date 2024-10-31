import random


class DataGenerator:
    def generate_data(self):
        return {
            'engine_temperature': random.uniform(-10, 130),
            'oil_level': random.uniform(0, 100),
            'battery_voltage': random.uniform(10, 14),
            'battery_health': random.randint(50, 100),
            'tire_pressure': random.uniform(25, 40),
            'tire_tread_depth': random.uniform(1, 15)
        }
