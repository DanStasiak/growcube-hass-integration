import logging
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    config = entry.data
    host = config["host"]
    api_key = config["api_key"]
    interval = config.get("poll_interval", 300)
    threshold = config.get("moisture_threshold", 30)

    entities = [
        GrowCubeMoistureSensor(host, api_key, interval),
        GrowCubeLastWateredSensor(host, api_key, interval),
        GrowCubeNeedsWaterBinarySensor(host, api_key, interval, threshold),
    ]
    async_add_entities(entities, True)

class GrowCubeMoistureSensor(Entity):
    """Soil moisture %."""
    def __init__(self, host, api_key, interval):
        self._host = host
        self._api_key = api_key
        self._interval = interval
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
        data = await self._fetch_data()
        self._state = data.get("moisture")

class GrowCubeLastWateredSensor(Entity):
    """Timestamp of last watering."""
    def __init__(self, host, api_key, interval):
        self._host = host
        self._api_key = api_key
        self._interval = interval
        self._state = None

    @property
    def name(self):
        return "GrowCube Last Watered"

    @property
    def unique_id(self):
        return f"{self._host}-last-watered"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        data = await self._fetch_data()
        # assume your API returns an ISO timestamp under "last_watered"
        self._state = data.get("last_watered")

class GrowCubeNeedsWaterBinarySensor(BinarySensorEntity):
    """On if moisture < threshold."""
    def __init__(self, host, api_key, interval, threshold):
        self._moisture_sensor = GrowCubeMoistureSensor(host, api_key, interval)
        self._threshold = threshold

    @property
    def name(self):
        return "GrowCube Needs Water"

    @property
    def unique_id(self):
        return f"{self._moisture_sensor._host}-needs-water"

    @property
    def is_on(self):
        try:
            return float(self._moisture_sensor.state) < self._threshold
        except (TypeError, ValueError):
            return False

    async def async_update(self):
        # update the underlying moisture sensor first
        await self._moisture_sensor.async_update()
