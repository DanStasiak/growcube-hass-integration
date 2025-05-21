import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors from a config entry."""
    config = entry.data
    host = config["host"]
    api_key = config["api_key"]
    async_add_entities([GrowCubeMoistureSensor(host, api_key)], True)

class GrowCubeMoistureSensor(Entity):
    """Representation of a GrowCube soil moisture sensor."""

    def __init__(self, host, api_key):
        self._host = host
        self._api_key = api_key
        self._state = None

    @property
    def name(self):
        return "GrowCube Moisture"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Placeholder for actual API call
        self._state = 50
