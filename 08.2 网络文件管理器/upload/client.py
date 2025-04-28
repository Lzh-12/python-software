import asyncio


async def send_message(writer, message):
    writer.write(message.encode())
    await writer.drain()


async def handle_response(reader):
    data = await reader.read(100)
    message = data.decode()
    print(message)


async def upload_file(writer, file_path, reader):
    await send_message(writer, f'upload {file_path}')
    await handle_response(reader)  # 修复处


async def list_files(writer, keyword, reader):
    await send_message(writer, f'list {keyword}')
    await handle_response(reader)  # 修复处


async def download_file(writer, file_name, save_path, reader):
    await send_message(writer, f'download {file_name} {save_path}')
    await handle_response(reader)  # 修复处


async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    # await upload_file(writer, 'd:\\netty.png', reader)  # 上传文件
    await upload_file(writer, 'netty.png', reader)  # 上传文件
    await list_files(writer, '*', reader)  # 列出所有文件
    # await download_file(writer, 'file_name', 'save_path', reader)  # 下载文件
    writer.write('/quit'.encode())
    await writer.drain()
    writer.close()


if __name__ == '__main__':
    asyncio.run(main())
