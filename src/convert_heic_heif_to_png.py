"""

    FUNÇÃO PARA CONVERSÃO DE UM ARQUIVO HEIC OU HEIF PARA PNG

    # Arguments
        input_file_heic_heif       - Required: Local onde está
                                               o arquivo de imagem (String)
        name_save                  - Optional: Nome de save do
                                               arquivo formatado (String)

    # Returns
        validator                  - Required : Validador de
                                                execução da função (Boolean)

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "22/06/2022"


from inspect import stack
from PIL import Image

import pillow_heif


def convert_heic_heif_to_png(input_file_heic_heif, name_save="RESULT_IMAGE"):

    """

        FUNÇÃO PARA CONVERSÃO DE UM ARQUIVO HEIC OU HEIF PARA PNG

        ESSA FUNÇÃO NÃO REALIZA A VERIFICAÇÃO SE O INPUT É HEIC OU HEIF,
        APENAS REALIZA A TENTATIVA DE CONVERSÃO.

        # Arguments
            input_file_heic_heif       - Required: Local onde está
                                                   o arquivo de imagem (String)
            name_save                  - Optional: Nome de save do
                                                   arquivo formatado (String)

        # Returns
            validator                  - Required : Validador de
                                                    execução da função (Boolean)

    """

    validator = False

    try:
        format_save = "png"

        if (input_file_heic_heif is not None) and (input_file_heic_heif != ""):

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

            validator = True

        else:
            print("FORNEÇA UM CAMINHO DE IMAGEM VÁLIDO")

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validator


