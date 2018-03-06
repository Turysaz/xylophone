

from .ConfigurationService import create_configuration_parser
from .EventAggregator import EventAggregator
from .IoCContainer import IoCContainer
from .MainControl import MainControl
from .MainView import MainView
from .ObjectFactory import ObjectFactory
from .ProjectParser import ProjectParser

class Bootstrapper():

    def __init__(self):

        self.ioc = IoCContainer()

        self.ioc.register_singleton("conf", create_configuration_parser)
        self.ioc.register_singleton("ea", EventAggregator)
        self.ioc.register_singleton("of", ObjectFactory, "ea")
        self.ioc.register_singleton("pp", ProjectParser, "ea","of")
        self.ioc.register_singleton("view", MainView, "conf", "ea")
        self.ioc.register_singleton("ctrl", MainControl, "conf", "ea", "view", "pp")

    def bootstrap(self):
        ctrl = self.ioc.get_instance("ctrl")
        ctrl.run_game()