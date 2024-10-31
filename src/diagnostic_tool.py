from components.engine import Engine
from components.battery import Battery
from components.tire import Tire
from data_generator import DataGenerator

class DiagnosticTool:
    def __init__(self):
        self.engine = Engine()
        self.battery = Battery()
        self.tires = [Tire() for _ in range(4)]
        self.data_generator = DataGenerator()

    def run(self):
        try:
            data = self.data_generator.generate_data()
            self.process_data(data)
            self.display_results()
        except Exception as e:
            print(f"An error occurred during diagnostics: {e}")

    def process_data(self, data):
        self.engine_issues = self.engine.diagnose(data)
        self.battery_issues = self.battery.diagnose(data)
        self.tire_issues = [tire.diagnose(data) for tire in self.tires]

    def display_results(self):
        print("\nDiagnostic Results:")
        print("------------------")
        print("Engine:")
        if self.engine_issues:
            for issue in self.engine_issues:
                print(f"  - {issue}")
        else:
            print("  No issues detected")
        
        print("\nBattery:")
        if self.battery_issues:
            for issue in self.battery_issues:
                print(f"  - {issue}")
        else:
            print("  No issues detected")
        
        for i, issues in enumerate(self.tire_issues):
            print(f"\nTire {i+1}:")
            if issues:
                for issue in issues:
                    print(f"  - {issue}")
            else:
                print("  No issues detected")
        
        print("\nDiagnostics complete.")