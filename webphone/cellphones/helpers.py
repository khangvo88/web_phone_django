from django.conf import settings
import os
from django.utils import timezone

def cut_to_block_n(items,block=3):
    """ remove the tail so that only muliply of n-block appear.
     Note if items is smaller than n then return all. Useful for slideshow script
     default block = 3"""
    num_show = int(len(items) / block)
    if num_show > 0:
        results = items[:block * num_show]
    else:
        results = items
    return results


def device_image_upload_to(instance, filename):
    # file will be uploaded to MEDIA_ROOT/device_<id>/<filename>
    ext = filename.split('.')[-1]
    name=""
    if hasattr(instance, "name") and instance.name!="":
        name = instance.name+"_"
    return "device/{0}/{1}{2}.{3}".format(instance.id,name,timezone.now().strftime("%Y%m%d"),ext)

def handle_uploaded_file(f):
    """upload file <f> into <settings.MEDIA_URL>"""
    if not f:
        return None
    with open(settings.MEDIA_ROOT+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def generate_file_name(filename):
    new_name = ''
    ii = 1
    while True:
        new_name = checkDupAndGenerateFileNameOnWebserver(filename, "_" + str(ii))
        if new_name:
            break
        ii += 1
    return new_name


def checkDupAndGenerateFileNameOnWebserver(namefile, ii):
    file_root, file_ext = os.path.splitext(namefile)
    if len(namefile) > settings.MAX_LENGTH_NAME_FILE:
        return ''
    elif not os.path.isfile(settings.TMP_STORE + '/' + namefile) and not os.path.isfile(
                                    settings.TMP_STORE + '/' + file_root + '.png'):
        return namefile
    else:
        newnamefile = file_root + ii + file_ext
        return checkDupAndGenerateFileNameOnWebserver(newnamefile, ii)