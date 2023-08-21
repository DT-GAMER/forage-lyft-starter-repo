from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerEngine
from tires_carrigan_tire import CarriganTire

class Glissade(car):
    def __init__(self, current_mileage, current_service_mileage, last_service_date, tire_sensor_data):
        glissade_engine = WilloughbyEngine(current_mileage, current_service_mileage)
        glissade_engine = SpindlerBattery(last_service_date)
        glissade_engine = CarriganTire(tire_sensor_data)

        super().__init__(glissade_engine, glissade_battery, glissade_tire);

    def needs_service(self):
        return super().needs_service()
