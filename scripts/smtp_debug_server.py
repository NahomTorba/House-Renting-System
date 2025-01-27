import asyncio
from aiosmtpd.controller import Controller

class DebuggingServer:
    async def handle_DATA(self, server, session, envelope):
        print('Message from:', envelope.mail_from)
        print('Message to:', envelope.rcpt_tos)
        print('Message data:', envelope.content.decode('utf8', errors='replace'))
        return '250 OK'

controller = Controller(DebuggingServer(), hostname='localhost', port=1025)
controller.start()

try:
    asyncio.run(asyncio.Event().wait())
except KeyboardInterrupt:
    pass
