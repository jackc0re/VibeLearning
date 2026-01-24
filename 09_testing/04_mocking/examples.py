"""\
Mocking - Examples

Demonstrates:
  - dependency replacement with unittest.mock.patch

Run with:
    python examples.py
"""


from __future__ import annotations

from dataclasses import dataclass
from unittest.mock import patch


@dataclass(frozen=True)
class Weather:
    temp_c: float


def fetch_weather_from_api(city: str) -> Weather:
    """Pretend to call an external API (we will mock this in tests)."""
    raise RuntimeError("Network call not allowed in example")


def should_wear_jacket(city: str) -> bool:
    weather = fetch_weather_from_api(city)
    return weather.temp_c < 12


def demo_patch():
    with patch(__name__ + ".fetch_weather_from_api") as mock_fetch:
        mock_fetch.return_value = Weather(temp_c=5)
        assert should_wear_jacket("Sofia") is True

        mock_fetch.return_value = Weather(temp_c=25)
        assert should_wear_jacket("Sofia") is False

    print("OK - Mocking demo passed")


if __name__ == "__main__":
    demo_patch()

