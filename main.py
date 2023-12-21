###########
# IMPORTS #
###########

# import required libraries
import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip


#############
# CONSTANTS #
#############

# define constants
end = "\033[0m"
bold = "\033[1m"
bold_green = "\033[1m\033[92m"
bold_warning = "\033[1m\033[93m"


###################
# DEFINE FUNTIONS #
###################


def get_urls_(link: str) -> list:
    """
    Get a youtube link and return a list of links to download

    Args
        link: str with youtube link
    """

    # try to get link
    try:
        YouTube(link)
    # in case it is not a video but a playlist
    except:
        return Playlist(link)
    # in case it is a single video
    else:
        return [link]


def convert_video_to_audio_(video_file_path: str) -> None:
    """
    Get the path to a given .mp4 file and convert it to .mp3

    Args
        video_file_path: str with the path to the file to convert
    """
    # print info
    print(f"Converting video to audio...")

    # define audio object
    audioclip = AudioFileClip(video_file_path)

    # open video object as audio object
    with AudioFileClip(video_file_path) as audioclip:
        # convert to mp3
        audioclip.write_audiofile(video_file_path[:-4] + ".mp3")

    # delete .mp4 file to remove duplicates
    os.remove(video_file_path)


def download_video_(
    video_link: str, folder_to_save: str, save_as_audio: bool, i: int, N: int
) -> None:
    """
    Download youtue video given the video link

    Args
        video_link: str with the youtube video link
        folder_to_save: str with the folder to save the files inside
        save_as_audio: boolean to indicate if file has to be a .mp3
            instead of .mp4
        i: int with number of video on a playlist
        N: int with the number of videos on the playlist
    """

    # instanciate a youtube object
    yt = YouTube(video_link)
    # filter video options
    yt_video = (
        yt.streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )
    # get file name
    yt_file_name = yt_video.default_filename
    # check if link is a single video or a part of a playlist
    if N > 1:
        # add number of video in case of playlist
        yt_file_name = f"{i+1} - {yt_video.default_filename}"

    # define path to save
    if folder_to_save != ".":
        video_file_path = folder_to_save
    # save on current folder
    else:
        video_file_path = "."

    # download video
    yt_video.download(
        output_path=video_file_path, filename=yt_file_name, skip_existing=True
    )

    # check if has to convert video to audio
    if save_as_audio:
        # convert video to audio
        convert_video_to_audio_(os.path.join(video_file_path, yt_file_name))


def download(link: str, folder_to_save: str = ".", save_as_audio: bool = False) -> None:
    """
    Download video/audio files given an Youtube URL

    Args
        link: str with Youtube URL
        folder_to_save: str with folder name to save files inside
        save_as_audio: bool to indicate if files have to be saved as .mp3
            instead of .mp4
    """

    # get links
    links = get_urls_(link)
    # get number of links
    N = len(links)
    # print info
    print(f"\n{bold_green}There are {N} videos to download!{end} ")
    print(f"{bold_green}---> Downloading all {N} videos <---{end}")

    # iterate over links
    for i, link in enumerate(links):
        # print info
        print(f"\n{bold}Downloading video {i+1} of {N}{end}")
        # try to download videos
        try:
            # download videos
            download_video_(link, folder_to_save, save_as_audio, i, N)
            # print info
            print(f"{bold}    Video {i+1} is downloaded \o/{end}")
        # in case of errors
        except Exception as e:
            # print log
            print(
                f"The following error when downloading track {i+1} out of {len(links)}: {e}"
            )
            # skip to next track
            continue


############
# RUN CODE #
############

# check if code is being call directly
if __name__ == "__main__":
    # ask for url
    url = input(f"\n{bold_warning}Paste the URL to download content:{end} ")
    # ask for output format
    save_as_audio = input(
        f"{bold_warning}Save as video [V] or audio [A] ?{end} "
    ).lower()
    # check user input until an expected response
    while save_as_audio.lower() not in ["v", "a"]:
        # keep asking
        save_as_audio = input(
            f"{bold_warning}Save as video [V] or audio [A] ?{end} "
        ).lower()
    # define response dict
    output_format = {"a": True, "v": False}
    # ask for output format
    folder_to_save = input(
        f"{bold_warning}Define folder to save content [ENTER to save on current folder]:{end} "
    )
    # check if user didn't defined a folder to save
    if folder_to_save == "":
        # set default to current
        folder_to_save = "."

    # download
    download(
        link=url,
        folder_to_save=folder_to_save,
        save_as_audio=output_format[save_as_audio],
    )
