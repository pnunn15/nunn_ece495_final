# Stable Diffusion over FastAPI

Runs a quantized Stable Diffusion model trained on Pokemon images. The model is served with FastAPI running on uvicorn. Steps to run are listed below.

## Usage

### Easy to run with Docker

1. Clone stable-diffusion-pokemons-tome-quantized
```bash
git clone https://huggingface.co/OpenVINO/stable-diffusion-pokemons-tome-quantized
```
2. Pull the baseline docker image
```bash
docker pull intel/intel-optimized-pytorch
```
3. Build the image
```bash
docker build -t <img_name>:<version> .
```
4. Run with the following command. Be sure to update the source directory for the volume mount to the location where you cloned the model.
```bash
docker run --rm -p 2626:2626 -v /stable-diffusion-pokemons-tome-quantized:/app/stable-diffusion-pokemons-tome-quantized <img>
```


5. In separate terminal, call
```bash
curl -o myimage.jpg "http://localhost:2626/generate_img?prompt=<your prompt>"
```