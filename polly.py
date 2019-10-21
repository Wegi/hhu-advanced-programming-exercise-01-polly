from enum import Enum


class ParrotType(Enum):
    EUROPEAN = "European"
    AFRICAN = "African"
    NORWEGIAN_BLUE = "Norwegian Blue"
    MIXED = "Mixed Parrot"


class Parrot:

    number_of_coconuts = 0

    def __init__(self, type: ParrotType, number_of_coconuts: int, voltage, is_nailed):
        self.type = type
        self.number_of_coconuts = number_of_coconuts
        self.voltage = voltage
        self.is_nailed = is_nailed

    def get_speed(self):
        if self.type == ParrotType.EUROPEAN:
            return self.get_base_speed()
        elif self.type == ParrotType.AFRICAN:
            return max([0, self.get_base_speed() - self.get_load_factor() * self.number_of_coconuts])
        elif self.type == ParrotType.NORWEGIAN_BLUE:
            return 0 if self.is_nailed else self.get_base_speed(with_voltage=True)
        else:
            raise RuntimeError("Should be unreachable")

    def get_base_speed(self, with_voltage=False):
        if with_voltage:
            return min([24.0, self.voltage * self.get_base_speed()])
        else:
            return 12.0

    @staticmethod
    def get_load_factor():
        return 9.0
