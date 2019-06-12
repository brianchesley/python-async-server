import time
import asyncio

host = ''
port = 12345


def server_response(flag):
    time.sleep(5)
    return 'goodbye!, 5'


async def handle_client(reader, writer):
    request = None
    flag = 1
    while request != 'quit':
        request = (await reader.read(10000))
        print(request)
        response = str(request) + '\n'
        response = server_response(flag)
        writer.write(response.encode('utf8'))

loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(handle_client, host, port))
loop.run_forever()
