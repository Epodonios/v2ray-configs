
import base64, json, os, sys, glob
from urllib.parse import urlparse, parse_qs, urlencode, quote, unquote

def decode_vmess(link):
    if not link.startswith("vmess://"):
        return None
    data = link[len("vmess://"):]
    padded = data + '=' * (-len(data) % 4)
    try:
        obj = json.loads(base64.b64decode(padded).decode())
        return obj
    except Exception:
        return None

def encode_vmess(obj):
    s = json.dumps(obj, separators=(',', ':'))
    enc = base64.b64encode(s.encode()).decode().rstrip('=')
    return "vmess://" + enc

def process_vless(link, new_remark):
    if not link.startswith("vless://"):
        return None
    try:
        parts = urlparse(link)
        qs = parse_qs(parts.query)
        tag = quote(new_remark)
        base = f"{parts.scheme}://{parts.netloc}{parts.path}"
        query = f"?{parts.query}" if parts.query else ""
        return f"{base}{query}#{tag}"
    except:
        return None

def process_ss(link, new_remark):
    if not link.startswith("ss://"):
        return None
    try:
        if '#' in link:
            base, _ = link.split('#', 1)
        else:
            base = link
        return f"{base}#{quote(new_remark)}"
    except:
        return None

def process_line(line, new_remark):
    if line.startswith("vmess://"):
        obj = decode_vmess(line)
        if obj is not None:
            obj['ps'] = new_remark
            return encode_vmess(obj)
    elif line.startswith("vless://"):
        return process_vless(line, new_remark)
    elif line.startswith("ss://"):
        return process_ss(line, new_remark)
    return line  # untouched

def process_file(path, new_remark):
    tmp = path + '.tmp'
    with open(path, 'r', encoding='utf-8') as fin, open(tmp, 'w', encoding='utf-8') as fout:
        for line in fin:
            line = line.strip()
            new_line = process_line(line, new_remark)
            fout.write(new_line + '\n')
    os.replace(tmp, path)
    print(f"✅ {os.path.basename(path)} به‌روزرسانی شد.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python change_remark_all.py <new_remark>")
        sys.exit(1)

    new_remark = sys.argv[1]
    sub_files = glob.glob("Sub*.txt")

    if not sub_files:
        print("هیچ فایل Sub*.txt پیدا نشد.")
        sys.exit(1)

    for file in sub_files:
        process_file(file, new_remark)
