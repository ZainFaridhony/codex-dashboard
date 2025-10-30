"""Simple in-memory rate limiter placeholder."""
from collections import defaultdict
from datetime import datetime, timedelta

_BUCKET: dict[str, list[datetime]] = defaultdict(list)


def is_allowed(key: str, limit: int, window: timedelta) -> bool:
    """Check whether a request is allowed within a time window."""

    now = datetime.utcnow()
    entries = _BUCKET[key]
    _BUCKET[key] = [ts for ts in entries if now - ts <= window]
    if len(_BUCKET[key]) >= limit:
        return False
    _BUCKET[key].append(now)
    return True
