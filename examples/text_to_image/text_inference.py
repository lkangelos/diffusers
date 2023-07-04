from diffusers import StableDiffusionPipeline

def main():
    generator = StableDiffusionPipeline.from_pretrained("/home/louanqi/pycharm/diffusers/examples/text_to_image/sd-pokemon-model")
    generator.to("cuda:3")

    prompt = "A pokemon with red eyes and black legs."
    image = generator(prompt).images[0]
    image.save("./examples/text_to_image/generated_image.png")

if __name__ == "__main__":
    main()