import json


def save_json(data):
    with open(f"data/chorus.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def serialize(data):
    return {
        'domain_name': data[1],
        'logo_url': data[2],
        'company_name': data[0]
    }
