"""Voice test: Chatterbox (free, MIT). Makes samples in assets/audio/voice-tests/cb_*.wav"""
import os, subprocess, time
import torchaudio
from chatterbox.tts import ChatterboxTTS

TEXT = [
    "Hi. It's Otto. It's night on your side of the Earth, and I'm up here on the night shift. I'll keep watch, so you don't have to.",
    "Tonight, let's think slowly about time. Here's something that might surprise you. The theory of relativity started with a question so simple that a teenager asked it.",
    "What would it look like, if you could ride alongside a beam of light? Just sit with that for a moment.",
    "You don't need to understand all of it. If you fall asleep halfway, that's the plan.",
]
OUT = "assets/audio/voice-tests"
model = ChatterboxTTS.from_pretrained(device="cpu")
refs = {"default": None,
        "ref_george_onyx": f"{OUT}/blend_george_onyx.wav",
        "ref_michael_onyx": f"{OUT}/blend_michael_onyx.wav",
        "ref_onyx": f"{OUT}/am_onyx.wav"}
import torch
for name, ref in refs.items():
    t = time.time(); parts = []
    for line in TEXT:
        w = model.generate(line, audio_prompt_path=ref, exaggeration=0.3, cfg_weight=0.4, temperature=0.7)
        parts += [w, torch.zeros(1, int(model.sr * 0.6))]
    path = f"{OUT}/cb_{name}.wav"
    torchaudio.save(path, torch.cat(parts, dim=1), model.sr)
    print(name, "took %.0fs" % (time.time() - t), flush=True)
