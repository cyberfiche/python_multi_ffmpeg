"""
This python script encodes all files that have the extension MOD in the current
working directory.

Sources:
    https://trac.ffmpeg.org/wiki/Encode/VP9
    https://www.virag.si/2012/01/webm-web-video-encoding-tutorial-with-ffmpeg-0-9/
"""
import subprocess, os, glob

# -------------------------------------------------------------------------------
# CONFIGURABLE SETTINGS
# -------------------------------------------------------------------------------

# path to ffmpeg bin
FFMPEG_PATH = os.path.join(os.environ['USERPROFILE'], 'opt', 'ffmpeg', 'bin')
source_path = os.path.join('K:',
                           'Phase V Annexation Project Files',
                           'Project VII- Area 16 and 17',
                           'Area 17',
                           'MKR PRECONSTRUCTION VIDEO\DISK 1')
dest_path = os.path.join('C:', 'Users', 'prevettej', 'opt', 'ffmpeg')
ext = '*.MOD'
webm_params = [
    '-codec:v', 'libvpx',
    '-quality', 'good',
    '-cpu-used', '0',
    '-b:v', '500k',
    '-qmin', '10',
    '-qmax', '42',
    '-maxrate', '500k',
    '-bufsize', '1000k',
    '-threads' '4',
    '-vf', 'scale=-1:480',
    '-codec:a', 'libvorbis',
    '-b:a', '128k',
]


# -------------------------------------------------------------------------------
# encoding script
# -------------------------------------------------------------------------------
def process():
    # get a list of files that have the extension mkv
    # filelist = filter(lambda f: f.split('.')[-1] == 'mkv', os.listdir(cwd))
    # filelist = sorted(filelist)

    # use glob instead of filter

    glob_list = glob.glob(os.path.join(source_path, ext))
    # encode each file
    # for source_file_path in glob_list:
        # encode(source_file_path)
        # file_name = (file.split('\\')[-1]).split('.')[0]
    for __ in range(0,1):
        encode(glob_list[0])


def encode(source_file_path):
    # dest_file_path = '{}.webm'.format((source_file_path.split('\\')[-1]).split('.')[0])
    # dest_file_path = '{}.webm'.format(source_file_path.split('.')[0])
    # dest_file_path = os.devnull
    dest_file_path = ''

    try:
        command = [
            'ffmpeg',
            '-i', source_file_path,
            '-codec:v', 'libvpx',
            '-quality', 'good',
            '-cpu-used', '0',
            '-b:v', '500k',
            '-qmin', '10',
            '-qmax', '42',
            '-maxrate', '500k',
            '-bufsize', '1000k',
            '-threads', '4',
            '-vf', 'scale=-1:480',
            '-codec:a', 'libvorbis',
            '-b:a', '128k',
            '-f', 'null',
            dest_file_path
        ]
        subprocess.call(command)  # encode the video!
    finally:
        print(source_file_path, dest_file_path, sep='\n')


if __name__ == "__main__":
    process()
