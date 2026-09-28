"""Find custom voices on this key's project, then try to speak with the first match for NAME."""
import base64, json, os, sys, urllib.request, urllib.error
KEY = os.environ["GEMINI_API_KEY"]; NAME = os.environ.get("VOICE_NAME", "ASMR 3").lower()
B = "https://generativelanguage.googleapis.com/v1beta"
def call(method, path, body=None):
    req = urllib.request.Request(B + path, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=300) as r: return r.status, json.load(r)
    except urllib.error.HTTPError as e: return e.code, e.read().decode()[:600]
st, d = call("GET", "/voices?pageSize=100")
print("LIST", st)
voices = d.get("voices", []) if isinstance(d, dict) else []
if not isinstance(d, dict): print(d)
custom = [v for v in voices if v.get("type", "").lower() not in ("prebuilt", "voice_type_prebuilt")]
for v in custom: print("CUSTOM:", json.dumps({k: v.get(k) for k in ("id","name","displayName","display_name","type","description","gender","accent")}))
print("first keys:", list(voices[0].keys()) if voices else None, "| total", len(voices))
match = [v for v in custom if NAME in json.dumps(v).lower()] or custom
if not match: sys.exit("no custom voice found on this project")
vid = match[0].get("id") or match[0].get("name")
print("USING", vid)
text = "Hi. It's Otto. It's night on your side of the Earth, and I'm up here on the night shift. I'll keep watch, so you don't have to."
tries = {
 "generateContent+voice": ("/models/gemini-3.8-flash-tts:generateContent", {"contents":[{"parts":[{"text":text}]}],
     "generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voice": vid}}}),
 "generateContent+prebuiltName": ("/models/gemini-3.8-flash-tts:generateContent", {"contents":[{"parts":[{"text":text}]}],
     "generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"voiceConfig":{"prebuiltVoiceConfig":{"voiceName": vid}}}}}),
 "interactions": ("/interactions", {"model":"gemini-3.8-flash-tts","input":[{"type":"user_input","content":[{"type":"text","text":text}]}],
     "response_format":{"type":"audio"},"generation_config":{"speech_config":[{"voice": vid}]}}),
}
for name, (path, body) in tries.items():
    st, d = call("POST", path, body)
    if isinstance(d, dict):
        import re
        s = re.sub(r'"data": "[^"]{60}[^"]*"', '"data": "<audio>"', json.dumps(d))
        print(name, st, s[:1200])
    else:
        print(name, st, d)
