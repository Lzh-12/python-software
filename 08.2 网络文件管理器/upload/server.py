import asyncio
import mimetypes
import os
import uuid


class FileServer:
    def __init__(self):
        self.upload_dir = 'uploads'  # 文件保存目录
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    async def handle_client(self, reader, writer):
        while True:
            data = await reader.read(100)
            message = data.decode()
            if message.startswith('upload'):
                _, file_path = message.split(' ')
                await self.handle_upload(file_path, writer)
            elif message.startswith('list'):
                _, keyword = message.split(' ')
                await self.handle_list(keyword, writer)
            elif message.startswith('download'):
                _, file_name, save_path = message.split(' ')
                await self.handle_download(file_name, save_path, writer)
            elif message.strip() == '/quit':
                break

    async def handle_upload(self, file_path, writer):
        try:
            file_name = os.path.basename(file_path)
            mime_type, _ = mimetypes.guess_type(file_name)
            file_extension = mimetypes.guess_extension(mime_type)
            new_file_name = str(uuid.uuid4()) + file_extension
            new_file_path = os.path.join(self.upload_dir, new_file_name)
            with open(file_path, 'rb') as f:
                with open(new_file_path, 'wb') as new_f:
                    new_f.write(f.read())
            writer.write('Upload Done'.encode())
            await writer.drain()
        except Exception as e:
            writer.write(f'Upload Failed: {e}'.encode())
            await writer.drain()

    async def handle_list(self, keyword, writer):
        files = os.listdir(self.upload_dir)
        if keyword == '*':
            file_list = ', '.join(files)
        else:
            file_list = ', '.join([f for f in files if keyword in f])
        writer.write(file_list.encode())
        await writer.drain()

    async def handle_download(self, file_name, save_path, writer):
        file_path = os.path.join(self.upload_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
            with open(save_path, 'wb') as save_f:
                save_f.write(content)
            writer.write('Download Done'.encode())
            await writer.drain()
        else:
            writer.write('File Not Found'.encode())
            await writer.drain()

    async def run_server(self):
        server = await asyncio.start_server(self.handle_client, '127.0.0.1', 8888)
        async with server:
            await server.serve_forever()


def main():
    file_server = FileServer()
    asyncio.run(file_server.run_server())


if __name__ == '__main__':
    main()
