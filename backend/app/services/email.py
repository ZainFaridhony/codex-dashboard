"""Email service adapter placeholder for Brevo integration."""


class EmailService:
    """Service responsible for sending transactional emails."""

    async def send_password_reset(self, *args, **kwargs):  # noqa: ANN002, ANN003
        raise NotImplementedError
