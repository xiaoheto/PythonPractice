from PIL import Image

input_path = "images/moli_source.png"
output_path = "images/moli.bmp"

# 2. 目标的尺寸和背景颜色 (F0FFFF - 242550, 255, 255)
target_size = (60, 58)
target_bg_color = (255, 255, 255)

try:
    with Image.open(input_path) as img:
        
        resized_img = img.resize(target_size, resample=Image.NEAREST)
        
        final_img = Image.new('RGB', target_size, target_bg_color)
        if 'A' in resized_img.mode:
            final_img.paste(resized_img, (0, 0), resized_img)
        else:
            final_img.paste(resized_img, (0, 0))

        final_img.save(output_path, "BMP")
        print(f"成功将图像保存为: {output_path}，尺寸为 {final_img.size}")

except FileNotFoundError:
    print(f"错误: 找不到文件 {input_path}。")
except Exception as e:
    print(f"发生了一个错误: {e}")