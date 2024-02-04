from rembg import remove 
from PIL import Image 

input_path="C:\\Users\\bansa\\Desktop\\nameLogo.png"
output_path="C:\\Users\\bansa\\Desktop\\output.png"

input=Image.open(input_path)
output=remove(input)

output.save(output_path,format='PNG')