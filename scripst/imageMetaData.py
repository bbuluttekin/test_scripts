from PIL import Image
from PIL.ExifTags import TAGS
import glob


def extractMetaData(image, output):
    """
    Extract meta data from photos and output them either to console or save it to file.

    Variables:
    ==========

    image: Full path to image (str)
    output: Name of the file you want to save the meta data (str)
    """
    try:
        metaData = {}

        imageFile = Image.open(image)
        rawData = imageFile._getexif()
        if rawData:
            for (tag, value) in rawData.items():
                tagName = TAGS.get(tag, tag)
                metaData[tagName] = value
            return metaData
        if output:
            with open(output, "w") as f:
                for (tagName, value) in metaData.items():
                    f.write(tagName + "," + value + "\n")
    except:
        print("Could not open the image process failed!")


def transformGPSData(lat, lon):
    pass


if __name__ == '__main__':
    for img in glob.glob("*.jpg"):
        meta = extractMetaData(img, output=None)
        # print(meta["GPSInfo"][2][0][0])
