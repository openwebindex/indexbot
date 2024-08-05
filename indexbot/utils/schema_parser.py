import json

def parse_schema(response):
    # Example: Extract JSON-LD data from <script type="application/ld+json">
    script_data = response.xpath('//script[@type="application/ld+json"]/text()').get()
    if script_data:
        try:
            schema_data = json.loads(script_data)
            return schema_data
        except json.JSONDecodeError:
            return None
    return None
