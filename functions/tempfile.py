from tempfile import NamedTemporaryFile
from config import toastalerts as tst

def get_tempfile_path_image(varImage):
        
    with NamedTemporaryFile(delete=False, suffix=".jpg") as tmpfile:
        varImage.save(tmpfile, format="JPEG")  # Save the image to the temporary file
        image_path = tmpfile.name
    return image_path


def get_tempfile_path_audio_wav(varAudioSegment):

    with NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        varAudioSegment.save(tmpfile, format="WAV")
        audio_path = tmpfile.name
    return audio_path
    

def get_tempfile_path_audio_mp3():
    with NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        temp_file_path = tmpfile.name
        return temp_file_path
    
def create_temp_file(varSuffix: str):
    with NamedTemporaryFile(delete=False, suffix=varSuffix) as tmpfile:
        temp_file_path = tmpfile.name
    return temp_file_path
