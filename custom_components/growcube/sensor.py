import logging
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

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
    def unique_id(self):
        return f"{self._host}-moisture"

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return "%"

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Replace with your API call
        # data = await hass.async_add_executor_job(fetch_moisture, self._host, self._api_key)
        # self._state = data["moisture"]
        self._state = 42  # stub
