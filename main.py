# -*- coding: utf-8 -*-
# @Author  : relakkes@gmail.com
# @Time    : 2024/3/21 23:12

import asyncio


class MediaCrawler:
    def __init__(self):
        self.email = "relakkes@gmail.com"
        self.user_name = "Relakkes Yang"

    async def start(self):
        print(f"{self.user_name} {self.email}")
        print("I enjoy programming for web crawling and open source.\n"
              "But for certain reasons, I am unable to pursue it.")


if __name__ == '__main__':
    asyncio.run(MediaCrawler().start())
