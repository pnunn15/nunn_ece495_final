"""Serve StableDiffusion v1.5 with FastAPI
* Run: uvicorn genimg:app --host 0.0.0.0 --port 2626
* Run Docker Image: docker run --rm -p 2626:2626 -v /stable-diffusion-pokemons-tome-quantized:/app/stable-diffusion-pokemons-tome-quantized <img>
* Call: curl -o myimage.jpg "http://localhost:2626/generate_img?prompt=outerspace
"""
from optimum.intel.openvino import OVStableDiffusionPipeline
from diffusers.training_utils import set_seed
from fastapi import FastAPI
from fastapi.responses import Response
from io import BytesIO

path_to_model = "./stable-diffusion-pokemons-tome-quantized"

optimized_pipe = OVStableDiffusionPipeline.from_pretrained(
    path_to_model, compile=False)

optimized_pipe.reshape(batch_size=1, height=512, width=512, num_images_per_prompt=1)
optimized_pipe.compile()

# Create the FastAPI app
app = FastAPI()


@app.get("/generate_img")
async def generate_img(prompt: str, seed: int=26, steps: int=20):
    """Uses a diffusion model to generate and return an image based on the prompt."""
    # Set the seed for inference.
    set_seed(seed)
    # Generate the image based on the prompt
    image = optimized_pipe(prompt, num_inference_steps=steps, output_type="pil").images[0]

    # Convert the PIL Image to bytes in memory
    image_bytes_io = BytesIO()
    image.save(image_bytes_io, format="JPEG")
    image_data = image_bytes_io.getvalue()

    # Indicate that you are returning a JPEG image
    headers = {
        "Content-Type": "image/jpeg",
    }

    # Return the image in a Response object
    # This works with a simple `curl -o myimage.jpg ...`
    return Response(content=image_data, headers=headers)
