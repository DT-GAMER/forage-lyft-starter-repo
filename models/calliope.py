from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_engine = SpindlerBattery(last_service_date)
        calliope_tire = OctoprimeTire(tire_sensor_date):

        super().__init__(calliope_engine, calliope_batteries, calliope_tire)

        self.engine = Calliope_engine
        self.engine = calliope_battery
        self.engine = calliope_tire

    def needs_service(self):
        return super().needs_service()
