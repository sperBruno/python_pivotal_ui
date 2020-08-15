from utils.property_reader import PropertyReader


class PropertyHandler:

    @staticmethod
    def get_instance():
        return PropertyReader.get_property()
