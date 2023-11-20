# Stable Diffusion over FastAPI

Generates a Pokemon-style image based off a prompt.

## Usage

Easy to run with Docker

1. Clone stable-diffusion-pokemons-tome-quantized
2. Build
3. Run with:

```bash
docker run --rm -p 2626:2626 -v /stable-diffusion-pokemons-tome-quantized:/app/stable-diffusion-pokemons-tome-quantized <img>
```