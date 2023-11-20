FROM intel/intel-optimized-pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt --no-cache-dir

# COPY stable_diffusion_pokemon_quantization.py ./
COPY stable-diffusion-pokemons-tome-quantized/ .

# ENV PYTHONUNBUFFERED=1

# CMD [ "python", "./stable_diffusion_pokemon_quantization.py" ]
# # CMD [ "catimg", "sd_quantized_pokemon.png"]
# # CMD [ "python", "-m", "http.server" ]