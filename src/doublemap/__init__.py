import copy
import requests


class RouteTracker(object):
    """ 
    DoubleMap Bus route tracker.
    Params: string domain (example: 'http://iupui.doublemap.com/')
            string google_api_key
    """
    def __init__(self, domain, google_api_key):
        if domain.endswith('/'):
            domain = domain[:-1]
        self.__domain = domain
        self.__api_key = google_api_key
        self.__buses = {}
        self.__routes = {}

    def fetch(self):
        """ Fetch bus and route information. """
        bus_url = self.__domain + "/map/v2/buses"
        buses = requests.get(bus_url).json()
        # add each bus to the dict of buses
        for bus in buses:
            bus_info = copy.deepcopy(bus)
            bus_info.pop('id', None)
            self.__buses[bus['id']] = bus_info

        routes_url = self.__domain + "/map/v2/routes"
        routes = requests.get(routes_url).json()
        # add each route to the dict of routes
        for route in routes:
            route_info = copy.deepcopy(route)
            route_info.pop('id', None)
            self.__routes[route['id']] = route_info

    def bus_info(self, bus_id):
        """ Get information about a specific bus id. """
        return self.__buses[bus_id]

    def route_info(self, route_id):
        """ Get information about a specific route id. """
        return self.__routes[route_id]

    """ Test method for calling the google api

    def distance(self):
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
        origin_param = "%s, %s" % (self.bus_info(247)['lat'],
                                   self.bus_info(247)['lon'])
        dest_param = "%s, %s" % (self.bus_info(757)['lat'],
                                 self.bus_info(757)['lon'])
        payload = {'key': self.__api_key,
                   'sensor': 'false',
                   'origins': origin_param,
                   'destinations': dest_param}
        return requests.get(url, params=payload).json()

    """

    @property
    def buses(self):
        return self.__buses

    @property
    def routes(self):
        return self.__routes
