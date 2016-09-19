#coding:utf-8

__author__ = "Tacey Wong"


#简单qr "Some text" > test.png



import qrcode 
import Image
import qrcode.image.svg
import os

# img = qrcode.make('中文')
# img.save('test.png')

#     factory = qrcode.image.svg.SvgImage
#     factory = qrcode.image.svg.SvgFragmentImage
#     factory = qrcode.image.svg.SvgPathImage

# img = qrcode.make('Some data here', image_factory=factory)


def gen_qrcode(text,path,logo=None,type=None):
    """
        二维码生成
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=1
    )
    qr.add_data(text)
    
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    if logo and os.path.exists(logo):  
        icon = Image.open(logo)  
        img_w, img_h = img.size  
        factor = 4  
        size_w = int(img_w / factor)  
        size_h = int(img_h / factor)  
 
        icon_w, icon_h = icon.size  
        if icon_w > size_w:  
            icon_w = size_w  
        if icon_h > size_h:  
            icon_h = size_h  
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)  
 
        w = int((img_w - icon_w) / 2)  
        h = int((img_h - icon_h) / 2)  
        icon = icon.convert("RGBA")  
        img.paste(icon, (w, h), icon)  
    img.save(path)  


import zbar
def rec_qrcode(code_pic):
    """
        二维码识别
    """
    scanner = zbar.ImageScanner()
    scanner.parse_config("enable")
    img = Image.open(code_pic).convert("L")
    w,h = img.size
    zimg = zbar.Image(w,h,"Y800",img.tobytes())

    scanner.scan(zimg)

    for s in zimg:
        print s.type,s.data


# import qrcode



if __name__ == "__main__":
    gen_qrcode(text="zzzz中文什搜索么z",path="test.png",logo="logo.jpg")
    rec_qrcode("test.png")