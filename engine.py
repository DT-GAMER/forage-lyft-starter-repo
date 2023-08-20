import abc from ABC, abstractmethod

class Engine(ABC):
    def __init__(self, current_mileage, current_service_mileage, warning_indicator_on=False):
        self.current_mileage = current_mileage
        self.current_service_mileage = current_service_mileage
        self.warning_inicator_on = warning_indicator_on

    @abstractmethod
    def engine_needs_service(self):
        pass
