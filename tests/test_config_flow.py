"""config_flow tests."""

from unittest import mock

# from custom_components.lvgl_pages import config_flow
from custom_components.lvgl_pages.const import *
import pytest

# from pytest_homeassistant_custom_component.async_mock import patch
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_FILE_PATH, CONF_NAME

SCHEMA_COPY = vol.Schema(
    {
        vol.Required(CONF_NAME): str,
        vol.Required(CONF_FILE_PATH): str,
    }
)


# @pytest.mark.asyncio
# async def test_flow_init(hass):
#     """Test the initial flow."""
#     result = await hass.config_entries.flow.async_init(
#         config_flow.DOMAIN, context={"source": "user"}
#     )

#     expected = {
#         "data_schema": SCHEMA_COPY,
#         # "data_schema": config_flow.DATA_SCHEMA,
#         "description_placeholders": None,
#         "errors": {},
#         "flow_id": mock.ANY,
#         "handler": "lvgl_pages",
#         "step_id": "user",
#         "type": "form",
#     }
#     assert expected == result
