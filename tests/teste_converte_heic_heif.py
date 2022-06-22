import base64
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.base64_encode_decode import image_to_base64, base64_get_extension
from src.convert_heic_heif_to_png import convert_heic_heif_to_png

input_image = '../fixtures/IMG_4108.HEIC'

# CONVERTENDO PARA BASE64
input_image_base64 = image_to_base64(input_image)

# DECODIFICANDO A BASE64
result_decode = base64.b64decode(input_image_base64.decode())

# OBTENDO A EXTENSÃO
extension = base64_get_extension(result_decode)

print("-"*50)
print("A EXTENSÃO DO ARQUIVO É {}".format(extension))

if extension in [".heic", ".heif"]:
    save_output_format = ".jpg"

    convert_heic_heif_to_png(input_image, name_save="RESULT_IMAGE")