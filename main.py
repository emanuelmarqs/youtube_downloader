#Instalar biblioteca (pip install pytube)
#pip freeze > requeriments.txt

from pytube import YouTube
from pytube.cli import on_progress

def salvar_video(link_do_video):
    print("Iniciando download...")

    try:
        yt = YouTube(link_do_video, on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()

        return "\nDownload completo!"
    
    except:
        return "Não foi possível baixar o vídeo"
    
if __name__ == "__main__":
    while True:
        link_do_video = input("Informe o link do vídeo para baixar ou aperte ENTER para encerrar o programa: ")

        if link_do_video != '':
            print(salvar_video(link_do_video))
            continue
        else:
            print("Programa encerrado!")
            break
