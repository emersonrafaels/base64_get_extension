from inspect import stack
from PIL import Image

import pillow_heif

def convert_heic_heif_to_png(input_file_heic_heif, name_save="RESULT_IMAGE"):

    try:
        format_save = "png"

        print("REALIZANDO A CONVERSÃO DA IMAGEM")

        # REALIZANDO A LEITURA DA IMAGEM
        heic_heic_file = pillow_heif.read_heif(input_file_heic_heif)

        # CONVERTENDO A IMAGEM EM PILLOW
        image = Image.frombytes(
            heic_heic_file.mode,
            heic_heic_file.size,
            heic_heic_file.data,
            "raw",
        )

        # SALVANDO A IMAGEM NO FORMATO ESCOLHIDO
        image.save("{}.{}".format(name_save, format_save), format(format_save))

        print("CONVERSÃO DA IMAGEM REALIZADA COM SUCESSO")
    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))


