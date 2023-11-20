FROM intel/intel-optimized-pytorch

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt --no-cache-dir

COPY stable-diffusion-pokemons-tome-quantized/ .
COPY genimg.py .
# ENV PYTHONUNBUFFERED=1
EXPOSE 2626
# CMD [ "python", "./stable_diffusion_pokemon_quantization.py" ]
# # CMD [ "catimg", "sd_quantized_pokemon.png"]
# # CMD [ "python", "-m", "http.server" ]
ENTRYPOINT [ "uvicorn", "genimg:app", "--host", "0.0.0.0", "--port", "2626" ]
