"""

    FUNÇÕES UTEIS PARA CODIFICAÇÃO E DECODIFICAÇÃO DE BASE64.

    A SAÍDA DA DECODIFICAÇÃO É NO FORMATO ARQUIVO IMAGEM (SALVO NA PASTA RAIZ).

    # Arguments
        file_base64                - Required : Input no formato Base64 (BASE64)

    # Returns
        built_pdf                  - Required : Caminho/Nome do arquivo gerado (String)

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "22/06/2022"


import base64
from inspect import stack
import imghdr
import mimetypes
import os

from winmagic import magic


def base64_get_extension(file_base64_decode):

    """

        ESSA FUNÇÃO RETORNA O TIPO DA IMAGEM DECODIFICADA DO BASE64.

        PARA OBTER A EXTENSÃO UTILIZA-SE O MIMETYPE:
            ADIVINHA A EXTENSÃO DE UM ARQUIVO COM BASE EM SEU TIPO MIME,
            FORNECIDO POR TIPO .
            O VALOR DE RETORNO É UMA STRING QUE FORNECE UMA
            EXTENSÃO DE NOME DO ARQUIVO, INCLUINDO O PONTO INICIAL ('.')

        # Arguments
            file_base64_decode           - Required : Input no formato
                                                      Base64 Decodificado (String)

        # Returns
            extension                    - Required : Extensão da imagem
                                                      decodificada (String)

    """

    extension = None

    try:
        # VERIFICANDO SE É UM ARQUIVO HEIC
        if str(file_base64_decode).find("heic")!=-1:
            extension = ".heic"
        # VERIFICANDO SE É UM ARQUIVO HEIF
        elif str(file_base64_decode).find("heif") != -1:
            extension = ".heif"
        else:

            # OBTENDO A EXTENSÃO DE UMA IMAGEM
            extension = imghdr.what(None, h=file_base64_decode)

            if extension is None:
                # O ARQUIVO ENVIADO NÃO É IMAGEM
                # OBTENDO A EXTENSÃO
                mime_type = magic.from_buffer(file_base64_decode, mime=True)
                extension = mimetypes.guess_extension(mime_type)
            else:
                extension = "{}{}".format(".", extension)

        return extension

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))
        return None


def isbase64(input_file):

    """

         VERIFICA SE UM VALOR É UMA BASE64.

         FUNCIONA PARA VALORES EM FORMATO:
            1) BYTES
            2) STRING

         # Arguments
            input_file                 - Required : Valor a ser verificado (Bytes | String)

        # Returns
            verificator                - Required : Verificador de base64 (Boolean)

    """

    try:
        # VERIFICANDO SE O ENVIADO ESTÁ EM FORMATO STRING
        if isinstance(input_file, str):

            # CONVERTENDO A STRING EM BYTES
            input_file_bytes = bytes(input_file, 'ascii')

        # VERIFICANDO SE O ENVIADO ESTÁ EM FORMATO DE BYTES
        elif isinstance(input_file, bytes):

            # MANTENDO EM BYTES
            input_file_bytes = input_file

        else:
            raise ValueError("Argument must be string or bytes")

        return base64.b64encode(base64.b64decode(input_file_bytes)) == input_file_bytes, input_file_bytes

    except Exception:
        return False, None


def base64_to_image(file_base64):

    """

         ESSA FUNÇÃO TEM COMO OBJETIVO, CONVERTER FORMATO DE INPUT (BASE64) -> IMAGE (PNG)

         O ARQUIVO OBTIDO (PNG) É SALVO NA MÁQUINA QUE ESTÁ EXECUTANDO O MODELO.

         # Arguments
            file_base64                - Required : Input no formato Base64 (BASE64)

        # Returns
            built_image                - Required : Caminho/Nome do arquivo gerado (String)

    """

    built_image = None

    try:
        # DECODOFICANDO A BASE64
        result_decode = base64.b64decode(file_base64.decode())

        # OBTENDO A EXTENSÃO DO ARQUIVO
        extension = base64_get_extension(result_decode)

        # FORMATANDO O NOME DE SAVE
        built_image = os.path.join(os.getcwd(), "{}{}".format("INPUT_BASE64", ".png"))

        # REALIZANDO A ABERTURA DE UM ARQUIVO (QUE SERÁ ESCRITO NA MÁQUINA)
        with open(built_image, "wb") as image_base64:

            try:
                # SALVANDO A IMAGEM DECODIFICADA
                image_base64.write(result_decode)

            except Exception as ex:
                print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {]".format(stack()[0][3], ex))

    return built_image


def image_to_base64(file_image):

    """

         ESSA FUNÇÃO TEM COMO OBJETIVO, CONVERTER FORMATO DE INPUT (PNG) -> BASE64

         O ARQUIVO OBTIDO (PNG) É SALVO NA MÁQUINA QUE ESTÁ EXECUTANDO O MODELO.

         # Arguments
            file_image                - Required : Caminho do arquivo
                                                   no formato imagem (String)

        # Returns
            built_base64              - Required : Valor no formato Base64 (BASE64)

    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ O VALOR DA BASE64
    built_base64 = None

    try:
        # DECODOFICANDO A BASE64, ARMAZENANDO-O NO OBJETO ABERTO
        # ESCREVENDO NA MÁQUINA
        built_base64 = base64.b64encode(open(file_image, 'rb').read())

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return built_base64