It is a simple and straightforward solution to **download youtube videos**, **audios** and **playlists** using your **local** computational **resources**.

It is entirely written in **python** with **pytube** and **moviepy** libraries.


How to use:
1. create a new folder (e.g. `mkdir python_youtube_downloader`)
2. get into the folder (`cd python_youtube_downloader`)
3. clone repository (`git clone git@github.com:ds-gustavo-cunha/python_local_downloader.git`)
4. create a new venv locally (in case of *pipenv*: `pipenv shell`)
5. install dependencies on the new venv (in case of *pipenv*: `pipenv install -r requirements.txt`)
6. run download script with Makefile: `make download`
7. follow the instruction to download videos/audios