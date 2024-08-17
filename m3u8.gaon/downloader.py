import os
import requests
import m3u8
from concurrent.futures import ThreadPoolExecutor

class M3U8Downloader:
    def __init__(self, m3u8_url, output_path='output.mp4', max_workers=5):
        self.m3u8_url = m3u8_url
        self.output_path = output_path
        self.max_workers = max_workers
        self.ts_files = []
        self.base_url = '/'.join(m3u8_url.split('/')[:-1])

    def download_ts(self, ts_url, ts_filename):
        response = requests.get(ts_url, stream=True)
        if response.status_code == 200:
            with open(ts_filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {ts_filename}")
        else:
            print(f"Failed to download {ts_filename}")

    def download(self):
        m3u8_obj = m3u8.load(self.m3u8_url)
        ts_urls = [segment.uri for segment in m3u8_obj.segments]
        ts_filenames = [f"segment_{i}.ts" for i in range(len(ts_urls))]
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for ts_url, ts_filename in zip(ts_urls, ts_filenames):
                ts_url_full = ts_url if ts_url.startswith('http') else f"{self.base_url}/{ts_url}"
                self.ts_files.append(ts_filename)
                executor.submit(self.download_ts, ts_url_full, ts_filename)
        
        executor.shutdown(wait=True)
        self.combine_ts_files()

    def combine_ts_files(self):
        with open(self.output_path, 'wb') as output_file:
            for ts_file in self.ts_files:
                with open(ts_file, 'rb') as f:
                    output_file.write(f.read())
                os.remove(ts_file)
        print(f"Saved combined video to {self.output_path}")
