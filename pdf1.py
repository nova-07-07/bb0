from pdf2image import convert_from_path

# Convert PDF pages to images
images = convert_from_path("I:\\bible\\pdf1.pdf")

# Save images to the folder
image_files = []
for i, img in enumerate(images):
    img_filename = f"pdf1img{i+1}.jpeg"
    img_path = os.path.join(image_folder, img_filename)
    img.save(img_path, "JPEG")
    image_files.append(img_filename)

# Return the list of extracted images
image_files
